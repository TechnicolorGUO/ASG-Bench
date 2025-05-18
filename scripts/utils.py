import ast
import json
import os
import re
import shlex
import shutil
import subprocess
import logging
from datetime import datetime
from openai import OpenAI

from dotenv import load_dotenv
import requests

from prompts import OUTLINE_REFINE_PROMPT
from reference import extract_refs, split_markdown_content_and_refs, parse_markdown
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from collections import Counter

# Download required NLTK data
# try:
#     nltk.data.find('tokenizers/punkt')
# except LookupError:
#     nltk.download('punkt')
# try:
#     nltk.data.find('corpora/stopwords')
# except LookupError:
#     nltk.download('stopwords')
# try:
#     nltk.data.find('corpora/wordnet')
# except LookupError:
#     nltk.download('wordnet')

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
    # Configure logging
    logging.basicConfig(
        filename='llm_responses.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Log request information
    request_info = {
        'timestamp': datetime.now().isoformat(),
        'model': os.environ.get("MODEL"),
        'max_tokens': max_tokens,
        'temperature': temperature,
        'prompt_length': len(prompt)
    }
    logging.info(f"Request: {json.dumps(request_info)}")
    
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
    
    # Log response information
    response_info = {
        'timestamp': datetime.now().isoformat(),
        'response_length': len(text),
        'response_preview': text[:100] + '...' if len(text) > 100 else text
    }
    logging.info(f"Response: {json.dumps(response_info)}")
    
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

def is_valid_word(word: str) -> bool:
    """
    Check if a word is a valid English word.
    
    Args:
        word: Word to check
        
    Returns:
        bool: True if word is valid
    """
    # Must be at least 3 characters long
    if len(word) < 3:
        return False
        
    # Must contain at least one vowel
    if not any(c in 'aeiouy' for c in word.lower()):
        return False
        
    # Must not contain numbers
    if any(c.isdigit() for c in word):
        return False
        
    # Must not be all uppercase (likely an acronym)
    if word.isupper() and len(word) > 1:
        return False
        
    # Must be in WordNet or be a common technical term
    if wordnet.synsets(word) or word in TECHNICAL_TERMS:
        return True
        
    return False


# Common technical terms that might not be in WordNet
TECHNICAL_TERMS = {
    'gpu', 'cpu', 'api', 'url', 'http', 'https', 'json', 'xml', 'html', 'css',
    'javascript', 'python', 'java', 'c++', 'c#', 'ruby', 'php', 'sql', 'nosql',
    'mongodb', 'mysql', 'postgresql', 'redis', 'docker', 'kubernetes', 'aws',
    'azure', 'gcp', 'cloud', 'serverless', 'microservice', 'api', 'rest',
    'graphql', 'websocket', 'tcp', 'udp', 'ip', 'dns', 'ssl', 'tls', 'ssh',
    'ftp', 'smtp', 'pop3', 'imap', 'ldap', 'oauth', 'jwt', 'jwt', 'jwt',
    'token', 'session', 'cookie', 'cache', 'cdn', 'dns', 'domain', 'subdomain',
    'endpoint', 'route', 'path', 'query', 'parameter', 'header', 'body',
    'request', 'response', 'status', 'code', 'error', 'exception', 'stack',
    'trace', 'log', 'debug', 'info', 'warn', 'error', 'fatal', 'level',
    'config', 'setting', 'environment', 'variable', 'constant', 'enum',
    'interface', 'class', 'object', 'method', 'function', 'procedure',
    'routine', 'module', 'package', 'library', 'framework', 'sdk', 'api',
    'toolkit', 'plugin', 'extension', 'addon', 'widget', 'component',
    'element', 'node', 'edge', 'vertex', 'graph', 'tree', 'forest', 'heap',
    'stack', 'queue', 'list', 'array', 'vector', 'matrix', 'tensor',
    'scalar', 'vector', 'matrix', 'tensor', 'gradient', 'derivative',
    'integral', 'sum', 'product', 'quotient', 'remainder', 'modulo',
    'exponent', 'root', 'logarithm', 'sine', 'cosine', 'tangent',
    'hyperbolic', 'trigonometric', 'algebraic', 'geometric', 'arithmetic',
    'statistical', 'probabilistic', 'stochastic', 'deterministic',
    'algorithmic', 'computational', 'numerical', 'analytical', 'symbolic',
    'logical', 'boolean', 'binary', 'ternary', 'quaternary', 'quinary',
    'senary', 'septenary', 'octal', 'decimal', 'hexadecimal', 'octal',
    'binary', 'decimal', 'hexadecimal', 'octal', 'binary', 'decimal',
    'hexadecimal', 'octal', 'binary', 'decimal', 'hexadecimal'
}

def extract_high_frequency_words(category: str, top_n: int = 100) -> None:
    """
    Extract high frequency words from outlines and markdown files in a category.
    
    Args:
        category: Category name (e.g., 'econ')
        top_n: Number of top frequency words to extract
    """
    # Initialize stopwords
    stop_words = set(stopwords.words('english'))
    # Add custom stopwords
    custom_stop_words = {
        'et', 'al', 'e.g', 'i.e', 'fig', 'table', 'section', 'chapter',
        'figure', 'figures', 'tables', 'sections', 'chapters', 'paper',
        'study', 'studies', 'research', 'researchers', 'authors', 'author',
        'review', 'reviews', 'survey', 'surveys', 'analysis', 'analyses',
        'method', 'methods', 'approach', 'approaches', 'result', 'results',
        'conclusion', 'conclusions', 'introduction', 'background', 'related',
        'work', 'works', 'literature', 'discussion', 'discussions', 'summary',
        'summaries', 'overview', 'overviews', 'example', 'examples', 'case',
        'cases', 'model', 'models', 'framework', 'frameworks', 'system',
        'systems', 'algorithm', 'algorithms', 'technique', 'techniques',
        'methodology', 'methodologies', 'experiment', 'experiments',
        'evaluation', 'evaluations', 'performance', 'performances',
        'implementation', 'implementations', 'application', 'applications',
        'development', 'developments', 'design', 'designs', 'process',
        'processes', 'analysis', 'analyses', 'evaluation', 'evaluations',
        'comparison', 'comparisons', 'comparative', 'comparatively',
        'experimental', 'experimentally', 'theoretical', 'theoretically',
        'empirical', 'empirically', 'practical', 'practically', 'technical',
        'technically', 'theoretical', 'theoretically', 'empirical',
        'empirically', 'practical', 'practically', 'technical', 'technically',
        'theoretical', 'theoretically', 'empirical', 'empirically',
        'practical', 'practically', 'technical', 'technically'
    }
    stop_words.update(custom_stop_words)
    
    # Initialize word counter
    word_counter = Counter()
    
    # Process all topic directories in the category
    category_dir = os.path.join("surveys", category)
    if not os.path.exists(category_dir):
        print(f"Category directory {category_dir} does not exist")
        return
        
    for topic_dir in os.listdir(category_dir):
        topic_path = os.path.join(category_dir, topic_dir)
        if not os.path.isdir(topic_path):
            continue
            
        pdfs_dir = os.path.join(topic_path, "pdfs")
        if not os.path.exists(pdfs_dir):
            continue
            
        # Process outline files
        outline_path = os.path.join(pdfs_dir, "outline_raw.json")
        if os.path.exists(outline_path):
            try:
                with open(outline_path, 'r', encoding='utf-8') as f:
                    outline_data = json.load(f)
                    # Extract text from outline (assuming list of [level, title] pairs)
                    outline_text = ' '.join([
                        str(item[1]) if isinstance(item, list) and len(item) > 1 else str(item)
                        for item in outline_data
                    ])
                    # Tokenize and count words
                    words = word_tokenize(outline_text.lower())
                    # Filter words
                    words = [
                        word for word in words 
                        if word.isalnum() 
                        and word not in stop_words 
                        and is_valid_word(word)
                    ]
                    word_counter.update(words)
            except Exception as e:
                print(f"Error processing outline {outline_path}: {e}")
        
        # Process markdown files
        for file in os.listdir(pdfs_dir):
            if file.endswith('.md'):
                md_path = os.path.join(pdfs_dir, file)
                try:
                    with open(md_path, 'r', encoding='utf-8') as f:
                        md_text = f.read()
                        # Remove code blocks
                        md_text = re.sub(r'```.*?```', '', md_text, flags=re.DOTALL)
                        # Remove inline code
                        md_text = re.sub(r'`.*?`', '', md_text)
                        # Remove URLs
                        md_text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', md_text)
                        # Remove email addresses
                        md_text = re.sub(r'[\w\.-]+@[\w\.-]+', '', md_text)
                        # Remove special characters
                        md_text = re.sub(r'[^\w\s]', ' ', md_text)
                        # Tokenize and count words
                        words = word_tokenize(md_text.lower())
                        # Filter words
                        words = [
                            word for word in words 
                            if word.isalnum() 
                            and word not in stop_words 
                            and is_valid_word(word)
                        ]
                        word_counter.update(words)
                except Exception as e:
                    print(f"Error processing markdown {md_path}: {e}")
    
    # Get top N words
    top_words = word_counter.most_common(top_n)
    
    # Save results
    output_path = os.path.join(category_dir, "high_frequency_words.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "words": [{"word": word, "count": count} for word, count in top_words]
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Saved top {len(top_words)} frequent words to {output_path}")

def process_and_evaluate_pdf(pdf_path: str) -> dict:
    """
    Process a PDF file and evaluate all metrics (both general and domain-specific).
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        dict: Dictionary containing all evaluation results
    """
    from evaluate import evaluate
    
    # Get directory and filename
    pdf_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.basename(pdf_path)
    pdf_stem = os.path.splitext(pdf_name)[0]
    
    # Step 1: Convert PDF to markdown
    print(f"Converting PDF to markdown: {pdf_path}")
    if os.path.exists(os.path.join(pdf_dir, pdf_stem + ".md")):
        md_path = os.path.join(pdf_dir, pdf_stem + ".md")
    else:
        md_path, md_content = pdf2md(pdf_path, pdf_dir)
        if not md_path:
            print(f"Failed to convert PDF: {pdf_path}")
        return {}
    
    # Step 2: Extract and refine outline

    # Step 3: Extract references using reference.py logic 
    extract_refs(input_file=md_path, output_folder=os.path.dirname(md_path))
    # Save sentence-reference mapping
    
    # Step 4: Evaluate with general criteria
    print("Evaluating with general criteria...")
    general_results = evaluate(
        md_path=md_path,
        do_outline=True,
        do_content=True,
        do_reference=True,
        criteria_type="general"
    )
    
    # Step 5: Evaluate with domain-specific criteria
    print("Evaluating with domain-specific criteria...")
    domain_results = evaluate(
        md_path=md_path,
        do_outline=True,
        do_content=True,
        do_reference=True,
        criteria_type="domain"
    )
    
    # Combine results
    all_results = {
        "general": general_results,
        "domain": domain_results,
        "metadata": {
            "pdf_path": pdf_path,
            "md_path": md_path
        }
    }
    
    # # Save combined results
    # results_path = os.path.join(pdf_dir, "all_results.json")
    # with open(results_path, "w", encoding="utf-8") as f:
    #     json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # print(f"All results saved to: {results_path}")
    return all_results

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
    # extract_high_frequency_words("econ")
    process_and_evaluate_pdf("temp/2411.15594v5.pdf")
    # print(extract_references_from_md("temp/2411.15594v5.md"))