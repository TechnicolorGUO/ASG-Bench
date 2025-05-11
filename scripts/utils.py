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
from reference import split_markdown_content_and_refs
load_dotenv()

# --------------OpenAI/LLM Related Functions-------------

def getClient() -> OpenAI: 
    """
    Initialize and return an OpenAI client using environment variables.
    
    Returns:
        OpenAI: Configured OpenAI client instance
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    openai_api_base = os.environ.get("OPENAI_API_BASE")

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )
    return client

def generateResponse(client: OpenAI, prompt: str, max_tokens: int = 4096, temperature: float = 0.5) -> str:
    """
    Generate a response from the OpenAI model using streaming.
    
    Args:
        client (OpenAI): OpenAI client instance
        prompt (str): Input prompt for the model
        max_tokens (int, optional): Maximum tokens in response. Defaults to 4096.
        temperature (float, optional): Response randomness. Defaults to 0.5.
    
    Returns:
        str: Generated response text
    """
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

def get_deduplication_prompt(facts_list: list[str]) -> str:
    """
    Generate a prompt for deduplicating a list of facts.
    
    Args:
        facts_list (list[str]): List of facts to be deduplicated
        
    Returns:
        str: Formatted prompt for deduplication
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
    Generate an optimized prompt for claim extraction.
    
    Args:
        text (str): Input text to extract claims from
        
    Returns:
        str: Formatted prompt for claim extraction
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

def robust_json_parse(raw_response: str) -> dict:
    """
    Attempt to parse a JSON object from raw response text.
    If failed, try to extract the first {...} block and parse again.
    If still failed, return an empty dict and print a warning.
    
    Args:
        raw_response (str): Raw response text to parse
        
    Returns:
        dict: Parsed JSON object or empty dict if parsing fails
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
        print("Warning: Failed to parse LLM response as JSON, returning empty dict.\nRaw response:", raw_response)
        return {}

def robust_list_parse(response_str: str) -> list:
    """
    Robustly parse a string to a Python list.
    Tries JSON parsing first, then Python literal evaluation.
    
    Args:
        response_str (str): String to parse as a list
        
    Returns:
        list: Parsed list
        
    Raises:
        ValueError: If parsing fails
    """
    def extract_most_likely_list(text: str) -> str:
        start = text.find('[')
        end = text.rfind(']')
        if start != -1 and end != -1 and end > start:
            return text[start:end+1]
        return text

    cleaned = response_str.strip()
    cleaned = extract_most_likely_list(cleaned)

    try:
        result = json.loads(cleaned)
        if isinstance(result, list):
            return result
    except Exception:
        pass

    try:
        result = ast.literal_eval(cleaned)
        if isinstance(result, list):
            return result
    except Exception:
        pass

    raise ValueError("Could not parse response as a list.")

# --------------File I/O and Content Processing-------------

def read_md(md_path: str) -> str:
    """
    Read and return the contents of a markdown file.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        str: Contents of the markdown file
    """
    with open(md_path, "r", encoding="utf-8") as f:
        return f.read()

def count_md_files(surveys_root: str = "surveys") -> dict[str, int]:
    """
    Count the number of markdown files in the surveys directory for each system.
    
    Args:
        surveys_root (str, optional): Root directory of surveys. Defaults to "surveys".
        
    Returns:
        dict[str, int]: Dictionary mapping system names to their markdown file counts
    """
    sys_dict: dict[str, int] = {}
    for cat in os.listdir(surveys_root):
        cat_path = os.path.join(surveys_root, cat)
        if not os.path.isdir(cat_path):
            continue
        for topic in os.listdir(cat_path):
            topic_path = os.path.join(cat_path, topic)
            if not os.path.isdir(topic_path):
                continue
            for system in os.listdir(topic_path):
                md_files = os.listdir(os.path.join(topic_path, system))
                for file in md_files:
                    if file.lower().endswith(".md"):
                        sys_dict[system] = sys_dict.get(system, 0) + 1
    for system, count in sys_dict.items():
        print(f"{system}: {count}")
    return sys_dict

# --------------PDF Processing-------------

def download_arxiv_pdf(arxiv_id: str, save_dir: str) -> str:
    """
    Download an arXiv paper PDF to the specified directory.
    
    Args:
        arxiv_id (str): arXiv paper ID (e.g., '2301.00001')
        save_dir (str): Target directory path (e.g., './pdfs')
        
    Returns:
        str: Path to the saved PDF file
        
    Raises:
        Exception: If download fails
    """
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{arxiv_id}.pdf")

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
        if os.path.exists(file_path):
            os.remove(file_path)
        print(f"Failed to download {arxiv_id}: {e}")
        raise

def pdf2md(pdf_path: str, output_dir: str) -> tuple[str | None, str | None]:
    """
    Convert a PDF file to markdown using magic-pdf.
    Moves the generated markdown to the output directory root.
    Removes the intermediate directory after conversion.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Output directory path
        
    Returns:
        tuple[str | None, str | None]: (path to new markdown file, markdown content) or (None, None) if conversion fails
    """
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

    if not os.path.exists(md_orig_path):
        print(f"Cannot find md file at {md_orig_path}")
        return None, None

    shutil.move(md_orig_path, md_new_path)

    try:
        shutil.rmtree(pdf_stem_dir)
        print(f"Removed intermediate directory: {pdf_stem_dir}")
    except Exception as e:
        print(f"Failed to remove intermediate directory {pdf_stem_dir}: {e}")

    with open(md_new_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    return md_new_path, md_content

def batch_pdf2md_in_surveys(surveys_root: str = "surveys") -> None:
    """
    Batch convert all PDF files in surveys/<cat>/<topic>/<system> to markdown.
    Skips conversion if corresponding markdown file already exists.
    
    Args:
        surveys_root (str, optional): Root directory of surveys. Defaults to "surveys".
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

