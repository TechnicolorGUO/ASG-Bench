import os
import re
import json
import csv
import sys
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Add parent directory to path to import from reference module
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from reference import split_markdown_content_and_refs, parse_markdown

client = OpenAI(
  base_url=os.environ.get("BASE_URL"),
  api_key=os.environ.get("API_KEY"),
)

def generate_response(prompt):
    from openai import BadRequestError
    
    try:
        completion = client.chat.completions.create(
            model="qwen/qwen-plus",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )
        response_text = completion.choices[0].message.content.strip()
        return robust_json_parse(response_text)
    except BadRequestError as e:
        error_msg = str(e)
        if "maximum context length" in error_msg or "tokens" in error_msg.lower() or "too long" in error_msg.lower():
            # Re-raise token limit error to be handled by caller
            raise
        else:
            print(f"✗ BadRequestError: {error_msg}")
            return None
    except Exception as e:
        error_msg = str(e)
        if "maximum context length" in error_msg or "tokens" in error_msg.lower() or "too long" in error_msg.lower():
            # Re-raise token limit error to be handled by caller
            raise
        print(f"✗ Error generating response: {e}")
        return None

def robust_json_parse(response_text):
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse JSON response")
        print(f"Error: {e}")
        print(f"Response: {response_text[:500]}...")
        return None

aspects = {
  "outline": [
    {
      "Substantive Integrity": "Evaluates the depth, breadth, and scholarly merit of the content. This aspect aggregates criteria related to topical coverage, relevance, and content value, ensuring the outline comprehensively addresses the subject matter, maintains strict topical alignment, and incorporates meaningful scholarly elements like research gaps and conceptual frameworks rather than mere enumeration."
    },
    {
      "Structural Coherence": "Assesses the logical architecture and organizational flow of the outline. This aspect synthesizes criteria regarding structure, structural organization, and logical organization, focusing on the adherence to field-appropriate schemas (e.g., IMRaD), the natural progression of topics, and the clarity of relationships between sections to facilitate information localization and coherent argumentation."
    },
    {
      "Formal Precision": "Examines the technical execution and refinement of the outline's hierarchy and presentation. This aspect encompasses descriptiveness, topic uniqueness, structural balance, and hierarchical consistency, ensuring precise section titling, distinct non-redundant content, balanced distribution of subsections, and clear parent-child relationships that align with academic conventions."
    }
  ],
  "content": [
    {
      "Scope and Relevance": "Evaluates the breadth and pertinence of the content, ensuring it comprehensively covers key subtopics, representative works, and temporal or geographic diversity while maintaining strict alignment with the central research theme and avoiding extraneous information."
    },
    {
      "Structural Coherence": "Assesses the logical organization and flow of the work, focusing on the hierarchy of sections, the smoothness of transitions, the progression of arguments, and the overall narrative consistency that binds disparate elements into a unified whole."
    },
    {
      "Synthesis and Integration": "Measures the ability to move beyond sequential summarization to construct a cohesive intellectual framework, characterized by the identification of cross-paper connections, the recognition of overarching patterns, and the depth of comparative analysis."
    },
    {
      "Critical Insight and Novelty": "Examines the depth of intellectual contribution, including the rigorous critique of existing methodologies and limitations, the generation of original taxonomies or frameworks, and the identification of significant research gaps and future directions."
    },
    {
      "Scholarly Communication": "Reviews the quality of expression and academic rigor, encompassing clarity, fluency, and conciseness of language, as well as the precision of terminology, veracity of claims, and adherence to formal citation and formatting standards."
    }
  ],
  "reference": [
    {
      "Bibliometric Comprehensiveness": "Evaluates the extent and depth of the literature review, focusing on the quantitative coverage of the corpus, the inclusion of seminal works, and the balanced distribution of citations across relevant thematic clusters."
    },
    {
      "Evidential Integrity": "Assesses the reliability and precision of the scholarly discourse, ensuring that all claims are substantiated by appropriate evidence, generalizations are valid, and the attribution of ideas to their original authors is factually correct."
    },
    {
      "Referential Pertinence and Compliance": "Examines the quality of the bibliography by determining the thematic alignment of cited works with the research topic and verifying adherence to established academic standards regarding citation formatting, consistency, and completeness."
    }
  ]
}

