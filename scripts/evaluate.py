import json
import os
import dotenv
from prompts import CONTENT_EVALUATION_PROMPT, OUTLINE_EVALUATION_PROMPT, CRITERIA, REFERENCE_EVALUATION_PROMPT
from utils import extract_and_save_outline_from_md, extract_references_from_md, extract_topic_from_path, getClient, generateResponse, robust_json_parse,fill_single_criterion_prompt
class Judge():
    def __init__(self):
        dotenv.load_dotenv()
        self.client = getClient()
    
    def judge(self, prompt):
        """
        :param prompt: str
        :return: str
        """
        response = generateResponse(self.client, prompt)
        try:
            result = robust_json_parse(response)
            return result
        except Exception as e:
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

def evaluate_outline(md_path: str) -> dict:
    """
    Extract outline from the given Markdown file, call LLM to score, and return {criteria_name: score}.
    If extraction or scoring fails, assign a score of 0.
    :param md_path: Markdown file path
    :return: dict, key is the evaluation criterion, value is the score
    """
    results = {}
    criteria_name = "Outline"
    try:
        # 1. Extract and save outline.json (assume this function is implemented)
        extract_and_save_outline_from_md(md_path)

        # 2. Read outline.json
        outline_json_path = os.path.join(os.path.dirname(md_path), "outline.json")
        with open(outline_json_path, "r", encoding="utf-8") as f:
            outline_list = json.load(f)

        # 3. Format outline as string (each item on a new line)
        outline_str = "\n".join([json.dumps(item, ensure_ascii=False) for item in outline_list])

        # 4. Use the grandparent folder name as the topic
        topic = extract_topic_from_path(outline_json_path)

        # 5. Build the prompt and get the score
        criterion = CRITERIA[criteria_name]
        prompt = fill_single_criterion_prompt(
            prompt_template=OUTLINE_EVALUATION_PROMPT,
            content=outline_str,
            topic=topic,
            criterion=criterion,
            criteria_name=criteria_name,
            type="outline"
        )
        try:
            score_dict = judge.judge(prompt)
            if not (isinstance(score_dict, dict) and criteria_name in score_dict):
                results[criteria_name] = 0
            else:
                results.update(score_dict)
        except Exception as e:
            results[criteria_name] = 0
    except Exception as e:
        results[criteria_name] = 0
    print("The score is: ", results)
    return results

def evaluate_content(md_path: str) -> dict:
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

def evaluate_reference(md_path: str) -> dict:
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

if __name__ == "__main__":
    # 测试代码
    #md_path = "surveys/cs/3D Gaussian Splatting Techniques/AutoSurvey/3D Gaussian Splatting Techniques.md"  # 替换为实际的文件路径
    md_path = "surveys\cs\Agent-based Modeling and Simulation using Large Language Models\AutoSurvey\Agent-based Modeling and Simulation using Large Language Models.md"
    evaluate_outline(md_path)
    evaluate_content(md_path)
    evaluate_reference(md_path)


