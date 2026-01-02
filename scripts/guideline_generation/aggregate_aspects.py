outline = [
    {"Coverage": "comprehensively covers key aspects and representative directions of the topic"},
    {"Relevance": "maintains topical alignment without off-topic sections"},
    {"Structure": "reflects a clear and logical hierarchy among sections"},
    {"Structural Organization": "adherence to field-appropriate schemas (e.g., IMRaD, chronological development, method-based taxonomy) that support clear information localization and rapid retrieval."},
    {"Content Value": "inclusion of meaningful scholarly elements such as research gaps, conceptual frameworks, synthesized trends, limitations, and future directions, instead of simple enumeration."},
    {"Descriptiveness": "use of precise and concise section titles that correctly reflect scope and entities while avoiding vague or overly broad phrasing."},
    {"Topic Uniqueness": "- No duplicate topics across sections/subsections\n- Each section contains unique content\n- No redundant future/conclusion sections\n- Clear distinction between related topics"},
    {"Structural Balance": "- Reasonably balanced number of subsections across main content chapters\n- No obviously under-developed sections\n- No overly detailed sections that dominate the outline\n- Variations in subsection numbers should align with topic importance/complexity"},
    {"Hierarchical": "- Clear parent-child relationships\n- Appropriate topic levels for each section's role\n- Logical subdivision aligned with academic conventions\n- Consistent granularity where appropriate"},
    {"Logical Organization": "- Natural topic progression following academic norms\n- Clear relationships between sections\n- Coherent topic grouping\n- Purposeful content flow matching section functions"}
]

content = [
    {"Coverage": "Assesses the extent to which the survey encapsulates all aspects of the topic"},
    {"Relevance": "Measures how well the content aligns with the research topic."},
    {"Structure": "Evaluates the logical organization and coherence of each section."},
    {"Synthesis": "evaluates the ability to interconnect disparate studies, identify overarching patterns or contradictions, and construct a cohesive intellectual framework beyond individual summaries"},
    {"Critical Analysis": "examines the depth of critique applied to existing studies, including the identification of methodological limitations, theoretical inconsistencies, and research gaps"},
    {"Language": "The assessment of academic formality, clarity, and the avoidance of redundancy in the survey. This metric evaluates the overall quality of writing, ensuring the language is clear, concise, and appropriate for an academic audience"},
    {"Criticalness": "The extent to which the survey demonstrates critical analysis, provides original insights and identifies future research directions. This metric evaluates how well the survey goes beyond summarizing existing work, offering thoughtful critiques and highlighting gaps, challenges, or opportunities for further investigation"},
    {"Relevance": "The degree to which the content aligns with the research topic, assessing how well the content stays focused on the required research question"},
    {"Synthesis Quality": "- Measure synthesis ratio (integrated vs sequential)\n- Identify cross-paper connections\n- Evaluate comparative analysis depth"},
    {"Organization": "- Assess section/subsection hierarchy\n- Evaluate transition quality\n- Check information progression logic"},
    {"Readability": "- Sentence complexity and variety\n- Technical term introduction/explanation\n- Paragraph coherence"},
    {"Academic Rigor": "- Citation format consistency\n- Methodological transparency\n- Limitation acknowledgment"},
    {"Clarity": "- Concept explanation quality\n- Ambiguity identification\n- Example usage effectiveness"},
    {"Coherence": "- Thematic consistency\n- Cross-reference accuracy\n- Narrative flow maintenance"},
    {"Comprehensiveness": "- Cluster representation completeness\n- Temporal coverage (publication years)\n- Geographic/institutional diversity"},
    {"Critical Analysis": "- Limitation discussion depth\n- Conflicting findings acknowledgment\n- Methodological critique presence"},
    {"Novelty&Insights": "- Novel connections identified\n- Pattern recognition quality\n- Taxonomy/framework contributions"},
    {"Future Directions": "- Specificity of proposed directions\n- Feasibility assessment\n- Gap identification quality"},
    {"Veracity": "evaluating the clear separation of facts, opinions, and hypotheses and the precision/temperance of terminology with evidence-backed assertions;"},
    {"Originality Proportion": "assessing the proportion and quality of original contributions (e.g., novel taxonomies, critical insights, and forward-looking directions) beyond mere aggregation;"},
    {"Depth of Content": "measuring logical depth and structured synthesis that distinguish shallow collection from well-organized, reasoned analysis."},
    {"Coverage": "includes key subtopics and representative works"},
    {"Depth of Content": "offers meaningful analysis and synthesis, such as identifying research gaps or future directions"},
    {"Focus": "stays centered on its assigned theme"},
    {"Coherence": "presents ideas in a logically connected and well-structured manner"},
    {"Fluency": "is fluent and grammatically natural"}
]

reference = [
    {"Citation Coverage": "- Calculate exact percentage of corpus cited\n- Assess distribution across clusters\n- Check for key papers inclusion"},
    {"Accuracy": "- Verify claims are properly supported\n- Check author/year attribution accuracy\n- Identify any unsupported generalizations"},
    {"Reference Relevance": "Reference relevance evaluates whether the references listed in the References section are closely related to the survey's topic. A high-quality References section should primarily include publications, articles, or works that are directly relevant to the subject matter. The score depends on the proportion of irrelevant or tangential entries as identified by the model. Additionally, the formatting of the references should adhere to standard citation guidelines (e.g., APA, MLA, Chicago), ensuring consistency, accuracy, and completeness. Poor formatting, missing information, or inconsistencies in style will negatively impact the score."}
]