EXPAND_ASPECT_PROMPT = """You are an academic survey expert. Now you are refining the writing guideline of survey writing.

Given:
1. Component Type: {component_name} (outline/content/reference)
2. Component Content: The actual {component_name} from a survey paper
3. Aspect: {aspect_name} - {aspect_description}
4. Target Number: {n}

Task:
Expand the given aspect "{aspect_name}" into {n} specific, detailed criteria. Each criterion should:
- Provide a clear, actionable explanation of what "{aspect_name}" means in the context of {component_name}
- Include a concrete example from the provided component content that demonstrates this criterion
- The example should be a summary/synthesis of relevant parts from the component content, NOT a direct verbatim quote
- Be specific enough to guide evaluation of survey {component_name}

Component Content:
{component_content}

Aspect to Expand:
Name: {aspect_name}
Description: {aspect_description}

Please return the result in the following JSON format:
{{
  "aspect_name": "{aspect_name}",
  "expanded_criteria": [
    {{
      "criterion_name": "Specific criterion name 1",
      "description": "Detailed explanation of what this criterion means",
      "example": "Summarized example from the component content that demonstrates this criterion"
    }},
    {{
      "criterion_name": "Specific criterion name 2",
      "description": "Detailed explanation of what this criterion means",
      "example": "Summarized example from the component content that demonstrates this criterion"
    }},
    ...
  ]
}}

Return only the JSON object, without any markdown code block markers or additional text."""

def split_survey_into_parts(content: str):
    """
    Split markdown content into three parts: outline, content, and reference.
    
    Args:
        content: Markdown content string
        
    Returns:
        tuple: (outline, content_text, reference_text)
            - outline: list of [level, title] pairs
            - content_text: main content without headers and references
            - reference_text: reference block text
    """
    # Extract outline (headers)
    lines = content.split('\n')
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
    
    # Split content and references
    main_content, ref_block = split_markdown_content_and_refs(content)
    
    return outline, main_content, ref_block


# ------------------------------------------------------------------------------

class Survey:
    def __init__(self, survey_json_path):
        """
        Initialize Survey from a JSON file containing split results.
        
        Args:
            survey_json_path: Path to JSON file with 'outline', 'content', and 'reference' keys
        """
        self.survey_json_path = survey_json_path
        self.load_from_json(survey_json_path)
    
    def load_from_json(self, json_path):
        """Load survey data from JSON file."""
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.outline = data.get('outline', [])
        self.content = data.get('content', '')
        self.reference = data.get('reference', [])
    
    def get_survey_json_path(self) -> str:
        return self.survey_json_path

    def get_survey_name(self) -> str:
        """Extract survey name from JSON file path."""
        basename = os.path.basename(self.survey_json_path)
        # Remove '_split.json' suffix if present
        if basename.endswith('_split.json'):
            return basename.replace('_split.json', '')
        elif basename.endswith('.json'):
            return basename.replace('.json', '')
        return basename
    
    def get_component_content(self, component_name: str) -> str:
        """
        Get formatted component content based on component name.
        
        Args:
            component_name: "outline", "content", or "reference"
            
        Returns:
            str: Formatted component content
        """
        if component_name == "outline":
            # Format outline as a readable string
            formatted_lines = []
            for level, title in self.outline:
                indent = "  " * (level - 1)
                formatted_lines.append(f"{indent}{'#' * level} {title}")
            return "\n".join(formatted_lines)
        elif component_name == "content":
            # Return content directly (already processed)
            return self.content
        elif component_name == "reference":
            # Format references as a readable string
            if isinstance(self.reference, list):
                return "\n".join(self.reference)
            return str(self.reference)
        else:
            raise ValueError(f"Unknown component name: {component_name}")
    

