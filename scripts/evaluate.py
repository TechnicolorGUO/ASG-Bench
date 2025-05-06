from concurrent.futures import ThreadPoolExecutor, as_completed
import glob
import json
import math
import os
import dotenv
import pandas as pd
from prompts import CONTENT_EVALUATION_PROMPT, OUTLINE_EVALUATION_PROMPT, CRITERIA, OUTLINE_STRUCTURE_PROMPT, REFERENCE_EVALUATION_PROMPT, OUTLINE_COVERAGE_PROMPT, REFERENCE_QUALITY_PROMPT
from reference import split_markdown_content_and_refs
from utils import build_outline_tree_from_levels, count_md_features, count_sentences, extract_and_save_outline_from_md, extract_references_from_md, extract_topic_from_path, getClient, generateResponse, pdf2md, refine_outline_if_single_level, robust_json_parse,fill_single_criterion_prompt, read_md
import logging
from atomic_facts import extract_and_deduplicate_facts

class Judge():
    def __init__(self):
        dotenv.load_dotenv()
        with open('judge.log', 'w') as log_file:
            log_file.truncate(0)
        self.client = getClient()
        # Configure logging
        logging.basicConfig(filename='judge.log', level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
    
    def judge(self, prompt):
        """
        :param prompt: str
        :return: str
        """
        response = generateResponse(self.client, prompt)
        logging.info(f"Response received: {response}")  # Log the response
        try:
            result = robust_json_parse(response)
            return result
        except Exception as e:
            logging.error(f"Error parsing JSON: {e}")  # Log the error
            print("Error parsing JSON:", e)
            return None
        
judge = Judge()

def extract_topic_from_path(md_path: str) -> str:
    """
    Extract topic from the grandparent folder name of the given path.
    """
    abs_path = os.path.abspath(md_path)
    topic = os.path.basename(os.path.dirname(os.path.dirname(abs_path)))
    return topic

def evaluate_outline_llm(outline_json_path: str) -> dict:
    criteria_name = "Outline"
    results = {}
    try:
        # 1. 读取 outline.json
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)

        # 2. 格式化 outline 为字符串
        outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])

        # 3. 用祖父文件夹名作为 topic
        topic = extract_topic_from_path(outline_json_path)

        # 4. 构建 prompt 并获取分数
        criterion = CRITERIA[criteria_name]
        prompt = fill_single_criterion_prompt(
            prompt_template=OUTLINE_EVALUATION_PROMPT,
            content=outline_str,
            topic=topic,
            criterion=criterion,
            criteria_name=criteria_name,
            type="outline"
        )
        score_dict = judge.judge(prompt)
        if not (isinstance(score_dict, dict) and criteria_name in score_dict):
            results[criteria_name] = 0
        else:
            results.update(score_dict)
    except Exception as e:
        results[criteria_name] = 0
    return results

# def evaluate_outline_coverage(
#     outline_json_path: str,
#     standard_count: int = 10,
#     ideal_section_count: int = 30,
#     sigma: float = 15.0
# ) -> float:
#     """
#     评估大纲综合得分 Q'，融合模板完整度、创新丰富度和长度惩罚。

#     Args:
#         outline_json_path (str): 大纲JSON路径
#         standard_count (int): 标准section总数 N
#         ideal_section_count (int): 理想section总数 M*
#         sigma (float): 惩罚宽度参数

#     Returns:
#         float: 综合得分 Q'
#     """
#     try:
#         with open(outline_json_path, "r", encoding="utf-8") as f:
#             outline_list = json.load(f)

#         total_section_count = len(outline_list)  # M

#         outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])
#         topic = extract_topic_from_path(outline_json_path)
#         prompt = OUTLINE_COVERAGE_PROMPT.format(
#             outline=outline_str,
#             topic=topic,
#         )
#         response = judge.judge(prompt)
#         matched_count = response.get("matched_count", 0)   # K

#         K = matched_count
#         N = standard_count
#         M = total_section_count
#         M_star = ideal_section_count
#         U = max(M - K, 0)

#         R = K / N if N > 0 else 0
#         O = U / M if M > 0 else 0

#         F_harmonic = 2 * R * O / (R + O) if (R + O) > 0 else 0