from openai import OpenAI
import json
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  base_url=os.environ.get("BASE_URL"),
  api_key=os.environ.get("API_KEY"),
)


def aggregate_aspects(target_counts):
    """
    Aggregate aspects to specified counts
    
    Args:
        target_counts: Tuple in format (outline_count, content_count, reference_count)
        For example, (3, 5, 3) means aggregate outline to 3, content to 5, reference to 3
    
    Returns:
        Dictionary containing aggregated outline, content, and reference
    """
    outline_count, content_count, reference_count = target_counts
    
    def format_aspects_list(aspects_list):
        """Format aspects list to string"""
        formatted = []
        for i, aspect_dict in enumerate(aspects_list, 1):
            for key, value in aspect_dict.items():
                formatted.append(f"{i}. {key}: {value}")
        return "\n".join(formatted)
    
    def call_llm_for_aggregation(category_name, aspects_list, target_count):
        """Call LLM to aggregate aspects"""
        formatted_aspects = format_aspects_list(aspects_list)
        
        prompt = f"""You are an academic evaluation expert. I need you to aggregate the following evaluation criteria for {category_name} into {target_count} universal, highly aggregated aspects.

        Current aspects list:
        {formatted_aspects}

        Requirements:
        1. Aggregate these {len(aspects_list)} aspects into {target_count} universal aspects
        2. Each aggregated aspect should:
        - Be a highly abstract, universal concept
        - Cover multiple related original aspects
        - Have a concise and generalizable name
        - Have clear descriptions that reflect its universal nature
        3. Maintain academic rigor, ensuring the aggregated aspects comprehensively cover the core content of the original aspects
        4. The number of returned aspects must be exactly {target_count}

        Please return the result strictly in the following JSON array format, without any additional text:
        [
        {{"Aspect Name 1": "Detailed description 1"}},
        {{"Aspect Name 2": "Detailed description 2"}},
        ...
        ]

        Return only the JSON array, without any markdown code block markers or other text."""
        
        completion = client.chat.completions.create(
            model="google/gemini-3-pro-preview",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            extra_body={"reasoning":{"enabled":True}}
        )
        
        response_text = completion.choices[0].message.content.strip()
        
        # Try to parse JSON response
        try:
            # Try to find JSON array part (may be in code blocks or other text)
            start_idx = response_text.find('[')
            end_idx = response_text.rfind(']') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = response_text[start_idx:end_idx]
                response_json = json.loads(json_str)
                
                # Ensure return is in list format
                if isinstance(response_json, list):
                    return response_json
                elif isinstance(response_json, dict):
                    # If it's an object, try to extract array
                    for key in ['aspects', 'result', 'data', 'output']:
                        if key in response_json and isinstance(response_json[key], list):
                            return response_json[key]
                    # If not found, convert object to list
                    return [response_json]
                else:
                    return []
            else:
                # If array not found, try to parse entire response directly
                response_json = json.loads(response_text)
                if isinstance(response_json, list):
                    return response_json
                elif isinstance(response_json, dict):
                    for key in ['aspects', 'result', 'data', 'output']:
                        if key in response_json and isinstance(response_json[key], list):
                            return response_json[key]
                    return [response_json]
                return []
        except json.JSONDecodeError as e:
            # If parsing fails, print error message
            print(f"Warning: Failed to parse JSON response for {category_name}")
            print(f"Error: {e}")
            print(f"Response: {response_text[:500]}...")  # Only print first 500 characters
            return []
    
    # Aggregate outline
    print(f"\nAggregating outline: {len(outline)} aspects -> {outline_count} aspects...")
    aggregated_outline = call_llm_for_aggregation("outline", outline, outline_count)
    if len(aggregated_outline) != outline_count:
        print(f"Warning: outline returned {len(aggregated_outline)} aspects, expected {outline_count}")
    
    # Aggregate content
    print(f"Aggregating content: {len(content)} aspects -> {content_count} aspects...")
    aggregated_content = call_llm_for_aggregation("content", content, content_count)
    if len(aggregated_content) != content_count:
        print(f"Warning: content returned {len(aggregated_content)} aspects, expected {content_count}")
    
    # Aggregate reference
    print(f"Aggregating reference: {len(reference)} aspects -> {reference_count} aspects...")
    aggregated_reference = call_llm_for_aggregation("reference", reference, reference_count)
    if len(aggregated_reference) != reference_count:
        print(f"Warning: reference returned {len(aggregated_reference)} aspects, expected {reference_count}")
    
    result = {
        "outline": aggregated_outline,
        "content": aggregated_content,
        "reference": aggregated_reference
    }
    
    return result


def print_aggregated_aspects(result):
    """Print aggregated aspects"""
    print("\n" + "="*80)
    print("Aggregated Aspects Results")
    print("="*80)
    
    for category, aspects_list in result.items():
        print(f"\n[{category.upper()}] ({len(aspects_list)} aspects):")
        print("-" * 80)
        for i, aspect_dict in enumerate(aspects_list, 1):
            for key, value in aspect_dict.items():
                print(f"{i}. {key}")
                print(f"   {value}")
                print()


# Main function
if __name__ == "__main__":
    # Example: aggregate outline to 3, content to 5, reference to 3
    target_counts = (3, 5, 3)
    
    print(f"Target aggregation counts: outline={target_counts[0]}, content={target_counts[1]}, reference={target_counts[2]}")
    
    result = aggregate_aspects(target_counts)
    print_aggregated_aspects(result)
    
    # Save results to JSON file
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_filename = f"aggregated_aspects_{target_counts[0]}_{target_counts[1]}_{target_counts[2]}.json"
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"\nResults saved to: {output_path}")