def expand_aspect(survey: Survey, component_name: str, aspect_dict: dict, n: int = 3) -> dict:
    """
    Expand a single aspect into n detailed criteria using the survey content.
    
    Args:
        survey: Survey instance
        component_name: "outline", "content", or "reference"
        aspect_dict: Dictionary with aspect name and description, e.g., {"Substantive Integrity": "..."}
        n: Number of criteria to expand into
        
    Returns:
        dict: Expanded criteria in JSON format
    """
    # Extract aspect name and description
    aspect_name = list(aspect_dict.keys())[0]
    aspect_description = aspect_dict[aspect_name]
    
    # Get component content
    component_content = survey.get_component_content(component_name)
    
    max_retries = 3
    original_component_content = component_content
    
    for retry_count in range(max_retries):
        try:
            # Format prompt
            prompt = EXPAND_ASPECT_PROMPT.format(
                component_name=component_name,
                component_content=component_content,
                aspect_name=aspect_name,
                aspect_description=aspect_description,
                n=n
            )
            
            # Call LLM
            response = generate_response(prompt)
            
            if response:
                return response
            else:
                # If response is None but no exception was raised, return None
                # (This is not a retry-able error)
                return None
                
        except Exception as e:
            error_msg = str(e)
            is_token_error = (
                "maximum context length" in error_msg.lower() or 
                "tokens" in error_msg.lower() or 
                "too long" in error_msg.lower()
            )
            
            if is_token_error and retry_count < max_retries - 1:
                # Content too long, keep the latter half and retry
                content_lines = component_content.split('\n')
                if len(content_lines) > 1:
                    # Keep the latter half
                    half_point = len(content_lines) // 2
                    component_content = '\n'.join(content_lines[half_point:])
                    print(f"⚠ Content too long, retrying with latter half (retry {retry_count + 1}/{max_retries})")
                else:
                    # If it's a single line, truncate to half length
                    component_content = component_content[len(component_content) // 2:]
                    print(f"⚠ Content too long, retrying with latter half (retry {retry_count + 1}/{max_retries})")
                # Continue to next retry iteration
                continue
            else:
                # Not a token error or max retries reached
                print(f"✗ Error expanding aspect: {e}")
                if retry_count < max_retries - 1:
                    print(f"Retrying... ({retry_count + 1}/{max_retries})")
                    # For non-token errors, retry with current content (don't restore original)
                    continue
                else:
                    print(f"✗ Failed after {max_retries} retries")
                    return None
    
    return None

def expand_with_survey(survey_json_path: str, n: int = 3):
    """
    Expand all aspects for a survey into detailed criteria.
    
    Args:
        survey_json_path: Path to survey JSON file (with split results)
        n: Number of criteria to expand each aspect into
    """
    survey = Survey(survey_json_path)
    results = {}
    
    for component_name in aspects:
        results[component_name] = []
        print(f"\n{'='*80}")
        print(f"Processing component: {component_name}")
        print(f"{'='*80}")
        
        for aspect_dict in aspects[component_name]:
            aspect_name = list(aspect_dict.keys())[0]
            print(f"\nExpanding aspect: {aspect_name}")
            
            expanded = expand_aspect(survey, component_name, aspect_dict, n)
            if expanded:
                results[component_name].append(expanded)
                print(f"✓ Successfully expanded into {len(expanded.get('expanded_criteria', []))} criteria")
            else:
                print(f"✗ Failed to expand aspect")
    
    return results

def save_results(results, survey_json_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    # Extract survey name from JSON path
    basename = os.path.basename(survey_json_path)
    if basename.endswith('_split.json'):
        survey_name = basename.replace('_split.json', '').replace(' ', '_')
    elif basename.endswith('.json'):
        survey_name = basename.replace('.json', '').replace(' ', '_')
    else:
        survey_name = basename.replace(' ', '_')
    output_path = os.path.join(output_dir, f"expanded_aspects_{survey_name}.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {output_path}")

def expand_field_of_study(survey_field_of_study: str, input_base_dir: str = "Human_json_cleaned_v3", n: int = 3) -> dict:
    """
    Expand the field of study into detailed criteria.
    
    Args:
        survey_field_of_study: Field of study string
        input_base_dir: Base directory containing the JSON files (default: "Human_json_cleaned_v3")
        n: Number of criteria to expand into
    """
    dir_name = os.path.join(input_base_dir, survey_field_of_study)
    output_dir = f"outputs/criteria/{survey_field_of_study}"
    if not os.path.exists(dir_name):
        print(f"Directory not found: {dir_name}")
        return None
    results = None
    for file in os.listdir(dir_name):
        if file.endswith("_split.json") or file.endswith(".json"):
            survey_json_path = os.path.join(dir_name, file)
            print(f"Expanding survey: {survey_json_path}")
            results = expand_with_survey(survey_json_path, n)
            save_results(results, survey_json_path, output_dir)
    return results

if __name__ == "__main__":
    # Example usage
    # survey_field_of_study = "Biology"
    # expand_field_of_study(survey_field_of_study, input_base_dir="Human_json_cleaned_v3", n=3)
    survey_field_of_study = ["Business", "Computer Science", "Education", "Engineering", "Environmental Science", "Medicine", "Physics", "Psychology", "Sociology"]
    for field_of_study in survey_field_of_study:
        expand_field_of_study(field_of_study, input_base_dir="Human_json_cleaned_v3", n=3)
    