#         L = math.exp(-((M - M_star) ** 2) / (2 * sigma ** 2)) if sigma > 0 else (1.0 if M == M_star else 0.0)

#         Q_prime = F_harmonic * L

#         return Q_prime

#     except Exception as e:
#         print("Error in evaluating outline coverage:", e)
#         return 0.0

def evaluate_outline_coverage(
    outline_json_path: str,
    standard_count: int = 10,      # 标准参考section数，用于覆盖率
    avg_count: int = 30,           # 理想/期望section数，用于长度对数惩罚
    min_section_count: int = 5     # 最小允许section数
) -> float:
    """
    评估大纲综合得分 Q'，包含对长度的对数惩罚项。
    - standard_count: 用于计算匹配覆盖率K/N
    - avg_count: 用于对数长度惩罚
    """
    try:
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)

        total_section_count = len(outline_list)
        outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])
        topic = extract_topic_from_path(outline_json_path)
        prompt = OUTLINE_COVERAGE_PROMPT.format(
            outline=outline_str,
            topic=topic,
        )
        response = judge.judge(prompt)
        matched_count = response.get("matched_count", 0)

        K = matched_count         # 实际匹配到的section数
        N = standard_count        # 覆盖率参考标准数
        M = total_section_count   # 实际section数
        print(f"Matched count: {K}, Total section count: {M}.")
        U = max(M - K, 0)

        R = K / N if N > 0 else 0
        O = U / M if M > 0 else 0
        F_harmonic = 2 * R * O / (R + O) if (R + O) > 0 else 0

        # 对数惩罚项：以avg_count为基准
        if M < min_section_count:
            length_penalty = 0
        else:
            length_penalty = min(1.0, math.log(max(M, 1) + 1) / math.log(avg_count + 1))
            # 这里avg_count是对数归一化的分母

        Q_prime = F_harmonic * length_penalty

        return Q_prime

    except Exception as e:
        print(f"Error evaluating outline coverage: {e}")
        return 0.0

def evaluate_outline_structure(outline_json_path):
    """
    对 [level, title] 大纲结构评估层级合理性
    
    Returns:
        global_score: 全局结构合理性得分
        node_scores: 每个非叶节点的分数列表
    """
    with open(outline_json_path, "r", encoding="utf-8") as f:
        outline_list = json.load(f)
    node_objs, _ = build_outline_tree_from_levels(outline_list)
    non_leaf_nodes = [node for node in node_objs if node["children"]]
    node_scores = []
    for parent in non_leaf_nodes:
        children_list = "\n".join([
            f'  - Index: {child["index"]}, Title: {child["title"]}'
            for child in parent["children"]
        ])
        prompt = OUTLINE_STRUCTURE_PROMPT.format(
            parent_index=parent["index"],
            parent_title=parent["title"],
            children_list=children_list
        )
        # LLM调用（这里用模拟的judge函数代替）
        response = judge.judge(prompt)
        result = response.get("children", [])
        yes_count = sum(1 for child in result if str(child.get("is_included", "")).lower() == "yes")
        total = len(result)
        node_score = yes_count / total if total > 0 else 1.0  # 无子节点记满分（通常会被过滤掉）
        node_scores.append({
            "parent_index": parent["index"],
            "parent_title": parent["title"],
            "score": node_score
        })

    global_score = sum(x["score"] for x in node_scores) / len(node_scores) if node_scores else 1.0
    return global_score, node_scores

