from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import math
import os
import dotenv
from prompts import CONTENT_EVALUATION_PROMPT, OUTLINE_EVALUATION_PROMPT, CRITERIA, OUTLINE_STRUCTURE_PROMPT, REFERENCE_EVALUATION_PROMPT, OUTLINE_COVERAGE_PROMPT
from utils import build_outline_tree_from_levels, count_md_features, extract_and_save_outline_from_md, extract_references_from_md, extract_topic_from_path, getClient, generateResponse, pdf2md, robust_json_parse,fill_single_criterion_prompt, read_md
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

def evaluate_outline_coverage(
    outline_json_path: str,
    standard_count: int = 10,
    ideal_section_count: int = 30,
    sigma: float = 15.0
) -> float:
    """
    评估大纲综合得分 Q'，融合模板完整度、创新丰富度和长度惩罚。

    Args:
        outline_json_path (str): 大纲JSON路径
        standard_count (int): 标准section总数 N
        ideal_section_count (int): 理想section总数 M*
        sigma (float): 惩罚宽度参数

    Returns:
        float: 综合得分 Q'
    """
    try:
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)

        total_section_count = len(outline_list)  # M

        outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])
        topic = extract_topic_from_path(outline_json_path)
        prompt = OUTLINE_COVERAGE_PROMPT.format(
            outline=outline_str,
            topic=topic,
        )
        response = judge.judge(prompt)
        matched_count = response.get("matched_count", 0)   # K

        K = matched_count
        N = standard_count
        M = total_section_count
        M_star = ideal_section_count
        U = max(M - K, 0)

        R = K / N if N > 0 else 0
        O = U / M if M > 0 else 0

        F_harmonic = 2 * R * O / (R + O) if (R + O) > 0 else 0

        L = math.exp(-((M - M_star) ** 2) / (2 * sigma ** 2)) if sigma > 0 else (1.0 if M == M_star else 0.0)

        Q_prime = F_harmonic * L

        return Q_prime

    except Exception as e:
        print("Error in evaluating outline coverage:", e)
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

    try:
        # 1. Extract outline from md
        extract_and_save_outline_from_md(md_path)
    except Exception as e:
        print("Error extracting outline:", e)
        return results

    outline_json_path = os.path.join(os.path.dirname(md_path), "outline.json")

    # 2. LLM 评测
    if do_llm:
        try:
            outline_results = evaluate_outline_llm(outline_json_path)
            results.update(outline_results)
        except Exception as e:
            print("Error in evaluating outline llm:", e)
            results["Outline"] = 0
    else:
        print("Skip evaluate_outline_llm.")

    # 3. Coverage 评测
    if do_coverage:
        try:
            coverage_results = evaluate_outline_coverage(outline_json_path)
            results["Outline_coverage"] = coverage_results
        except Exception as e:
            print("Error in evaluating outline coverage:", e)
            results["Outline_coverage"] = 0
    else:
        print("Skip evaluate_outline_coverage.")

    # 4. Structure 评测
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
    # if do_faithfulness:
    #     try:
    #         results.update(evaluate_content_faithfulness(md_path))
    #     except Exception as e:
    #         print("Error in evaluating content faithfulness:", e)
    #         results['faithfulness'] = 0
    # else:
    #     print("Skip evaluate_content_faithfulness.")

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

def evaluate(
    md_path: str, 
    do_outline: bool = True, 
    do_content: bool = True, 
    do_reference: bool = True
) -> dict:
    """
    Evaluate the given Markdown file by selected criteria.
    """
    import os
    import json

    results = {}
    results_path = os.path.join(os.path.dirname(md_path), "results.json")
    print("Start evaluating:", md_path)

    # 定义每个部分必须存在的key
    outline_keys = ["Outline", "Outline_coverage", "Outline_structure"]
    content_keys = [
        "Coverage", "Structure", "Relevance", "Language", "Criticalness",
        "Images_density", "Equations_density", "Tables_density", "Total_density",
        "Claim_density_with_deduplication", "Claim_density_after_deduplication"
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

def process_system(md_path, results_path, topic, system, do_outline, do_content, do_reference):
    print(f"[{topic}/{system}] Evaluating: {md_path}")
    evaluate(md_path, 
             do_outline=do_outline, 
             do_content=do_content, 
             do_reference=do_reference)

def batch_evaluate_by_cat(cats:list, 
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
                results_path = os.path.join(sys_path, "results.json")
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

                tasks.append((md_path, results_path, topic, system, do_outline, do_content, do_reference))
        
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
                results_path = os.path.join(sys_path, "results.json")
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
                tasks_to_run.append((md_path, results_path, topic, system, do_outline, do_content, do_reference))
    
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


if __name__ == "__main__":
    # 测试代码
    #md_path = "surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md"  # 替换为实际的文件路径
    # md_path = "surveys\cs\Agent-based Modeling and Simulation using Large Language Models\AutoSurvey\Agent-based Modeling and Simulation using Large Language Models.md"
    # json_path = os.path.join(os.path.dirname(md_path), "outline.json")
    # evaluate_outline(md_path)
    # evaluate_content_informativeness(md_path)
    # evaluate_content(md_path)
    # evaluate_reference(md_path)
    # print(evaluate_outline_coverage(json_path))
    # evaluate(md_path)
    batch_evaluate_by_cat(["cs"])



