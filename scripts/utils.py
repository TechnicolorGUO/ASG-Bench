import ast
import json
import os
import re
import shlex
import shutil
import subprocess
from openai import OpenAI

from dotenv import load_dotenv
import requests

from prompts import OUTLINE_REFINE_PROMPT
load_dotenv()

def getClient(): 
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    openai_api_base = os.environ.get("OPENAI_API_BASE")

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )
    return client

def generateResponse(client, prompt, max_tokens=768, temperature=0.5):
    chat_response = client.chat.completions.create(
        model=os.environ.get("MODEL"),
        max_tokens=max_tokens,
        temperature=temperature,
        stop="<|im_end|>",
        stream=True,
        messages=[{"role": "user", "content": prompt}]
    )

    text = ""
    for chunk in chat_response:
        if chunk.choices[0].delta.content:
            text += chunk.choices[0].delta.content
    return text

def robust_json_parse(raw_response):
    """
    Try to parse a JSON object from raw_response.
    If failed, try to extract the first {...} block and parse again.
    If still failed, return an empty dict and print a warning.
    """
    try:
        return json.loads(raw_response)
    except Exception:
        match = re.search(r'(\{.*\})', raw_response, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except Exception:
                pass
        # If all parsing fails, return empty dict and print warning
        print("Warning: Failed to parse LLM response as JSON, returning empty dict.\nRaw response:", raw_response)
        return {}

def robust_list_parse(response_str):
    """
    Robustly parse a string to a Python list. 
    Tries JSON, then Python literal. Raises on failure.
    """
    # 尝试截断前后的无关内容（只保留第一个以 [ 开头、] 结尾的内容）
    def extract_most_likely_list(text):
        start = text.find('[')
        end = text.rfind(']')
        if start != -1 and end != -1 and end > start:
            return text[start:end+1]
        return text

    cleaned = response_str.strip()
    cleaned = extract_most_likely_list(cleaned)

    # 1. 尝试 json.loads
    try:
        result = json.loads(cleaned)
        if isinstance(result, list):
            return result
    except Exception:
        pass

    # 2. 尝试 ast.literal_eval
    try:
        result = ast.literal_eval(cleaned)
        if isinstance(result, list):
            return result
    except Exception:
        pass

    # 3. 最后失败就抛出异常
    raise ValueError("Could not parse response as a list.")

def download_arxiv_pdf(arxiv_id: str, save_dir: str) -> str:
    """
    下载 arXiv 论文 PDF 到指定目录
    :param arxiv_id: arXiv 主ID（如 '2301.00001'）
    :param save_dir: 目标文件夹路径（如 './pdfs'）
    :return: 保存后的PDF文件路径
    :raises: Exception 如果下载失败
    """
    # 构造PDF下载URL
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    # 确保文件夹存在
    os.makedirs(save_dir, exist_ok=True)
    # 文件名
    file_path = os.path.join(save_dir, f"{arxiv_id}.pdf")

    # 如果已经存在，则跳过下载
    if os.path.exists(file_path):
        print(f"PDF already exists: {file_path}")
        return file_path

    print(f"Downloading {pdf_url} ...")
    try:
        resp = requests.get(pdf_url, stream=True, timeout=20)
        resp.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Saved: {file_path}")
        return file_path
    except Exception as e:
        # 如果下载失败，尝试删除未完成的文件
        if os.path.exists(file_path):
            os.remove(file_path)
        print(f"Failed to download {arxiv_id}: {e}")
        raise

def extract_and_save_outline_from_md(md_file_path):
    """
    只处理#开头的标题。
    - 如果有多层井号，按井号数量决定层级；
    - 如果只有一层井号，全部视为一级。
    """
    if not os.path.isfile(md_file_path):
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")

    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern_hash = r'^(#{1,6})\s+(.+)'
    hash_headers = []
    for i, line in enumerate(lines):
        match = re.match(pattern_hash, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            hash_headers.append((i, level, title))

    # 判断是否只有一个井号层级
    levels = {lvl for _, lvl, _ in hash_headers}
    single_level = (len(levels) == 1 and hash_headers)

    outline = []
    if single_level:
        # 全部视为一级
        for _, _, title in hash_headers:
            outline.append([1, title])
    else:
        # 按井号层级
        for _, level, title in hash_headers:
            outline.append([level, title])

    json_path = os.path.join(os.path.dirname(md_file_path), "outline_raw.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)
    return outline

def refine_outline_if_single_level(
    raw_outline_path: str,
    json_path: str,
):
    """
    If the outline is all level-1, call LLM to refine and parse as a list, then save.
    Otherwise, save as is.
    """
    client = getClient()
    with open(raw_outline_path, "r", encoding="utf-8") as f:
        outline = json.load(f)

    # Check if all headings are level 1
    levels = {item[0] for item in outline}
    if len(levels) == 1 and list(levels)[0] == 1:
        outline_str = json.dumps(outline, ensure_ascii=False, indent=2)
        prompt = OUTLINE_REFINE_PROMPT.format(outline=outline_str)
        raw_response = generateResponse(client, prompt, max_tokens=768, temperature=0.5)
        refined_outline = robust_list_parse(raw_response)   # Use list parse here!
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(refined_outline, f, ensure_ascii=False, indent=2)
        return refined_outline
    else:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(outline, f, ensure_ascii=False, indent=2)
        return outline

def extract_references_from_md(md_path):
    """
    Extract the References section from a Markdown file.
    Returns reference list as a string (one per line), or empty string if not found.
    """
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Match ## References 或 # Reference 及类似写法，允许多余空格或其他大小写
    pattern = re.compile(
        r'^(#{1,6})\s*(References?|Bibliography|参考文献)[\s#]*\n+([\s\S]*?)(?=^#{1,6}\s|\Z)', 
        re.IGNORECASE | re.MULTILINE
    )
    match = pattern.search(text)
    if match:
        references_block = match.group(3).strip()
        # 按行分割，去掉空行
        references = [line for line in references_block.splitlines() if line.strip()]
        return references
    else:
        return []

def fill_single_criterion_prompt(
    prompt_template: str,
    content: str,
    topic: str,
    criterion: dict,
    criteria_name: str,
    type: str
) -> str:
    """
    自动填充评价 prompt，支持 survey/outline，支持输出 json 格式
    :param prompt_template: prompt模板
    :param content: 需要评价的内容
    :param topic: 主题
    :param criterion: 评价标准
    :param criteria_name: 该 criterion 的名称
    :param content_key: 模板内容字段名
    :return: prompt字符串
    """
    format_args = {
        "topic": topic,
        "criterion_description": criterion['description'],
        "score_1": criterion['score 1'],
        "score_2": criterion['score 2'],
        "score_3": criterion['score 3'],
        "score_4": criterion['score 4'],
        "score_5": criterion['score 5'],
        "criteria_name": criteria_name,
        type: content
    }
    return prompt_template.format(**format_args)

def extract_topic_from_path(md_path: str) -> str:
    # 先绝对路径化，防止不同系统分隔符问题
    abs_path = os.path.abspath(md_path)
    # 获取上上级目录名
    topic = os.path.basename(os.path.dirname(os.path.dirname(abs_path)))
    return topic

def build_outline_tree_from_levels(outline_list):
    """
    将 [level, title] 格式的大纲解析为树结构。
    
    Args:
        outline_list: List of [level, title]，层数从1开始，顺序排列。

    Returns:
        node_objs: 所有节点字典（含children, parent, index）
        top_nodes: 顶层节点列表
    """
    node_objs = []
    for idx, (level, title) in enumerate(outline_list):
        node = {
            "level": level,
            "title": title,
            "index": idx,           # 唯一编号，用顺序号
            "children": [],
            "parent": None
        }
        node_objs.append(node)

    stack = []
    for node in node_objs:
        while stack and stack[-1]["level"] >= node["level"]:
            stack.pop()
        if stack:
            node["parent"] = stack[-1]["index"]
            stack[-1]["children"].append(node)
        stack.append(node)

    top_nodes = [node for node in node_objs if node["parent"] is None]
    return node_objs, top_nodes

def pdf2md(pdf_path, output_dir):
    """
    调用 magic-pdf 将 PDF 转换为 markdown，并将生成的md移动到output_dir根目录。
    移动完成后，删除 output_dir/pdf_stem 文件夹（即 'auto' 上层目录）。
    :param output_dir: 输出目录
    :param pdf_path: PDF 文件路径，可选
    :return: (md_new_path, md_content)
    """
    # 构造命令
    cmd = ["magic-pdf"]
    if pdf_path:
        cmd += ["-p", pdf_path]
    cmd += ["-o", output_dir]

    try:
        print("Running command:", " ".join(shlex.quote(str(x)) for x in cmd))
        subprocess.run(cmd, check=True)
        print("Conversion finished!")
    except subprocess.CalledProcessError as e:
        print("Error running magic-pdf:", e)
        return None, None

    pdf_filename = os.path.basename(pdf_path)
    pdf_stem = pdf_filename.replace(".pdf", "")
    md_orig_path = os.path.join(output_dir, pdf_stem, "auto", pdf_stem + ".md")
    md_new_path = os.path.join(output_dir, pdf_stem + ".md")
    pdf_stem_dir = os.path.join(output_dir, pdf_stem)

    # 读取内容并移动
    if not os.path.exists(md_orig_path):
        print(f"Cannot find md file at {md_orig_path}")
        return None, None

    shutil.move(md_orig_path, md_new_path)

    # 删除整个 output_dir/pdf_stem 文件夹
    try:
        shutil.rmtree(pdf_stem_dir)
        print(f"Removed intermediate directory: {pdf_stem_dir}")
    except Exception as e:
        print(f"Failed to remove intermediate directory {pdf_stem_dir}: {e}")

    with open(md_new_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    return md_new_path, md_content

def batch_pdf2md_in_surveys(surveys_root = "surveys"):
    """
    对 surveys/<cat>/<topic>/<system> 下所有 pdf 文件批量转换为 md。
    如果已存在对应 md 文件则跳过。
    :param surveys_root: surveys 根目录
    """
    total_pdf = 0
    converted = 0
    skipped = 0
    failed = 0

    for cat in os.listdir(surveys_root):
        cat_path = os.path.join(surveys_root, cat)
        if not os.path.isdir(cat_path):
            continue
        for topic in os.listdir(cat_path):
            topic_path = os.path.join(cat_path, topic)
            if not os.path.isdir(topic_path):
                continue
            for system in os.listdir(topic_path):
                system_path = os.path.join(topic_path, system)
                if not os.path.isdir(system_path):
                    continue
                for file in os.listdir(system_path):
                    if file.lower().endswith(".pdf"):
                        total_pdf += 1
                        pdf_path = os.path.join(system_path, file)
                        md_name = os.path.splitext(file)[0] + ".md"
                        md_path = os.path.join(system_path, md_name)
                        if os.path.exists(md_path):
                            print(f"Skip (md exists): {md_path}")
                            skipped += 1
                            continue
                        # 调用pdf2md
                        print(f"Converting: {pdf_path}")
                        md_new_path, md_content = pdf2md(pdf_path, system_path)
                        if md_new_path:
                            print(f"Converted: {md_new_path}")
                            converted += 1
                        else:
                            print(f"Failed: {pdf_path}")
                            failed += 1

    print("\nBatch Summary:")
    print(f"Total PDF files: {total_pdf}")
    print(f"Converted: {converted}")
    print(f"Skipped (md exists): {skipped}")
    print(f"Failed: {failed}")

def count_sentences(text):
    sentences = re.split(r"[.!?\n]+(?:\s|\n|$)", text.strip())
    sentences = [s for s in sentences if s]
    return len(sentences)

def count_md_features(md_content):
    """
    统计md_content中的图片数、公式数、表格数
    :param md_content: str, markdown文本
    :return: dict, {'images': int, 'equations': int, 'tables': int}
    """
    # 图片：![](...) 或 <img ...> 或 html <img>
    img_md = re.findall(r'!\[.*?\]\(.*?\)', md_content)
    img_html = re.findall(r'<img [^>]*src=[\'"].*?[\'"][^>]*>', md_content, re.IGNORECASE)
    # 常见图片也可能是 <img ... />
    img_html2 = re.findall(r'<img [^>]*>', md_content, re.IGNORECASE)
    image_count = len(img_md) + len(img_html)
    # 避免重复计数
    image_count = len(set(img_md + img_html + img_html2))

    # 公式：行内 $...$，块公式 $$...$$，以及 \[...\] 和 \begin{}...\end{}
    # 块公式
    block_eq = re.findall(r'\$\$.*?\$\$', md_content, re.DOTALL)
    block_eq += re.findall(r'\\\[.*?\\\]', md_content, re.DOTALL)
    block_eq += re.findall(r'\\begin\{.*?\}.*?\\end\{.*?\}', md_content, re.DOTALL)
    # 行内 $...$，排除 $$...$$ 的情况
    # 这里匹配$...$但不是$$...$$
    inline_eq = re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', md_content)
    equation_count = len(block_eq) + len(inline_eq)

    # 表格：Markdown表格（至少有一行|---|），或html <table>
    md_tables = re.findall(
        r'(?:\|[^\n]*\n)+\|[\s\-:|]+\|(?:\n\|[^\n]*)*', md_content)
    html_tables = re.findall(r'<table[\s\S]*?</table>', md_content, re.IGNORECASE)
    table_count = len(md_tables) + len(html_tables)

    # 总句子数
    sentence_count = count_sentences(md_content)
    return {
        'images': image_count,
        'equations': equation_count,
        'tables': table_count,
        'sentences': sentence_count
    }

def read_md(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        return f.read()

def get_deduplication_prompt(facts_list: list) -> str:

    """
    生成用于对 facts 列表去重的 Prompt。要求输出需要删除的序号（逗号分隔）。
    """
    numbered_facts = "\n".join([f"{i+1}. {fact}" for i, fact in enumerate(facts_list)])
    return f"""Below is a numbered list of claims. Your task is to identify and group 
    claims that convey the same information, removing all redundancy.

    [Guidelines]:
    - Claims that express the same fact or knowledge in different wording or detail are duplicates.
    - If one claim is fully included within another or repeats the same idea, consider it a duplicate.
    - Claims with differing details, context, or scope are not duplicates.

    For each group of duplicates, output the serial numbers of the claims to be removed (comma-separated). 
    Choose one claim to keep.

    Example:
    If claims 2, 5, and 8 are duplicates and claim 2 is kept, output "5,8".

    List of claims:
    {numbered_facts}

    Output ONLY the serial numbers to remove. No additional text.
    """

def get_extraction_prompt(text: str) -> str:
    """
    Generate optimized prompt for claim extraction (v2)
    """
    return f"""Analyze the following text and decompose it into independent claims following strict consolidation rules:

    [Claim Definition]
    A verifiable objective factual statement that functions as an independent knowledge unit. Each claim must:
    1. Contain complete subject-predicate-object structure
    2. Exist independently without contextual dependency
    3. Exclude subjective evaluations

    [Merge Rules]→ Should merge when:
    - Same subject + same predicate + different objects (e.g., "Should measure A / Should measure B" → "Should measure A and B")
    - Different expressions of the same research conclusion
    - Parallel elements of the same category (e.g., "A, B and C")

    [Separation Rules]→ Should keep separate when:
    - Different research subjects/objects
    - Claims with causal/conditional relationships
    - Findings across temporal sequences
    - Conclusions using different verification methods

    [Output Format]
    Strict numbered list with consolidated claims maintaining grammatical integrity:
    1. Use "and/or/including" for merged items
    2. Separate parallel elements with commas
    3. Prohibit abbreviations or contextual references

    Below is the text you need to extract claims from:

    {text}
    """



if __name__ == "__main__":
    # # 测试提取大纲
    # md_file_path = "surveys/cs/Optimization Techniques for Transformer Inference/pdfs/2307.07982.md"
    # outline = extract_and_save_outline_from_md(md_file_path)
    # print(len(outline))
    # for item in outline:
    #     print(item)
    # # 打印大纲
    # print("Outline:")
    # tree, top_nodes = build_outline_tree_from_levels(outline)
    # print(len(tree))

    # md_path, md_content = pdf2md("surveys/cs/3D Gaussian Splatting Techniques/LLMxMapReduce/5_1_2025, 6_14_21 PM_3D Gaussian Splatting Techniques.pdf", "surveys/cs/3D Gaussian Splatting Techniques/LLMxMapReduce")
    # md_content = read_md("surveys/cs/3D Gaussian Splatting Techniques/LLMxMapReduce/5_1_2025, 6_14_21 PM_3D Gaussian Splatting Techniques/auto/5_1_2025, 6_14_21 PM_3D Gaussian Splatting Techniques.md")
    # print(count_md_features(md_content))
    # refine_outline_if_single_level("surveys\cs\Optimization Techniques for Transformer Inference\pdfs\outline_raw.json", "surveys\cs\Optimization Techniques for Transformer Inference\pdfs\outline.json")
    batch_pdf2md_in_surveys()