def evaluate_outline(
    md_path: str,
    do_llm: bool = True,
    do_coverage: bool = True,
    do_structure: bool = True
) -> dict:
    results = {}
    outline_json_path = os.path.join(os.path.dirname(md_path), "outline.json")
    # 1. Extract outline from md（如果没有 outline.json 才提取）
    if not os.path.exists(outline_json_path):
        try:
            extract_and_save_outline_from_md(md_path)
            outline_raw_json_path = os.path.join(os.path.dirname(md_path), "outline_raw.json")
        except Exception as e:
            print("Error extracting outline:", e)
            return results
    else:
        print(f"Found {outline_json_path}, skip extraction.")
        outline_raw_json_path = os.path.join(os.path.dirname(md_path), "outline.json")

    # 2. LLM 评测
    if do_llm:
        try:
            outline_results = evaluate_outline_llm(outline_raw_json_path)
            results.update(outline_results)
        except Exception as e:
            print("Error in evaluating outline llm:", e)
            results["Outline"] = 0
    else:
        print("Skip evaluate_outline_llm.")

    # 3. Coverage 评测
    if do_coverage:
        try:
            coverage_results = evaluate_outline_coverage(outline_raw_json_path)
            results["Outline_coverage"] = coverage_results
        except Exception as e:
            print("Error in evaluating outline coverage:", e)
            results["Outline_coverage"] = 0
    else:
        print("Skip evaluate_outline_coverage.")

    # 4. Structure 评测
    outline_json_path = os.path.join(os.path.dirname(md_path), "outline.json")
    refine_outline_if_single_level(outline_raw_json_path, outline_json_path)
    if do_structure:
        try:
            global_score, node_scores = evaluate_outline_structure(outline_json_path)
            results["Outline_structure"] = global_score
        except Exception as e:
            print("Error in evaluating outline structure:", e)
            results["Outline_structure"] = 0
    else:
        print("Skip evaluate_outline_structure.")

    print("The score is: ", results)
    return results

def evaluate_content_llm(md_path: str) -> dict:
    """
    Evaluate all specified content-related criteria and return a dict of all scores.
    If file reading or scoring fails, assign a score of 0 for that criterion.
    :param md_path: Markdown file path
    :return: dict {criteria_name: score, ...}
    """
    content_criteria = ["Coverage", "Structure", "Relevance", "Language", "Criticalness"]
    results = {}

    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content_str = f.read()
    except Exception as e:
        for criteria_name in content_criteria:
            results[criteria_name] = 0
        print("All content criteria scores:", results)
        return results

    topic = extract_topic_from_path(md_path)

    for criteria_name in content_criteria:
        criterion = CRITERIA[criteria_name]
        prompt = fill_single_criterion_prompt(
            prompt_template=CONTENT_EVALUATION_PROMPT,
            content=content_str,
            topic=topic,
            criterion=criterion,
            criteria_name=criteria_name,
            type= "content"
        )
        try:
            score_dict = judge.judge(prompt)
            if not (isinstance(score_dict, dict) and criteria_name in score_dict):
                results[criteria_name] = 0
            else:
                results.update(score_dict)
        except Exception as e:
            results[criteria_name] = 0

    print("All content criteria scores:", results)
    return results

def evaluate_content_informativeness(md_path: str) -> dict:
    md_content = read_md(md_path)
    counts = count_md_features(md_content)
    sentences = counts.get('sentences', 1)
    results = {}    

    images_density = counts.get('images', 0) / sentences
    equations_density = counts.get('equations', 0) / sentences
    tables_density = counts.get('tables', 0) / sentences
    total_density = (counts.get('images', 0) + counts.get('equations', 0) + counts.get('tables', 0)) / sentences

    results["Images_density"] = images_density * 100
    results["Equations_density"] = equations_density * 100
    results["Tables_density"] = tables_density * 100
    results["Total_density"] = total_density * 100

    # Claim density
    topic = extract_topic_from_path(md_path)
    results_claims = extract_and_deduplicate_facts(md_content, topic)
    results["Claim_density_before_deduplication"] = results_claims.get("claim_density_before_dedup", 0) * 100
    results["Claim_density_after_deduplication"] = results_claims.get("claim_density_after_dedup", 0) * 100
    print("Informativeness scores:", results)
    return results

def evaluate_content(
    md_path: str,
    do_llm: bool = True,
    do_info: bool = True,
    do_faithfulness: bool = True  # 先注释掉实现
) -> dict:
    results = {}
    content_criteria = [
        "Coverage", "Structure", "Relevance", "Language", "Criticalness"
    ]
    info_criteria = [
        "Images_density", "Equations_density", "Tables_density", 
        "Total_density", "Claim_density_before_deduplication", 
        "Claim_density_after_deduplication"
    ]
    # 1. LLM 评测部分
    if do_llm:
        try:
            results.update(evaluate_content_llm(md_path))
        except Exception as e:
            print("Error in evaluating content:", e)
            for criteria_name in content_criteria:
                results[criteria_name] = 0
    else:
        print("Skip evaluate_content_llm.")

    # 2. 信息量评测部分
    if do_info:
        try:
            results.update(evaluate_content_informativeness(md_path))
        except Exception as e:
            print("Error in evaluating content informativeness:", e)
            for criteria_name in info_criteria:
                results[criteria_name] = 0
    else:
        print("Skip evaluate_content_informativeness.")

    # 3. 事实性评测部分（暂未实现，先注释）
    if do_faithfulness:
        try:
            # 测试 得分为0
            results.update({"faithfulness": 0})
        except Exception as e:
            print("Error in evaluating content faithfulness:", e)
            results['faithfulness'] = 0
    else:
        print("Skip evaluate_content_faithfulness.")


    print("Content evaluation scores:", results)
    return results

