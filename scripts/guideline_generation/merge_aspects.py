import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

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
            temperature=0,
            # extra_body={"reasoning": {"enabled": True}}
        )
        response_text = completion.choices[0].message.content.strip()
        return robust_json_parse(response_text)
    except BadRequestError as e:
        error_msg = str(e)
        if "maximum context length" in error_msg or "tokens" in error_msg.lower():
            # Re-raise token limit error to be handled by caller
            raise
        else:
            print(f"✗ BadRequestError: {error_msg}")
            return None
    except Exception as e:
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

MERGE_ASPECT_CRITERIA_PROMPT = """You are an academic survey expert. Now you are merging multiple expanded criteria from the same aspect across multiple survey papers into a consolidated set.

Given:
1. Aspect Name: {aspect_name}
2. Component Type: {component_name} (outline/content/reference)
3. All Expanded Criteria: A list of criteria from the same aspect "{aspect_name}" collected from multiple survey papers
4. Target Number: {n}

Task:
Merge all the given expanded criteria into {n} comprehensive, consolidated criteria. Each merged criterion should:
- Synthesize related criteria from different survey papers into a unified, coherent criterion
- Preserve the essential meaning and evaluation focus of the original criteria
- Be general enough to apply across different survey papers while remaining specific enough to guide evaluation
- Avoid redundancy while maintaining comprehensiveness
- Each merged criterion should have a clear, distinct focus
- Extract common patterns and best practices from the examples

All Expanded Criteria:
{all_criteria_json}

Please return the result in the following JSON format:
{{
  "aspect_name": "{aspect_name}",
  "component_name": "{component_name}",
  "merged_expanded_criteria": [
    {{
      "criterion_name": "Consolidated criterion name 1",
      "description": "Comprehensive description that synthesizes related criteria",
      "example": "Highly synthesized and aggregated example that demonstrates universally applicable criteria"
    }},
    {{
      "criterion_name": "Consolidated criterion name 2",
      "description": "Comprehensive description that synthesizes related criteria",
      "example": "Highly synthesized and aggregated example that demonstrates universally applicable criteria"
    }},
    ...
  ]
}}

Return only the JSON object, without any markdown code block markers or additional text."""

# ------------------------------------------------------------------------------

