from concurrent.futures import ThreadPoolExecutor, as_completed
import glob
import json
import math
import os
from queue import Queue
import threading
import time
import dotenv
import pandas as pd
from prompts import CONTENT_EVALUATION_PROMPT, CONTENT_FAITHFULNESS_PROMPT, OUTLINE_EVALUATION_PROMPT, CRITERIA, OUTLINE_STRUCTURE_PROMPT, REFERENCE_EVALUATION_PROMPT, OUTLINE_COVERAGE_PROMPT, REFERENCE_QUALITY_PROMPT, CONTENT_EVALUATION_SIMULTANEOUS_PROMPT
from reference import extract_refs, split_markdown_content_and_refs
from utils import build_outline_tree_from_levels, count_md_features, count_sentences, extract_and_save_outline_from_md, extract_references_from_md, extract_topic_from_path, getClient, generateResponse, pdf2md, refine_outline_if_single_level, robust_json_parse,fill_single_criterion_prompt, read_md
import logging
from atomic_facts import extract_and_deduplicate_facts, extract_facts_only

class Judge:
    """
    A class to handle LLM-based evaluation using OpenAI's API.
    """
    def __init__(self) -> None:
        """
        Initialize the Judge with OpenAI client and logging configuration.
        """
        dotenv.load_dotenv()
        with open('judge.log', 'w') as log_file:
            log_file.truncate(0)
        self.client = getClient()
        # Configure logging
        logging.basicConfig(filename='judge.log', level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
    
    def judge(self, prompt: str) -> dict | None:
        """
        Evaluate a prompt using the LLM and return the parsed response.
        
        Args:
            prompt (str): The prompt to evaluate
            
        Returns:
            dict | None: Parsed JSON response or None if parsing fails
        """
        response = generateResponse(self.client, prompt)
        logging.info(f"Response received: {response}")
        try:
            result = robust_json_parse(response)
            return result
        except Exception as e:
            logging.error(f"Error parsing JSON: {e}")
            print("Error parsing JSON:", e)
            return None
        
judge = Judge()


# ------------- Outline Evaluation Functions ------------

def evaluate_outline_llm(outline_json_path: str) -> dict:
    """
    Evaluate the outline using LLM-based criteria.
    
    Args:
        outline_json_path (str): Path to the outline JSON file
        
    Returns:
        dict: Dictionary containing evaluation scores
    """
    criteria_name = "Outline"
    results = {}
    try:
        # 1. Read outline.json
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)

        # 2. Format outline as string
        outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])

        # 3. Use parent directory name as topic
        topic = extract_topic_from_path(outline_json_path)

        # 4. Build prompt and get score
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
    standard_count: int = 10,      # Reference section count for coverage calculation
    avg_count: int = 30,           # Ideal/expected section count for length penalty
    min_section_count: int = 5     # Minimum allowed section count
) -> float:
    """
    Evaluate outline coverage score Q', including logarithmic length penalty.
    
    Args:
        outline_json_path (str): Path to the outline JSON file
        standard_count (int, optional): Reference section count for coverage. Defaults to 10.
        avg_count (int, optional): Ideal section count for length penalty. Defaults to 30.
        min_section_count (int, optional): Minimum allowed section count. Defaults to 5.
        
    Returns:
        float: Coverage score between 0 and 100
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

        K = matched_count         # Number of matched sections
        N = standard_count        # Reference section count
        M = total_section_count   # Actual section count
        U = max(M - K, 0)        # Unmatched sections

        R = K / N if N > 0 else 0
        O = U / M if M > 0 else 0
        F_harmonic = 2 * R * O / (R + O) if (R + O) > 0 else 0

        # Logarithmic penalty term: normalized by avg_count
        if M < min_section_count:
            length_penalty = 0
        else:
            length_penalty = min(1.0, math.log(max(M, 1) + 1) / math.log(avg_count + 1))

        Q_prime = F_harmonic * length_penalty

        return round(Q_prime * 100, 4)

    except Exception as e:
        print(f"Error evaluating outline coverage: {e}")
        return 0.0

def evaluate_outline_structure(outline_json_path: str) -> tuple[float, list[dict]]:
    """
    Evaluate the hierarchical structure of the outline.
    
    Args:
        outline_json_path (str): Path to the outline JSON file
        
    Returns:
        tuple[float, list[dict]]: (global structure score, list of node scores)
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
        response = judge.judge(prompt)
        result = response.get("children", [])
        yes_count = sum(1 for child in result if str(child.get("is_included", "")).lower() == "yes")
        total = len(result)
        node_score = yes_count / total if total > 0 else 1.0  # Full score if no children
        node_scores.append({
            "parent_index": parent["index"],
            "parent_title": parent["title"],
            "score": node_score
        })

    global_score = round(sum(x["score"] for x in node_scores) / len(node_scores) * 100, 4) if node_scores else 1.0
    return global_score, node_scores