def evaluate_reference_llm(md_path: str) -> dict:
    """
    Extract references from the given Markdown file, call LLM to evaluate relevance,
    and return {"Reference": score}. If extraction or scoring fails, assign a score of 0.
    :param md_path: Markdown file path
    :return: dict, key is "Reference", value is the score
    """
    results = {}
    criteria_name = "Reference"
    try:
        references = extract_references_from_md(md_path)
        if not references:
            results[criteria_name] = 0
            print("No references found.")
            return results

        topic = extract_topic_from_path(md_path)
        criterion = CRITERIA[criteria_name]
        references_str = "\n".join(references)
        prompt = fill_single_criterion_prompt(
            prompt_template=REFERENCE_EVALUATION_PROMPT,
            content=references_str,
            topic=topic,
            criterion=criterion,
            criteria_name=criteria_name,
            type="reference"
        )
        try:
            score_dict = judge.judge(prompt)
            if not (isinstance(score_dict, dict) and criteria_name in score_dict):
                results[criteria_name] = 0
            else:
                results.update(score_dict)
        except Exception:
            print("Error in scoring references.")
            results[criteria_name] = 0
    except Exception:
        print("Error in extracting references.")
        results[criteria_name] = 0
    print("Reference evaluation score:", results)
    return results

def evaluate_reference_density(md_path: str) -> dict:
    results = {}

    json_path = os.path.join(os.path.dirname(md_path), "references.json")

    with open(json_path, "r", encoding="utf-8") as f:
        references = json.load(f)
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

        
    main_content, _ = split_markdown_content_and_refs(content)
    sentence_count = count_sentences(main_content)
    references_count = len(references)

    if sentence_count > 0:
        results["Reference_density"] = round(references_count / sentence_count, 4) * 100
    else:
        results["Reference_density"] = 0
    print("Reference density score:", results)
    return results

def evaluate_reference_quality(md_path: str) -> dict:
    results = {}
    csv_path = os.path.join(os.path.dirname(md_path), os.path.basename(md_path).replace(".md", ".csv"))  

    # csv columns: [sentence,references]
    refs_mapping = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = pd.read_csv(f)
        for index, row in reader.iterrows():
            sentence = row["sentence"]
            references = row["references"].split(";")
            refs_mapping[sentence] = references

    # Count the number of references that are relevant to the topic
    total_count = 0
    supported_count = 0
    topic = extract_topic_from_path(md_path)
    for sentence, references in refs_mapping.items():
        # Call LLM to evaluate the relevance of each reference
        prompt = REFERENCE_QUALITY_PROMPT.format(
            sentence=sentence,
            references="\n".join(references),
            topic=topic
        )
        try:
            response = judge.judge(prompt)
            total = response.get("total", 0)
            supported = response.get("supported", 0)
            total_count += int(total)
            supported_count += int(supported)
            print(f"Sentence: {sentence}, Total: {total}, Supported: {supported}")
        except Exception as e:
            total_count += 0
            supported_count += 0
            print("Error in evaluating reference quality:", e)
            continue
    # Calculate the average scores
    if total_count > 0:
        results["Reference_quality"] = round(supported_count / total_count, 4) * 100
    else:
        results["Reference_quality"] = 0
    print("Reference quality score:", results)
    return results