def load_all_json_files(folder_path: str) -> list:
    """
    Load all JSON files from a folder.
    
    Args:
        folder_path: Path to folder containing JSON files
        
    Returns:
        list: List of tuples (file_path, data_dict)
    """
    json_files = []
    if not os.path.exists(folder_path):
        print(f"Warning: Folder {folder_path} does not exist")
        return json_files
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.json') and filename.startswith('expanded_aspects_'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    json_files.append((file_path, data))
                    print(f"Loaded: {filename}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    return json_files

def extract_aspect_criteria_from_all_files(json_files: list, aspect_name: str, component_name: str = None) -> list:
    """
    Extract all criteria for a specific aspect from all JSON files.
    
    Args:
        json_files: List of tuples (file_path, data_dict)
        aspect_name: Name of the aspect to extract
        component_name: Optional component name to filter (if None, searches all components)
        
    Returns:
        list: List of all criteria for the specified aspect
    """
    all_criteria = []
    
    for file_path, data in json_files:
        # Search through all components
        for comp_name, aspect_list in data.items():
            # If component_name is specified, skip other components
            if component_name and comp_name != component_name:
                continue
            
            # Find the aspect
            for aspect_dict in aspect_list:
                if aspect_dict.get("aspect_name") == aspect_name:
                    expanded_criteria = aspect_dict.get("expanded_criteria", [])
                    # Add source file context to each criterion
                    for criterion in expanded_criteria:
                        criterion_with_context = {
                            "source_file": os.path.basename(file_path),
                            "component_name": comp_name,
                            **criterion
                        }
                        all_criteria.append(criterion_with_context)
                    break
    
    return all_criteria

def merge_aspect_criteria(aspect_name: str, component_name: str, all_criteria: list, n: int) -> dict:
    """
    Merge all criteria for a specific aspect into n consolidated criteria using LLM.
    
    Args:
        aspect_name: Name of the aspect
        component_name: Component name (outline/content/reference)
        all_criteria: List of all criteria for this aspect
        n: Target number of merged criteria
        
    Returns:
        dict: Merged criteria result
    """
    # Format all criteria as JSON string
    all_criteria_json = json.dumps(all_criteria, indent=2, ensure_ascii=False)
    
    # Format prompt
    prompt = MERGE_ASPECT_CRITERIA_PROMPT.format(
        aspect_name=aspect_name,
        component_name=component_name,
        all_criteria_json=all_criteria_json,
        n=n
    )
    
    # Call LLM
    response = generate_response(prompt)
    
    return response

def merge_aspect_from_folder(folder_path: str, aspect_name: str, component_name: str = None, n: int = 5) -> dict:
    """
    Merge criteria for a specific aspect from all JSON files in a folder.
    
    Args:
        folder_path: Path to folder containing expanded_aspects JSON files
        aspect_name: Name of the aspect to merge (e.g., "Substantive Integrity")
        component_name: Optional component name to filter (if None, searches all components)
        n: Target number of merged criteria
        
    Returns:
        dict: Merged criteria result
    """
    # Load all JSON files
    print(f"Loading JSON files from folder: {folder_path}")
    json_files = load_all_json_files(folder_path)
    
    if not json_files:
        print("No JSON files found!")
        return None
    
    print(f"Found {len(json_files)} JSON files")
    
    # Extract all criteria for the specified aspect
    print(f"\nExtracting criteria for aspect: '{aspect_name}'")
    if component_name:
        print(f"Filtering by component: '{component_name}'")
    else:
        print("Searching across all components")
    
    all_criteria = extract_aspect_criteria_from_all_files(json_files, aspect_name, component_name)
    
    if not all_criteria:
        print(f"No criteria found for aspect '{aspect_name}'")
        return None
    
    print(f"Found {len(all_criteria)} criteria from {len(json_files)} files")
    
    # Determine component name if not specified
    if not component_name:
        # Get the most common component name from criteria
        component_counts = {}
        for criterion in all_criteria:
            comp = criterion.get("component_name", "unknown")
            component_counts[comp] = component_counts.get(comp, 0) + 1
        component_name = max(component_counts.items(), key=lambda x: x[1])[0]
        print(f"Using component: '{component_name}' (most common)")
    
    # Merge criteria
    print(f"\n{'='*80}")
    print(f"Merging criteria for aspect: '{aspect_name}'")
    print(f"Component: '{component_name}'")
    print(f"Total criteria to merge: {len(all_criteria)}")
    print(f"Target merged criteria: {n}")
    print(f"{'='*80}")
    
    merged = merge_aspect_criteria(aspect_name, component_name, all_criteria, n)
    
    if merged:
        merged_criteria = merged.get("merged_expanded_criteria", [])
        print(f"✓ Successfully merged into {len(merged_criteria)} criteria")
        return merged
    else:
        print(f"✗ Failed to merge criteria")
        return None

def discover_all_aspects(json_files: list) -> dict:
    """
    Discover all aspects from JSON files, grouped by component.
    
    Args:
        json_files: List of tuples (file_path, data_dict)
        
    Returns:
        dict: Dictionary mapping component_name to set of aspect names
    """
    aspects_by_component = {}
    
    for file_path, data in json_files:
        for component_name, aspect_list in data.items():
            if component_name not in aspects_by_component:
                aspects_by_component[component_name] = set()
            
            for aspect_dict in aspect_list:
                aspect_name = aspect_dict.get("aspect_name")
                if aspect_name:
                    aspects_by_component[component_name].add(aspect_name)
    
    return aspects_by_component

def merge_all_aspects_from_folder(folder_path: str, n: int = 5, output_dir: str = None):
    """
    Merge all aspects from all JSON files in a folder.
    For each component and each aspect, merge criteria from all files.
    Save all results to a single JSON file in the same format as input files.
    
    Args:
        folder_path: Path to folder containing expanded_aspects JSON files
        n: Target number of merged criteria per aspect
        output_dir: Output directory path (defaults to folder_path)
    """
    if output_dir is None:
        output_dir = folder_path
    
    # Load all JSON files
    print(f"Loading JSON files from folder: {folder_path}")
    json_files = load_all_json_files(folder_path)
    
    if not json_files:
        print("No JSON files found!")
        return
    
    print(f"Found {len(json_files)} JSON files")
    
    # Discover all aspects
    print("\nDiscovering all aspects...")
    aspects_by_component = discover_all_aspects(json_files)
    
    for component_name, aspect_set in aspects_by_component.items():
        print(f"  {component_name}: {len(aspect_set)} aspects")
        for aspect_name in sorted(aspect_set):
            print(f"    - {aspect_name}")
    
    # Merge each aspect and collect results
    total_aspects = sum(len(aspect_set) for aspect_set in aspects_by_component.values())
    print(f"\n{'='*80}")
    print(f"Processing {total_aspects} aspects across {len(aspects_by_component)} components")
    print(f"{'='*80}\n")
    
    # Initialize result structure matching the original JSON format
    merged_results = {}
    for component_name in aspects_by_component.keys():
        merged_results[component_name] = []
    
    # Merge each aspect and append to results
    for component_name, aspect_set in aspects_by_component.items():
        for aspect_name in sorted(aspect_set):
            merged_result = merge_aspect_from_folder(
                folder_path=folder_path,
                aspect_name=aspect_name,
                component_name=component_name,
                n=n
            )
            
            if merged_result:
                # Convert merged result to the same format as input files
                aspect_entry = {
                    "aspect_name": merged_result.get("aspect_name", aspect_name),
                    "expanded_criteria": merged_result.get("merged_expanded_criteria", [])
                }
                merged_results[component_name].append(aspect_entry)
                print(f"✓ Added merged criteria for {component_name} - {aspect_name}")
            else:
                print(f"⚠ Skipping failed merge: {component_name} - {aspect_name}")
            
            print()  # Empty line between aspects
    
    # Save all results to a single file
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "merged_aspects.json")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*80}")
    print(f"All merged results saved to: {output_path}")
    print(f"{'='*80}")

if __name__ == "__main__":
    # survey_field_of_study = "Biology"
    # folder_path = f"outputs/criteria/{survey_field_of_study}"
    # merge_all_aspects_from_folder(folder_path, n=5)
    survey_field_of_study = ["Business", "Computer Science", "Education", "Engineering", "Environmental Science", "Medicine", "Physics", "Psychology", "Sociology"]
    for field_of_study in survey_field_of_study:
        folder_path = f"outputs/criteria/{field_of_study}"
        merge_all_aspects_from_folder(folder_path, n=5)