def evaluate_outline_number(outline_json_path: str) -> dict:
    """
    Evaluate the number of sections in the outline.
    
    Args:
        outline_json_path (str): Path to the outline JSON file
        
    Returns:
        dict: Dictionary containing the section count
    """
    results = {}
    try:
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)
        total_section_count = len(outline_list)
        results["Outline_no"] = total_section_count
    except Exception as e:
        print(f"Error evaluating outline number: {e}")
        results["Outline_no"] = 0
    return results

def evaluate_outline(
    md_path: str,
    do_llm: bool = True,
    do_coverage: bool = True,
    do_structure: bool = True
) -> dict:
    """
    Evaluate the outline of a markdown file.
    
    Args:
        md_path (str): Path to the markdown file
        do_llm (bool, optional): Whether to perform LLM evaluation. Defaults to True.
        do_coverage (bool, optional): Whether to evaluate coverage. Defaults to True.
        do_structure (bool, optional): Whether to evaluate structure. Defaults to True.
        
    Returns:
        dict: Dictionary containing evaluation results
    """
    results = {}
    outline_json_path = os.path.join(os.path.dirname(md_path), "outline.json")
    
    # 1. Extract outline from md (only if outline.json doesn't exist)
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

    # 2. LLM evaluation
    if do_llm:
        try:
            outline_results = evaluate_outline_llm(outline_raw_json_path)
            results.update(outline_results)
        except Exception as e:
            print("Error in evaluating outline llm:", e)
            results["Outline"] = 0
    else:
        print("Skip evaluate_outline_llm.")

    # 3. Coverage evaluation
    if do_coverage:
        try:
            coverage_results = evaluate_outline_coverage(outline_raw_json_path)
            results["Outline_coverage"] = coverage_results
        except Exception as e:
            print("Error in evaluating outline coverage:", e)
            results["Outline_coverage"] = 0
    else:
        print("Skip evaluate_outline_coverage.")

    # 4. Structure evaluation
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

    # 5. Number evaluation
    try:
        number_results = evaluate_outline_number(outline_json_path)
        results.update(number_results)
    except Exception as e:
        print("Error in evaluating outline number:", e)
        results["Outline_no"] = 0

    return results

# ------------- Content Evaluation Functions ------------

def evaluate_content_llm(md_path: str) -> dict:
    """
    Evaluate content using LLM-based criteria.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing evaluation scores for each criterion
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
            type="content"
        )
        try:
            score_dict = judge.judge(prompt)
            if not (isinstance(score_dict, dict) and criteria_name in score_dict):
                results[criteria_name] = 0
            else:
                results.update(score_dict)
        except Exception as e:
            results[criteria_name] = 0

    return results

def evaluate_content_llm_simultaneous(md_path: str) -> dict:
    """
    Evaluate content using LLM-based criteria simultaneously for all criteria.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing evaluation scores for all criteria
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
    
    # Prepare prompt parameters for all criteria
    prompt_params = {
        "topic": topic,
        "content": content_str
    }
    
    # Add all criteria descriptions and scores to prompt parameters
    for criteria_name in content_criteria:
        criterion = CRITERIA[criteria_name]
        prompt_params[f"{criteria_name.lower()}_description"] = criterion["description"]
        for i in range(1, 6):
            prompt_params[f"{criteria_name.lower()}_score_{i}"] = criterion[f"score {i}"]

    try:
        # Generate the prompt with all criteria
        prompt = CONTENT_EVALUATION_SIMULTANEOUS_PROMPT.format(**prompt_params)
        
        # Get scores for all criteria at once
        score_dict = judge.judge(prompt)
        
        # Validate and update results
        if isinstance(score_dict, dict):
            for criteria_name in content_criteria:
                if criteria_name in score_dict:
                    results[criteria_name] = score_dict[criteria_name]
                else:
                    results[criteria_name] = 0
        else:
            for criteria_name in content_criteria:
                results[criteria_name] = 0
    except Exception as e:
        print(f"Error in simultaneous evaluation: {e}")
        for criteria_name in content_criteria:
            results[criteria_name] = 0

    return results