def evaluate_reference(
        md_path: str,
        do_llm: bool = True,
        do_density: bool = True,
        do_quality: bool = True
) -> dict:
    results = {}
    # 1. LLM 评测部分
    if do_llm:
        try:
            results.update(evaluate_reference_llm(md_path))
        except Exception as e:
            print("Error in evaluating reference:", e)
            results["Reference"] = 0
    else:
        print("Skip evaluate_reference_llm.")

    # 2. 密度评测部分
    if do_density:
        try:
            results.update(evaluate_reference_density(md_path))
        except Exception as e:
            print("Error in evaluating reference density:", e)
            results["Reference_density"] = 0
    else:
        print("Skip evaluate_reference_density.")

    # 3. 质量评测部分
    if do_quality:
        try:
            results.update(evaluate_reference_quality(md_path))
        except Exception as e:
            print("Error in evaluating reference quality:", e)
            results["Reference_quality"] = 0
    else:
        print("Skip evaluate_reference_quality.")

    return results
    
def evaluate(
    md_path: str, 
    model: str = "default",
    do_outline: bool = True, 
    do_content: bool = True, 
    do_reference: bool = True
) -> dict:
    """
    Evaluate the given Markdown file by selected criteria.
    :param md_path: Markdown文件路径
    :param model: 模型名（如qwen-plus）
    """
    results = {}
    # 拼接出带模型名的results文件名
    results_path = os.path.join(
        os.path.dirname(md_path), 
        f"results_{model}.json"
    )
    print("Start evaluating:", md_path)
    print("Using model:", model)

    # 定义每个部分必须存在的key
    outline_keys = ["Outline", "Outline_coverage", "Outline_structure"]
    content_keys = [
        "Coverage", "Structure", "Relevance", "Language", "Criticalness",
        "Images_density", "Equations_density", "Tables_density", "Total_density",
        "Claim_density_before_deduplication", "Claim_density_after_deduplication"
    ]
    # reference_keys = [...]

    # 先加载旧的结果
    if os.path.exists(results_path):
        try:
            with open(results_path, "r", encoding="utf-8") as f:
                results = json.load(f)
        except Exception as e:
            print("Error in loading existing results:", e)

    # Outline部分，只在关键key不全时才运行
    if do_outline:
        if not all(k in results for k in outline_keys):
            try:
                results.update(evaluate_outline(md_path))
            except Exception as e:
                print("Error in evaluating outline:", e)
        else:
            print("Outline already complete, skip.")
    else:
        print("Skip evaluating outline.")

    # Content部分，只在关键key不全时才运行
    if do_content:
        if not all(k in results for k in content_keys):
            try:
                results.update(evaluate_content(md_path))
            except Exception as e:
                print("Error in evaluating content:", e)
        else:
            print("Content already complete, skip.")
    else:
        print("Skip evaluating content.")

    # Reference部分同理...
    # if do_reference:
    #     if not all(k in results for k in reference_keys):
    #         try:
    #             results.update(evaluate_reference(md_path))
    #         except Exception as e:
    #             print("Error in evaluating reference:", e)
    #     else:
    #         print("Reference already complete, skip.")
    # else:
    #     print("Skip evaluating reference.")

    # 保存
    try:
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error in saving results:", e)
    return results

def process_system(md_path, model,results_path, topic, system, do_outline, do_content, do_reference):
    print(f"[{topic}/{system}] Evaluating: {md_path}")
    evaluate(md_path, 
             model=model,
             do_outline=do_outline, 
             do_content=do_content, 
             do_reference=do_reference)