# --------------Markdown Processing-------------

def extract_and_save_outline_from_md(md_file_path: str) -> list[list[int | str]]:
    """
    Extract and save outline from markdown file.
    Processes headers starting with #.
    - If multiple # levels exist, uses # count as level
    - If only one # level exists, treats all as level 1
    
    Args:
        md_file_path (str): Path to markdown file
        
    Returns:
        list[list[int | str]]: List of [level, title] pairs
        
    Raises:
        FileNotFoundError: If markdown file not found
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

    levels = {lvl for _, lvl, _ in hash_headers}
    single_level = (len(levels) == 1 and hash_headers)

    outline = []
    if single_level:
        for _, _, title in hash_headers:
            outline.append([1, title])
    else:
        for _, level, title in hash_headers:
            outline.append([level, title])

    json_path = os.path.join(os.path.dirname(md_file_path), "outline_raw.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)
    return outline

def refine_outline_if_single_level(raw_outline_path: str, json_path: str) -> list:
    """
    Refine outline if all headings are level 1.
    Uses LLM to refine and parse as a list, then saves.
    Otherwise, saves as is.
    
    Args:
        raw_outline_path (str): Path to raw outline JSON file
        json_path (str): Path to save refined outline
        
    Returns:
        list: Refined outline
    """
    client = getClient()
    with open(raw_outline_path, "r", encoding="utf-8") as f:
        outline = json.load(f)

    levels = {item[0] for item in outline}
    if len(levels) == 1 and list(levels)[0] == 1:
        outline_str = json.dumps(outline, ensure_ascii=False, indent=2)
        prompt = OUTLINE_REFINE_PROMPT.format(outline=outline_str)
        raw_response = generateResponse(client, prompt, max_tokens=4096, temperature=0.5)
        refined_outline = robust_list_parse(raw_response)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(refined_outline, f, ensure_ascii=False, indent=2)
        return refined_outline
    else:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(outline, f, ensure_ascii=False, indent=2)
        return outline

def extract_references_from_md(md_path: str) -> list[str]:
    """
    Read and return reference entries from references.json in the same directory as md_path.
    
    Args:
        md_path (str): Path to markdown file
        
    Returns:
        list[str]: List of reference entries, empty list if file not found or invalid
    """
    dir_path = os.path.dirname(md_path)
    json_path = os.path.join(dir_path, "references.json")
    if not os.path.isfile(json_path):
        return []
    with open(json_path, "r", encoding="utf-8") as f:
        try:
            refs = json.load(f)
            refs = [ref.strip() for ref in refs if ref.strip()]
            return refs
        except Exception:
            return []

def build_outline_tree_from_levels(outline_list: list[list[int | str]]) -> tuple[list[dict], list[dict]]:
    """
    Parse [level, title] format outline into a tree structure.
    
    Args:
        outline_list (list[list[int | str]]): List of [level, title] pairs, levels start from 1
        
    Returns:
        tuple[list[dict], list[dict]]: (all node dictionaries with children/parent/index, top-level nodes)
    """
    node_objs = []
    for idx, (level, title) in enumerate(outline_list):
        node = {
            "level": level,
            "title": title,
            "index": idx,
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

# --------------Text Analysis and Statistics-------------

def count_sentences(text: str) -> int:
    """
    Count the number of sentences in text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of sentences
    """
    sentences = re.split(r"[.!?\n]+(?:\s|\n|$)", text.strip())
    sentences = [s for s in sentences if s]
    return len(sentences)

def count_md_features(md_content: str) -> dict[str, int]:
    """
    Count images, equations, tables, and sentences in markdown content.
    
    Args:
        md_content (str): Markdown text
        
    Returns:
        dict[str, int]: Counts of {'images': int, 'equations': int, 'tables': int, 'sentences': int}
    """
    img_md = re.findall(r'!\[.*?\]\(.*?\)', md_content)
    img_html = re.findall(r'<img [^>]*src=[\'"].*?[\'"][^>]*>', md_content, re.IGNORECASE)
    img_html2 = re.findall(r'<img [^>]*>', md_content, re.IGNORECASE)
    image_count = len(set(img_md + img_html + img_html2))

    block_eq = re.findall(r'\$\$.*?\$\$', md_content, re.DOTALL)
    block_eq += re.findall(r'\\\[.*?\\\]', md_content, re.DOTALL)
    block_eq += re.findall(r'\\begin\{.*?\}.*?\\end\{.*?\}', md_content, re.DOTALL)
    inline_eq = re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', md_content)
    equation_count = len(block_eq) + len(inline_eq)

    md_tables = re.findall(
        r'(?:\|[^\n]*\n)+\|[\s\-:|]+\|(?:\n\|[^\n]*)*', md_content)
    html_tables = re.findall(r'<table[\s\S]*?</table>', md_content, re.IGNORECASE)
    table_count = len(md_tables) + len(html_tables)

    main_content, _ = split_markdown_content_and_refs(md_content)
    sentence_count = count_sentences(main_content)
    return {
        'images': image_count,
        'equations': equation_count,
        'tables': table_count,
        'sentences': sentence_count
    }

# --------------Utility Functions-------------

def extract_topic_from_path(md_path: str) -> str:
    """
    Extract topic name from markdown file path.
    
    Args:
        md_path (str): Path to markdown file
        
    Returns:
        str: Topic name
    """
    abs_path = os.path.abspath(md_path)
    topic = os.path.basename(os.path.dirname(os.path.dirname(abs_path)))
    return topic

def fill_single_criterion_prompt(
    prompt_template: str,
    content: str,
    topic: str,
    criterion: dict[str, str],
    criteria_name: str,
    type: str
) -> str:
    """
    Fill a single criterion evaluation prompt template.
    
    Args:
        prompt_template (str): Prompt template string
        content (str): Content to be evaluated
        topic (str): Topic name
        criterion (dict[str, str]): Criterion dictionary with description and scores
        criteria_name (str): Name of the criterion
        type (str): Type of content being evaluated
        
    Returns:
        str: Filled prompt string
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
    # md_content = read_md("surveys\cs\Large Language Model Based Multi-Agent Systems\pdfs/2402.01680.md")
    # print(count_md_features(md_content))
    # refine_outline_if_single_level("surveys\cs\Optimization Techniques for Transformer Inference\pdfs\outline_raw.json", "surveys\cs\Optimization Techniques for Transformer Inference\pdfs\outline.json")
    # batch_pdf2md_in_surveys()
    count_md_files()