def evaluate_content_informativeness(md_path: str) -> dict:
    """
    Evaluate the informativeness of the content by analyzing various features.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing density scores for various content features
    """
    md_content = read_md(md_path)
    counts = count_md_features(md_content)
    sentences = counts.get('sentences', 1)
    results = {}    

    images_density = counts.get('images', 0) / sentences
    equations_density = counts.get('equations', 0) / sentences
    tables_density = counts.get('tables', 0) / sentences
    total_density = (counts.get('images', 0) + counts.get('equations', 0) + counts.get('tables', 0)) / sentences

    results["Images_density"] = round(images_density * 100, 4)
    results["Equations_density"] = round(equations_density * 100, 4)
    results["Tables_density"] = round(tables_density * 100, 4)
    results["Total_density"] = round(total_density * 100, 4)

    # Citation density
    total_citations = 0
    csv_path = os.path.join(os.path.dirname(md_path), os.path.basename(md_path).replace(".md", ".csv"))  
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = pd.read_csv(f)
        for index, row in reader.iterrows():
            sentence = row["sentence"]
            references = row["references"].split(";")
            citations = len(references)
            total_citations += citations
    if total_citations > 0:
        results["Citations_density"] = round(total_citations * 100 / sentences, 4)
    else:
        results["Citations_density"] = 0

    # Claim density
    topic = extract_topic_from_path(md_path)
    results_claims = extract_facts_only(md_content, topic)
    results["Claim_density"] = results_claims.get("claim_density", 0) * 100
    # results["Claim_density_after_deduplication"] = results_claims.get("claim_density_after_dedup", 0) * 100
    return results