def batch_evaluate_by_cat(cats:list, 
                  model:str,
                  do_outline=True, 
                  do_content=True, 
                  do_reference=True, 
                  num_workers=1):
    """
    批量处理 surveys/cat/<topic>/<system> 下所有md/pdf文件并评测
    支持并行处理，num_workers=1 为串行，>1 为多线程。
    """
    for cat in cats:
        base_dir = os.path.join("surveys", cat)
        topics = [d for d in os.listdir(base_dir) 
                if os.path.isdir(os.path.join(base_dir, d))]
        print(f"Found topics: {topics}")

        tasks = []

        for topic in topics:
            topic_path = os.path.join(base_dir, topic)
            systems = [d for d in os.listdir(topic_path)
                    if os.path.isdir(os.path.join(topic_path, d))]
            print(f"Topic: {topic} | Systems: {systems}")
            for system in systems:
                sys_path = os.path.join(topic_path, system)
                # 1. 查找md文件
                md_files = [f for f in os.listdir(sys_path) 
                            if f.lower().endswith(".md")]
                pdf_files = [f for f in os.listdir(sys_path) 
                            if f.lower().endswith(".pdf")]
                results_path = os.path.join(
                    sys_path, 
                    f"results_{model}.json"
                )
                # 2. 如果没有md，尝试用pdf生成
                if not md_files:
                    if pdf_files:
                        pdf_path = os.path.join(sys_path, pdf_files[0])
                        print(f"[{topic}/{system}] No md found, converting pdf: {pdf_path}")
                        md_path, _ = pdf2md(pdf_path, sys_path)
                        if not md_path:
                            print(f"[{topic}/{system}] PDF to md failed, skip.")
                            continue
                    else:
                        print(f"[{topic}/{system}] No md or pdf found, skip.")
                        continue
                else:
                    md_path = os.path.join(sys_path, md_files[0])

                tasks.append((md_path, model, results_path, topic, system, do_outline, do_content, do_reference))
        
        if num_workers == 1:
            # 串行执行
            for args in tasks:
                process_system(*args)
        else:
            # 多线程并发
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                future_to_system = {executor.submit(process_system, *args): args for args in tasks}
                for future in as_completed(future_to_system):
                    # 捕获异常防止线程池死掉
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Exception in thread: {e}")

def batch_evaluate_by_system(
    system_list: list,
    model: str,
    tasks_json_path: str = "surveys/tasks.json",
    do_outline: bool = True,
    do_content: bool = True,
    do_reference: bool = True,
    num_workers: int = 1
):
    """
    批量评测指定system列表的所有任务
    :param system_list: 需要评测的system名列表，如["InteractiveSurvey", "AutoSurvey"]
    :param tasks_json_path: task映射json路径
    :param do_outline: 是否评测outline
    :param do_content: 是否评测content
    :param do_reference: 是否评测reference
    :param num_workers: 并行数
    """
    # 读取 tasks.json
    with open(tasks_json_path, 'r', encoding='utf-8') as f:
        tasks = json.load(f)
    
    tasks_to_run = []
    for system in system_list:
        if system not in tasks:
            print(f"System {system} not found in {tasks_json_path}, skip.")
            continue
        for topic_map in tasks[system]:  # topic_map: {topic: path}
            for topic, rel_path in topic_map.items():
                sys_path = os.path.join("surveys", rel_path)
                # 寻找 md 或 pdf
                md_files = [f for f in os.listdir(sys_path) if f.lower().endswith(".md")]
                pdf_files = [f for f in os.listdir(sys_path) if f.lower().endswith(".pdf")]
                results_path = os.path.join(
                    sys_path, 
                    f"results_{model}.json"
                )
                if not md_files:
                    if pdf_files:
                        pdf_path = os.path.join(sys_path, pdf_files[0])
                        print(f"[{topic}/{system}] No md found, converting pdf: {pdf_path}")
                        md_path, _ = pdf2md(pdf_path, sys_path)
                        if not md_path:
                            print(f"[{topic}/{system}] PDF to md failed, skip.")
                            continue
                    else:
                        print(f"[{topic}/{system}] No md or pdf found, skip.")
                        continue
                else:
                    md_path = os.path.join(sys_path, md_files[0])
                tasks_to_run.append((md_path, model, results_path, topic, system, do_outline, do_content, do_reference))
    
    if num_workers == 1:
        for args in tasks_to_run:
            process_system(*args)
    else:
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_system = {executor.submit(process_system, *args): args for args in tasks_to_run}
            for future in as_completed(future_to_system):
                try:
                    future.result()
                except Exception as e:
                    print(f"Exception in thread: {e}")

def calculate_average_score(cat: str, system: str, model: str) -> dict:
    """
    计算指定类别、系统、模型的平均分
    :param cat: 类别名，如"cs"
    :param system: 系统名，如"InteractiveSurvey"
    :param model: 模型名，如"qwen-plus"
    :return: 平均分字典
    """
    base_dir = os.path.join("surveys", cat)
    topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    total_results = {}
    count = 0

    for topic in topics:
        topic_path = os.path.join(base_dir, topic)
        sys_path = os.path.join(topic_path, system)
        results_path = os.path.join(
            sys_path, 
            f"results_{model}.json"
        )
        if not os.path.exists(results_path):
            continue
        with open(results_path, "r", encoding="utf-8") as f:
            results = json.load(f)
        for key, value in results.items():
            if key not in total_results:
                total_results[key] = 0
            total_results[key] += value
        count += 1

    if count == 0:
        average_scores = {}
    else:
        average_scores = {key: round(value / count, 4) for key, value in total_results.items()}

    # 写入到 average_results.json
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    if os.path.exists(avg_results_path):
        with open(avg_results_path, "r", encoding="utf-8") as f:
            avg_results_data = json.load(f)
    else:
        avg_results_data = {}

    # 新的结构：系统名->模型名->均值
    if system not in avg_results_data:
        avg_results_data[system] = {}
    avg_results_data[system][model] = average_scores

    with open(avg_results_path, "w", encoding="utf-8") as f:
        json.dump(avg_results_data, f, ensure_ascii=False, indent=4)

    return average_scores

def clear_scores(cat: str, system: str, model: str):
    """
    清除指定类别、系统、模型的所有评测结果
    :param cat: 类别名，如"cs"
    :param system: 系统名，如"InteractiveSurvey"
    :param model: 模型名，如"qwen-plus"
    """
    base_dir = os.path.join("surveys", cat)
    topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for topic in topics:
        topic_path = os.path.join(base_dir, topic)
        sys_path = os.path.join(topic_path, system)
        results_path = os.path.join(
            sys_path, 
            f"results_{model}.json"
        )
        if os.path.exists(results_path):
            os.remove(results_path)
    
    # 清理 average_results.json 里的对应系统和模型
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    if os.path.exists(avg_results_path):
        with open(avg_results_path, "r", encoding="utf-8") as f:
            avg_results_data = json.load(f)
        if system in avg_results_data:
            if model in avg_results_data[system]:
                del avg_results_data[system][model]
                # 如果该系统下已经没有模型了，把系统也删掉
                if not avg_results_data[system]:
                    del avg_results_data[system]
        with open(avg_results_path, "w", encoding="utf-8") as f:
            json.dump(avg_results_data, f, ensure_ascii=False, indent=4)

def clear_all_scores():
    """
    清除所有评测结果（所有以results_开头、.json结尾的结果文件）
    """
    base_dir = "surveys"
    for cat in os.listdir(base_dir):
        cat_path = os.path.join(base_dir, cat)
        if os.path.isdir(cat_path):
            for topic in os.listdir(cat_path):
                topic_path = os.path.join(cat_path, topic)
                if os.path.isdir(topic_path):
                    for system in os.listdir(topic_path):
                        sys_path = os.path.join(topic_path, system)
                        if os.path.isdir(sys_path):
                            # 匹配所有 results_*.json 文件
                            pattern = os.path.join(sys_path, "results_*.json")
                            for file_path in glob.glob(pattern):
                                try:
                                    os.remove(file_path)
                                    print(f"Removed: {file_path}")
                                except Exception as e:
                                    print(f"Failed to remove {file_path}: {e}")


if __name__ == "__main__":
    # 测试代码
    # md_path = "surveys\cs\Optimization Techniques for Transformer Inference\pdfs/2307.07982.md"  # 替换为实际的文件路径
    # md_path = "surveys\cs\Agent-based Modeling and Simulation using Large Language Models\AutoSurvey\Agent-based Modeling and Simulation using Large Language Models.md"
    # json_path = os.path.join(os.path.dirname(md_path), "outline.json")
    # evaluate_outline(md_path)
    # evaluate_content_informativeness(md_path)
    # evaluate_content(md_path)
    # evaluate_reference(md_path)
    # print(evaluate_outline_coverage(json_path))
    # batch_evaluate_by_cat(["cs"])
    # calculate_average_score("cs", "AutoSurvey", "qwen-plus-2025-04-28")
    # clear_scores("cs", "AutoSurvey")
    # batch_evaluate_by_system(["vanilla"], "qwen-plus-2025-04-28", num_workers=4)
    # clear_all_scores()
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/vanilla_outline/3D Gaussian Splatting Techniques.md")
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/vanilla/3D Gaussian Splatting Techniques.md")
    # print(evaluate_outline_coverage("surveys/cs/3D Gaussian Splatting Techniques/vanilla/outline.json"))
    evaluate_reference("surveys/cs/3D Gaussian Splatting/pdfs/2401.03890.md")