def evaluate_content_faithfulness(md_path: str) -> dict:
    """
    Evaluate the faithfulness of content by checking reference support.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing reference quality scores
    """
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
        prompt = CONTENT_FAITHFULNESS_PROMPT.format(
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
        except Exception as e:
            total_count += 0
            supported_count += 0
            print("Error in evaluating reference quality:", e)
            continue

    if total_count > 0:
        results["Reference_quality"] = round(supported_count / total_count, 4) * 100
    else:
        results["Reference_quality"] = 0
    print("Reference quality score:", results)
    return results

def evaluate_content_faithfulness_parallel(md_path: str, max_workers: int = 4) -> dict:
    """
    Evaluate content faithfulness using parallel processing.
    
    Args:
        md_path (str): Path to the markdown file
        max_workers (int, optional): Maximum number of worker threads. Defaults to 4.
        
    Returns:
        dict: Dictionary containing reference quality scores
    """
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

    total_count = 0
    supported_count = 0
    topic = extract_topic_from_path(md_path)

    # Define single evaluation task
    def evaluate_sentence(sentence: str, references: list[str]) -> tuple[int, int]:
        """
        Evaluate a single sentence and its references.
        
        Args:
            sentence (str): The sentence to evaluate
            references (list[str]): List of references to check
            
        Returns:
            tuple[int, int]: (total references, supported references)
        """
        prompt = CONTENT_FAITHFULNESS_PROMPT.format(
            sentence=sentence,
            references="\n".join(references),
            topic=topic
        )
        try:
            response = judge.judge(prompt)
            total = response.get("total", 0)
            supported = response.get("supported", 0)
            return int(total), int(supported)
        except Exception as e:
            print("Error in evaluating reference quality:", e)
            return 0, 0

    # Process all sentences in parallel
    futures = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for sentence, references in refs_mapping.items():
            futures.append(executor.submit(evaluate_sentence, sentence, references))

        for future in as_completed(futures):
            total, supported = future.result()
            total_count += total
            supported_count += supported

    if total_count > 0:
        results["Reference_quality"] = round(supported_count / total_count * 100, 2)
    else:
        results["Reference_quality"] = 0.0

    print("Reference quality score:", results)
    return results

def evaluate_content_sentence_number(md_path: str) -> dict:
    """
    Count the number of sentences in the content.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing the sentence count
    """
    results = {}
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content_str = f.read()

        main_content, _ = split_markdown_content_and_refs(content_str)
        sentence_count = count_sentences(main_content)
        results["Sentence_no"] = sentence_count
    except Exception as e:
        print("Error in evaluating sentence number:", e)
        results["Sentence_no"] = 0
    return results

def evaluate_content(
    md_path: str,
    do_llm: bool = True,
    do_info: bool = True,
    do_faithfulness: bool = True
) -> dict:
    """
    Evaluate content using multiple criteria.
    
    Args:
        md_path (str): Path to the markdown file
        do_llm (bool, optional): Whether to perform LLM evaluation. Defaults to True.
        do_info (bool, optional): Whether to evaluate informativeness. Defaults to True.
        do_faithfulness (bool, optional): Whether to evaluate faithfulness. Defaults to True.
        
    Returns:
        dict: Dictionary containing all evaluation results
    """
    results = {}
    content_criteria = [
        "Coverage", "Structure", "Relevance", "Language", "Criticalness"
    ]
    info_criteria = [
        "Images_density", "Equations_density", "Tables_density", 
        "Total_density", "Claim_density", 
    ]
    
    # 1. LLM evaluation
    if do_llm:
        try:
            # Use the new simultaneous evaluation function
            results.update(evaluate_content_llm_simultaneous(md_path))
        except Exception as e:
            print("Error in evaluating content:", e)
            for criteria_name in content_criteria:
                results[criteria_name] = 0
    else:
        print("Skip evaluate_content_llm.")

    # 2. Informativeness evaluation
    if do_info:
        try:
            results.update(evaluate_content_informativeness(md_path))
        except Exception as e:
            print("Error in evaluating content informativeness:", e)
            for criteria_name in info_criteria:
                results[criteria_name] = 0
    else:
        print("Skip evaluate_content_informativeness.")

    # 3. Faithfulness evaluation
    if do_faithfulness:
        try:
            results.update(evaluate_content_faithfulness(md_path))
        except Exception as e:
            print("Error in evaluating content faithfulness:", e)
            results['Citations_density'] = 0
    else:
        print("Skip evaluate_content_faithfulness.")

    # 4. Sentence count evaluation
    try:
        results.update(evaluate_content_sentence_number(md_path))
    except Exception as e:
        print("Error in evaluating content sentence number:", e)
        results["Sentence_no"] = 0

    return results

# ------------- Reference Evaluation Functions -------------

def evaluate_reference_llm(md_path: str) -> dict:
    """
    Evaluate references using LLM-based criteria.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing reference evaluation scores
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
    return results

def evaluate_reference_density(md_path: str) -> dict:
    """
    Calculate the density of references in the content.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing reference density score
    """
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
    return results

def evaluate_reference_quality(md_path: str) -> dict:
    """
    Evaluate the quality of references using LLM.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing reference quality score
    """
    results = {}
    batch_size = 20
    ref_path = os.path.join(os.path.dirname(md_path), "references.json")
    topic = extract_topic_from_path(md_path)
    total_count = 0
    supported_count = 0

    with open(ref_path, "r", encoding="utf-8") as f:
        refs = json.load(f)
    
    for i in range(0, len(refs), batch_size):
        batch_refs = refs[i:i + batch_size]
        prompt = REFERENCE_QUALITY_PROMPT.format(
            references="\n".join(batch_refs),
            topic=topic
        )
        try:
            response = judge.judge(prompt)
            total = response.get("total", 0)
            supported = response.get("supported", 0)
            total_count += int(total)
            supported_count += int(supported)
        except Exception as e:
            print("Error in evaluating reference quality:", e)
            continue

    if total_count > 0:
        results["Reference_quality"] = round(supported_count / total_count * 100, 2)
    else:
        results["Reference_quality"] = 0.0

    return results

def evaluate_reference_number(md_path: str) -> dict:
    """
    Count the number of references in the content.
    
    Args:
        md_path (str): Path to the markdown file
        
    Returns:
        dict: Dictionary containing the reference count
    """
    results = {}
    json_path = os.path.join(os.path.dirname(md_path), "references.json")

    with open(json_path, "r", encoding="utf-8") as f:
        references = json.load(f)
    
    total_count = len(references)
    results["Reference_no"] = total_count
    return results

def evaluate_reference(
    md_path: str,
    do_llm: bool = True,
    do_density: bool = True,
    do_quality: bool = True
) -> dict:
    """
    Evaluate references using multiple criteria.
    
    Args:
        md_path (str): Path to the markdown file
        do_llm (bool, optional): Whether to perform LLM evaluation. Defaults to True.
        do_density (bool, optional): Whether to evaluate density. Defaults to True.
        do_quality (bool, optional): Whether to evaluate quality. Defaults to True.
        
    Returns:
        dict: Dictionary containing all reference evaluation results
    """
    results = {}

    # 0. Extract references if not exists
    reference_path = os.path.join(os.path.dirname(md_path), "references.json")
    if not os.path.exists(reference_path):
        extract_refs(input_file=md_path, output_folder=os.path.dirname(md_path))

    # 1. LLM evaluation
    if do_llm:
        try:
            results.update(evaluate_reference_llm(md_path))
        except Exception as e:
            print("Error in evaluating reference:", e)
            results["Reference"] = 0
    else:
        print("Skip evaluate_reference_llm.")

    # 2. Density evaluation
    if do_density:
        try:
            results.update(evaluate_reference_density(md_path))
        except Exception as e:
            print("Error in evaluating reference density:", e)
            results["Reference_density"] = 0
    else:
        print("Skip evaluate_reference_density.")

    # 3. Quality evaluation
    if do_quality:
        try:
            results.update(evaluate_reference_quality(md_path))
        except Exception as e:
            print("Error in evaluating reference quality:", e)
            results["Reference_quality"] = 0
    else:
        print("Skip evaluate_reference_quality.")

    # 4. Number evaluation
    try:
        results.update(evaluate_reference_number(md_path))
    except Exception as e:
        print("Error in evaluating reference number:", e)
        results["Reference_no"] = 0
    return results

# ------------- Main Evaluation Functions -------------

def evaluate(
    md_path: str, 
    model: str = "default",
    do_outline: bool = True, 
    do_content: bool = True, 
    do_reference: bool = True
) -> dict:
    """
    Evaluate a markdown file using specified criteria and model.
    
    Args:
        md_path (str): Path to the markdown file
        model (str, optional): Model name for evaluation. Defaults to "default".
        do_outline (bool, optional): Whether to evaluate outline. Defaults to True.
        do_content (bool, optional): Whether to evaluate content. Defaults to True.
        do_reference (bool, optional): Whether to evaluate references. Defaults to True.
        
    Returns:
        dict: Dictionary containing all evaluation results
    """
    start_time = time.time()
    results = {}
    results_path = os.path.join(
        os.path.dirname(md_path), 
        f"results_{model}.json"
    )
    print("Start evaluating:", md_path)
    print("Using model:", model)

    # Define required keys for each evaluation section
    outline_keys = ["Outline", "Outline_coverage", "Outline_structure", "Outline_no"]
    content_keys = [
        "Coverage", "Structure", "Relevance", "Language", "Criticalness",
        "Images_density", "Equations_density", "Tables_density", "Total_density", "Citations_density", "Sentence_no",
        "Claim_density"
    ]
    reference_keys = ["Reference", "Reference_density", "Reference_quality", "Reference_no"]

    # Load existing results if available
    if os.path.exists(results_path):
        try:
            with open(results_path, "r", encoding="utf-8") as f:
                results = json.load(f)
        except Exception as e:
            print("Error in loading existing results:", e)

    # Evaluate outline if requested and not already complete
    if do_outline:
        print("Evaluating outline...")
        if not all(k in results for k in outline_keys):
            try:
                results.update(evaluate_outline(md_path))
            except Exception as e:
                print("Error in evaluating outline:", e)
        else:
            print("Outline already complete, skip.")
    else:
        print("Skip evaluating outline.")

    # Evaluate content if requested and not already complete
    if do_content:
        print("Evaluating content...")
        if not all(k in results for k in content_keys):
            try:
                results.update(evaluate_content(md_path))
            except Exception as e:
                print("Error in evaluating content:", e)
        else:
            print("Content already complete, skip.")
    else:
        print("Skip evaluating content.")

    # Evaluate references if requested and not already complete
    if do_reference:
        print("Evaluating reference...")
        if not all(k in results for k in reference_keys):
            try:
                results.update(evaluate_reference(md_path))
            except Exception as e:
                print("Error in evaluating reference:", e)
        else:
            print("Reference already complete, skip.")
    else:
        print("Skip evaluating reference.")

    # Save results
    try:
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error in saving results:", e)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Evaluation completed in {elapsed_time:.2f} seconds.")
    return results

def process_system(
    md_path: str,
    model: str,
    results_path: str,
    topic: str,
    system: str,
    do_outline: bool,
    do_content: bool,
    do_reference: bool
) -> None:
    """
    Process a single system's evaluation.
    
    Args:
        md_path (str): Path to the markdown file
        model (str): Model name for evaluation
        results_path (str): Path to save results
        topic (str): Topic name
        system (str): System name
        do_outline (bool): Whether to evaluate outline
        do_content (bool): Whether to evaluate content
        do_reference (bool): Whether to evaluate references
    """
    print(f"[{topic}/{system}] Evaluating: {md_path}")
    evaluate(md_path, 
             model=model,
             do_outline=do_outline, 
             do_content=do_content, 
             do_reference=do_reference)

def batch_evaluate_by_cat(
    cats: list[str],
    model: str,
    do_outline: bool = True,
    do_content: bool = True,
    do_reference: bool = True,
    num_workers: int = 1
) -> None:
    """
    Batch evaluate all markdown files in specified categories.
    
    Args:
        cats (list[str]): List of category names to evaluate
        model (str): Model name for evaluation
        do_outline (bool, optional): Whether to evaluate outline. Defaults to True.
        do_content (bool, optional): Whether to evaluate content. Defaults to True.
        do_reference (bool, optional): Whether to evaluate references. Defaults to True.
        num_workers (int, optional): Number of worker threads. Defaults to 1.
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
                # Find markdown files
                md_files = [f for f in os.listdir(sys_path) 
                            if f.lower().endswith(".md")]
                pdf_files = [f for f in os.listdir(sys_path) 
                            if f.lower().endswith(".pdf")]
                results_path = os.path.join(
                    sys_path, 
                    f"results_{model}.json"
                )
                # Convert PDF to markdown if no markdown exists
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
            # Sequential execution
            for args in tasks:
                process_system(*args)
        else:
            # Parallel execution
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                future_to_system = {executor.submit(process_system, *args): args for args in tasks}
                for future in as_completed(future_to_system):
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Exception in thread: {e}")

def batch_evaluate_by_system(
    system_list: list[str],
    model: str,
    tasks_json_path: str = "surveys/tasks.json",
    do_outline: bool = True,
    do_content: bool = False,
    do_reference: bool = True,
    num_workers: int = 1
) -> None:
    """
    Batch evaluate all tasks for specified systems.
    
    Args:
        system_list (list[str]): List of system names to evaluate
        model (str): Model name for evaluation
        tasks_json_path (str, optional): Path to tasks mapping JSON. Defaults to "surveys/tasks.json".
        do_outline (bool, optional): Whether to evaluate outline. Defaults to True.
        do_content (bool, optional): Whether to evaluate content. Defaults to True.
        do_reference (bool, optional): Whether to evaluate references. Defaults to True.
        num_workers (int, optional): Number of worker threads. Defaults to 1.
    """
    # Read tasks.json
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
                # Find markdown or PDF files
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
    Calculate average scores for a specific category, system, and model.
    
    Args:
        cat (str): Category name (e.g., "cs")
        system (str): System name (e.g., "InteractiveSurvey")
        model (str): Model name (e.g., "qwen-plus")
        
    Returns:
        dict: Dictionary containing average scores
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

    # Write to average_results.json
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    if os.path.exists(avg_results_path):
        with open(avg_results_path, "r", encoding="utf-8") as f:
            avg_results_data = json.load(f)
    else:
        avg_results_data = {}

    # Structure: system_name -> model_name -> averages
    if system not in avg_results_data:
        avg_results_data[system] = {}
    avg_results_data[system][model] = average_scores

    with open(avg_results_path, "w", encoding="utf-8") as f:
        json.dump(avg_results_data, f, ensure_ascii=False, indent=4)

    return average_scores

def calculate_average_score_by_cat(cat: str) -> dict:
    """
    Calculate average scores for all systems in a specific category.
    
    Args:
        cat (str): Category name (e.g., "cs")
        
    Returns:
        dict: Dictionary containing average scores for all systems in the category
    """
    base_dir = os.path.join("surveys", cat)
    topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    # Dictionary to store results for each system and model
    all_results = {}
    
    for topic in topics:
        topic_path = os.path.join(base_dir, topic)
        systems = [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]
        
        for system in systems:
            sys_path = os.path.join(topic_path, system)
            # Find all results files for this system
            results_files = glob.glob(os.path.join(sys_path, "results_*.json"))
            
            for results_file in results_files:
                # Extract model name from filename (e.g., "results_qwen-plus.json" -> "qwen-plus")
                model = os.path.basename(results_file).replace("results_", "").replace(".json", "")
                
                if system not in all_results:
                    all_results[system] = {}
                if model not in all_results[system]:
                    all_results[system][model] = {"total": {}, "count": 0}
                
                try:
                    with open(results_file, "r", encoding="utf-8") as f:
                        results = json.load(f)
                    
                    # Add scores to total
                    for key, value in results.items():
                        if key not in all_results[system][model]["total"]:
                            all_results[system][model]["total"][key] = 0
                        all_results[system][model]["total"][key] += value
                    
                    all_results[system][model]["count"] += 1
                except Exception as e:
                    print(f"Error processing {results_file}: {e}")
                    continue
    
    # Calculate averages for each system and model
    average_scores = {}
    for system, models in all_results.items():
        average_scores[system] = {}
        for model, data in models.items():
            if data["count"] > 0:
                average_scores[system][model] = {
                    key: round(value / data["count"], 4)
                    for key, value in data["total"].items()
                }
    
    # Write to average_results.json
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    with open(avg_results_path, "w", encoding="utf-8") as f:
        json.dump(average_scores, f, ensure_ascii=False, indent=4)
    
    return average_scores

def calculate_average_score_by_system(system: str, model: str) -> dict:
    """
    Calculate average scores for a specific system and model across all categories.
    
    Args:
        system (str): System name (e.g., "AutoSurvey")
        model (str): Model name (e.g., "gpt-4")
        
    Returns:
        dict: Dictionary containing average scores for the system-model combination
    """
    base_dir = "surveys"
    all_scores = {}
    count = 0
    
    # Get all category directories
    cats = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for cat in cats:
        cat_path = os.path.join(base_dir, cat)
        avg_results_path = os.path.join(cat_path, "average_results.json")
        
        if os.path.exists(avg_results_path):
            try:
                with open(avg_results_path, "r", encoding="utf-8") as f:
                    cat_results = json.load(f)
                
                if system in cat_results and model in cat_results[system]:
                    system_model_scores = cat_results[system][model]
                    for metric, value in system_model_scores.items():
                        if metric not in all_scores:
                            all_scores[metric] = 0
                        all_scores[metric] += value
                    count += 1
            except Exception as e:
                print(f"Error processing {avg_results_path}: {e}")
                continue
    
    # Calculate averages if we have data
    if count > 0:
        average_scores = {
            metric: round(value / count, 4)
            for metric, value in all_scores.items()
        }
    else:
        average_scores = {}
    
    return average_scores

def calculate_all_cats_average_scores() -> dict:
    """
    Calculate average scores for all categories and store them in their respective average_results.json files.
    
    Returns:
        dict: Dictionary containing average scores for all categories
    """
    base_dir = "surveys"
    all_cats_results = {}
    
    # Get all category directories
    cats = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for cat in cats:
        print(f"Calculating average scores for category: {cat}")
        cat_results = calculate_average_score_by_cat(cat)
        all_cats_results[cat] = cat_results
    
    return all_cats_results

def clear_average_score_by_cat(cat: str) -> None:
    """
    Clear average results for a specific category.
    
    Args:
        cat (str): Category name (e.g., "cs")
    """
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    if os.path.exists(avg_results_path):
        try:
            os.remove(avg_results_path)
            print(f"Removed average results for category: {cat}")
        except Exception as e:
            print(f"Failed to remove {avg_results_path}: {e}")

def clear_average_score_by_system(system: str, model: str) -> None:
    """
    Clear average results for a specific system and model from all category average results.
    
    Args:
        system (str): System name (e.g., "AutoSurvey")
        model (str): Model name (e.g., "gpt-4")
    """
    base_dir = "surveys"
    cats = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for cat in cats:
        avg_results_path = os.path.join(base_dir, cat, "average_results.json")
        if os.path.exists(avg_results_path):
            try:
                with open(avg_results_path, "r", encoding="utf-8") as f:
                    avg_results = json.load(f)
                
                if system in avg_results:
                    if model in avg_results[system]:
                        del avg_results[system][model]
                        # Remove system if no models remain
                        if not avg_results[system]:
                            del avg_results[system]
                
                with open(avg_results_path, "w", encoding="utf-8") as f:
                    json.dump(avg_results, f, ensure_ascii=False, indent=4)
                
                print(f"Cleared {system}/{model} from {cat} average results")
            except Exception as e:
                print(f"Error processing {avg_results_path}: {e}")

def clear_all_average_scores() -> None:
    """
    Clear all average results files (average_results.json and global_average_results.json).
    """
    base_dir = "surveys"
    
    # Clear category average results
    cats = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    for cat in cats:
        avg_results_path = os.path.join(base_dir, cat, "average_results.json")
        if os.path.exists(avg_results_path):
            try:
                os.remove(avg_results_path)
                print(f"Removed average results for category: {cat}")
            except Exception as e:
                print(f"Failed to remove {avg_results_path}: {e}")
    
    # Clear global average results
    global_results_path = os.path.join(base_dir, "global_average_results.json")
    if os.path.exists(global_results_path):
        try:
            os.remove(global_results_path)
            print("Removed global average results")
        except Exception as e:
            print(f"Failed to remove {global_results_path}: {e}")

def aggregate_results_to_csv(cat: str, metrics_to_fill: list[str] = ["Outline", "Reference"]) -> None:
    """
    Aggregate all results from a category into a CSV file.
    For specified metrics, if value is 0, fill with average of the same model.
    
    Args:
        cat (str): Category name (e.g., "cs")
        metrics_to_fill (list[str]): List of metrics that need to be filled with average if 0
    """
    base_dir = os.path.join("surveys", cat)
    all_results = []
    
    # Get all topics
    topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    # Collect all results
    for topic in topics:
        topic_path = os.path.join(base_dir, topic)
        systems = [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]
        
        for system in systems:
            sys_path = os.path.join(topic_path, system)
            # Find all results files
            results_files = glob.glob(os.path.join(sys_path, "results_*.json"))
            
            for results_file in results_files:
                model = os.path.basename(results_file).replace("results_", "").replace(".json", "")
                try:
                    with open(results_file, "r", encoding="utf-8") as f:
                        results = json.load(f)
                    
                    # Add basic info
                    entry = {
                        "topic": topic,
                        "system": system,
                        "model": model
                    }
                    # Add all metrics
                    entry.update(results)
                    all_results.append(entry)
                except Exception as e:
                    print(f"Error processing {results_file}: {e}")
    
    # Convert to DataFrame
    df = pd.DataFrame(all_results)
    
    # Fill 0 values with model averages for specified metrics
    for metric in metrics_to_fill:
        if metric in df.columns:
            # Calculate model averages for this metric
            model_avgs = df[df[metric] != 0].groupby('model')[metric].mean()
            
            # Fill 0 values with corresponding model average
            for model, avg in model_avgs.items():
                mask = (df['model'] == model) & (df[metric] == 0)
                df.loc[mask, metric] = avg
    
    # Save to CSV
    output_path = os.path.join(base_dir, f"{cat}_results.csv")
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

def clear_scores(cat: str, system: str, model: str, target: str = "All") -> None:
    """
    Clear evaluation results for a specific category, system, and model.
    
    Args:
        cat (str): Category name (e.g., "cs")
        system (str): System name (e.g., "InteractiveSurvey")
        model (str): Model name (e.g., "qwen-plus")
        target (str): Target to clear, one of ["Outline", "Content", "Reference", "All"]
    """
    # Define metric groups
    metric_groups = {
        "Outline": ["Outline", "Outline_coverage", "Outline_structure", "Outline_no"],
        "Content": ["Coverage", "Structure", "Relevance", "Language", "Criticalness",
                   "Images_density", "Equations_density", "Tables_density", 
                   "Total_density", "Citations_density", "Sentence_no",
                   "Claim_density"],
        "Reference": ["Reference", "Reference_density", "Reference_quality", "Reference_no"]
    }
    
    base_dir = os.path.join("surveys", cat)
    topics = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for topic in topics:
        topic_path = os.path.join(base_dir, topic)
        sys_path = os.path.join(topic_path, system)
        results_path = os.path.join(sys_path, f"results_{model}.json")
        
        if os.path.exists(results_path):
            try:
                with open(results_path, "r", encoding="utf-8") as f:
                    results = json.load(f)
                
                if target == "All":
                    # Remove the entire file
                    os.remove(results_path)
                else:
                    # Remove only specified metrics
                    metrics_to_remove = metric_groups.get(target, [])
                    for metric in metrics_to_remove:
                        if metric in results:
                            del results[metric]
                    
                    # Save updated results
                    with open(results_path, "w", encoding="utf-8") as f:
                        json.dump(results, f, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"Error processing {results_path}: {e}")
    
    # Update average_results.json
    avg_results_path = os.path.join("surveys", cat, "average_results.json")
    if os.path.exists(avg_results_path):
        try:
            with open(avg_results_path, "r", encoding="utf-8") as f:
                avg_results_data = json.load(f)
            
            if system in avg_results_data and model in avg_results_data[system]:
                if target == "All":
                    # Remove the entire system-model entry
                    del avg_results_data[system][model]
                    if not avg_results_data[system]:
                        del avg_results_data[system]
                else:
                    # Remove only specified metrics
                    metrics_to_remove = metric_groups.get(target, [])
                    for metric in metrics_to_remove:
                        if metric in avg_results_data[system][model]:
                            del avg_results_data[system][model][metric]
            
            with open(avg_results_path, "w", encoding="utf-8") as f:
                json.dump(avg_results_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error processing {avg_results_path}: {e}")

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
    # calculate_average_score("cs", "vanilla_outline", "qwen-plus-2025-04-28")
    # calculate_average_score_by_cat("econ")
    # clear_scores("cs", "AutoSurvey")
    # batch_evaluate_by_system(["vanilla"], "qwen-plus-2025-04-28", num_workers=4)
    # clear_all_scores()
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/vanilla_outline/3D Gaussian Splatting Techniques.md")
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/vanilla/3D Gaussian Splatting Techniques.md")
    # print(evaluate_outline_coverage("surveys/cs/3D Gaussian Splatting Techniques/vanilla/outline.json"))
    # evaluate_reference("surveys\cs/3D Gaussian Splatting Techniques\AutoSurvey/3D Gaussian Splatting Techniques.md")
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md")
    # surveys\cs\3D Gaussian Splatting Techniques\InteractiveSurvey
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/InteractiveSurvey/survey_3D Gaussian Splatting Techniques.md")
    # batch_evaluate_by_system(["AutoSurvey", "InteractiveSurvey", "LLMxMapReduce", "SurveyForge", "SurveyX","vanilla","vanilla_outline", "pdfs"], "gpt-4o", num_workers=4)
    # evaluate("surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md")
    # print(evaluate_content_informativeness("surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md"))
    # print(evaluate_content_llm_simultaneous("surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md"))
    calculate_all_cats_average_scores()

