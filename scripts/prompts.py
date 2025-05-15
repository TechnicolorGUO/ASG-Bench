# ---------------- Dataset Prompts --------------

EXPAND_CATEGORY_TO_TOPICS = '''
Given the category "{category}", your task is to expand it into {num_topics} representative and highly general survey topics. Each topic should be suitable as the main subject of a comprehensive academic survey paper, expressed as a short phrase or noun clause (not a full sentence), accurately reflecting the scope and context of the topic within the given category.

Rules:
1. The topics must be highly general, each covering a major subfield, trend, or research area within the given category.
2. All topics together should aim to comprehensively cover the breadth of the category, minimizing significant overlap.
3. Use concise and academic language. The topics should be suitable for use as section headings or survey titles in an academic context.
4. If the category is broad (e.g., "Computer Science"), ensure the topics represent its most important and distinct research directions.
5. If the category is specific (e.g., "Artificial Intelligence"), focus on the key subfields, major approaches, or emerging trends within that subdomain.
6. Do not include introductory or overly generic topics such as "Computer Science" or "Artificial Intelligence".
7. For each topic, provide a short (1-2 sentence) description explaining what the topic covers.

Output format:
Please output the result as a JSON object. The key of each entry should be the topic (e.g., "Deep Learning for Computer Vision"), and the value should be the corresponding description.

Here is a placeholder example for the required format:
{{
  "Topic 1": "Description 1",
  "Topic 2": "Description 2"
}}

Here is a single real example for the category "Artificial Intelligence" with 1 topic:
{{
  "Deep Learning for Computer Vision": "This topic covers the development, architectures, and applications of deep learning in computer vision, including image recognition, object detection, and generative models."
}}

Here is the information for the task:
Category: {category}
Number of topics: {num_topics}
'''

CATEGORIZE_SURVEY_TITLES = '''
You are given a list of academic survey papers, each with its title and arXiv id:

{survey_titles}

Your task is to cluster these papers into {num_clusters} coherent and meaningful groups based on their topics or research areas.

For each cluster, provide:
- A concise, academic topic label (as the key)
- A list of the survey papers that belong to this cluster (as the value), where each paper is represented by its title and arXiv id in the same dictionary format as above.

Guidelines:
1. The topic label should accurately summarize the main theme or field covered by the papers in the cluster.
2. Papers in the same cluster should be closely related in content or research area.
3. The clusters should be distinct from each other and cover all the provided papers.
4. Do not create overlapping clusters. Each paper should belong to only one cluster.
5. Output the result as a valid JSON object, with the topic label as the key and a list of corresponding paper dicts as the value.

Output format example:
{{
  "Topic Label 1": [
    {{"title": "Survey Title A", "arxiv_id": "xxxx.xxxxx"}},
    {{"title": "Survey Title B", "arxiv_id": "yyyy.yyyyy"}}
  ],
  "Topic Label 2": [
    {{"title": "Survey Title C", "arxiv_id": "zzzz.zzzzz"}}
  ]
}}
You are not allowed to include topic labels like "Other Advanced Topics in xxx" in your output and every cluster should have a meaningful label.
Now, please return your clustering result for the provided survey papers without any other information.
'''

CATEGORIZE_SURVEY_TITLES_HEURISTIC = '''

You are given a list of academic survey papers, each with its title and arXiv id:

{survey_titles}

Your task is to cluster these papers into coherent and meaningful groups based on their topics or research areas. The number of clusters is not fixed—please determine the most natural and informative grouping based on the papers' content.

For each cluster, provide:
- A concise, academic topic label (as the key)
- A list of the survey papers that belong to this cluster (as the value), where each paper is represented by its title and arXiv id in the same dictionary format as above.

Guidelines:
1. The topic label should accurately and specifically summarize the main theme or field covered by the papers in the cluster.
2. Papers in the same cluster should be closely related in content or research area.
3. The clusters should be distinct from each other and cover all the provided papers.
4. Do not create overlapping clusters. Each paper should belong to only one cluster.
5. Do not use vague or catch-all labels like "Other Topics" or "Miscellaneous". Every cluster should have a meaningful, content-based label.
6. The number of clusters should be determined by the actual topical diversity among the papers.

Output the result as a valid JSON object, with the topic label as the key and a list of corresponding paper dicts as the value.

Output format example:
{{
  "Topic Label 1": [
    {{"title": "Survey Title A", "arxiv_id": "xxxx.xxxxx"}},
    {{"title": "Survey Title B", "arxiv_id": "yyyy.yyyyy"}}
  ],
  "Topic Label 2": [
    {{"title": "Survey Title C", "arxiv_id": "zzzz.zzzzz"}}
  ]
}}
Return only the JSON object as your answer, with no additional explanation.
'''

CATEGORIZE_SURVEY_TITLES_SINGLE = '''
You are given a list of academic survey papers, each with its title and arXiv id:

{survey_titles}

Your task is to assign each survey paper to its own unique cluster, such that every cluster contains exactly one paper. For each cluster, generate a concise, academic topic label that accurately summarizes the main theme or research area of that individual paper.

Guidelines:
1. Each cluster must contain exactly one paper.
2. The topic label for each cluster should be specific, informative, and closely reflect the core topic of the corresponding survey paper.
3. Avoid vague or generic labels; every label should meaningfully represent the paper's content.
4. The output should be a valid JSON object, where each key is the topic label and the value is a list containing the dictionary for that paper (with title and arXiv id).

Output format example:
{{
  "Topic Label for Paper 1": [
    {{"title": "Survey Title A", "arxiv_id": "xxxx.xxxxx"}}
  ],
  "Topic Label for Paper 2": [
    {{"title": "Survey Title B", "arxiv_id": "yyyy.yyyyy"}}
  ]
}}

Return only the JSON object as your answer, with no additional explanation.
'''

# -------------- Evaluation Prompts --------------

CRITERIA = {
    'Coverage': {
        'description': 'Coverage assesses the extent to which the survey encapsulates all relevant aspects of the topic, ensuring comprehensive discussion on both central and peripheral topics.',
        'score 1': 'The survey has very limited coverage, only touching on a small portion of the topic and lacking discussion on key areas.',
        'score 2': 'The survey covers some parts of the topic but has noticeable omissions, with significant areas either underrepresented or missing.',
        'score 3': 'The survey is generally comprehensive in coverage but still misses a few key points that are not fully discussed.',
        'score 4': 'The survey covers most key areas of the topic comprehensively, with only very minor topics left out.',
        'score 5': 'The survey comprehensively covers all key and peripheral topics, providing detailed discussions and extensive information.'
    },
    'Structure': {
        'description': 'Structure evaluates the logical organization and coherence of sections and subsections, ensuring that they are logically connected.',
        'score 1': 'The survey lacks logic, with no clear connections between sections, making it difficult to understand the overall framework.',
        'score 2': 'The survey has weak logical flow with some content arranged in a disordered or unreasonable manner.',
        'score 3': 'The survey has a generally reasonable logical structure, with most content arranged orderly, though some links and transitions could be improved such as repeated subsections.',
        'score 4': 'The survey has good logical consistency, with content well arranged and natural transitions, only slightly rigid in a few parts.',
        'score 5': 'The survey is tightly structured and logically clear, with all sections and content arranged most reasonably, and transitions between adjacent sections smooth without redundancy.'
    },
    'Relevance': {
        'description': 'Relevance measures how well the content of the survey aligns with the research topic and maintains a clear focus.',
        'score 1': 'The content is outdated or unrelated to the field it purports to review, offering no alignment with the topic.',
        'score 2': 'The survey is somewhat on topic but with several digressions; the core subject is evident but not consistently adhered to.',
        'score 3': 'The survey is generally on topic, despite a few unrelated details.',
        'score 4': 'The survey is mostly on topic and focused; the narrative has a consistent relevance to the core subject with infrequent digressions.',
        'score 5': 'The survey is exceptionally focused and entirely on topic; the article is tightly centered on the subject, with every piece of information contributing to a comprehensive understanding of the topic.'
    },
    'Language': {
        'description': 'Language assesses the academic formality, clarity, and correctness of the writing, including grammar, terminology, and tone.',
        'score 1': 'The language is highly informal, contains frequent grammatical errors, imprecise terminology, and numerous colloquial expressions. The writing lacks academic tone and professionalism.',
        'score 2': 'The writing style is somewhat informal, with several grammatical errors or ambiguous expressions. Academic terminology is inconsistently used.',
        'score 3': 'The language is mostly formal and generally clear, with only occasional minor grammatical issues or slightly informal phrasing.',
        'score 4': 'The language is clear, formal, and mostly error-free, with only rare lapses in academic tone or minor imprecisions.',
        'score 5': 'The writing is exemplary in academic formality and clarity, using precise terminology throughout, flawless grammar, and a consistently scholarly tone.'
    },
    'Criticalness': {
        'description': 'Criticalness evaluates the depth of critical analysis, the originality of insights, and the clarity and justification of proposed future research directions.',
        'score 1': 'The survey lacks critical analysis and fails to identify gaps, weaknesses, or areas for improvement. Offers no original insights and does not propose any meaningful future research directions.',
        'score 2': 'The survey provides only superficial critique, with limited identification of weaknesses. Original insights are minimal and future directions are vague or generic.',
        'score 3': 'The survey demonstrates moderate critical analysis, identifying some gaps or weaknesses. Offers some original perspectives and suggests future directions, though they may lack depth or specificity.',
        'score 4': 'The survey presents a strong critique, clearly identifying significant gaps and weaknesses, and proposes well-justified future research directions. Provides some novel insights, though a few aspects could be further developed.',
        'score 5': 'The survey excels in critical analysis, incisively evaluating methodologies, results, and assumptions. Provides highly original insights and proposes clear, actionable, and innovative future research directions, all rigorously justified.'
    },
    'Outline': {
        'description': (
            'Outline evaluates the clarity, logical hierarchy, and organization of the survey structure based on its section titles. '
            'Note: The outline is now provided as a plain list of section titles'
            'Please focus your evaluation on the semantic coherence, logical grouping, and progression reflected by the section titles themselves.'
        ),
        'score 1': 'The outline is chaotic or confusing, with unclear relationships and significant structural gaps. Section titles are vague, repetitive, or lack logical flow.',
        'score 2': 'The outline shows basic attempts at organization but contains multiple misplaced or poorly grouped sections. The progression is unclear or disjointed. Section titles are sometimes ambiguous.',
        'score 3': 'The outline demonstrates a generally reasonable structure, with some minor misalignments or grouping issues. Most section titles are clear, and topic coverage is mostly logical.',
        'score 4': 'The outline is well-structured, with clearly grouped section titles and a coherent progression of topics. Minor issues may exist but do not significantly affect readability or understanding.',
        'score 5': 'The outline is exceptionally clear, logically organized, and easy to follow. Section titles are concise and informative, and the structure fully represents the topic\'s breadth and depth.'
    },
    'Reference': {
        "description": (
            "Reference relevance evaluates whether the references listed in the References section are closely related to the survey's topic. "
            "A high-quality References section should primarily include publications, articles, or works that are directly relevant to the subject matter. "
            "The score depends on the proportion of irrelevant or tangential entries as identified by the model."
        ),
        "score 1": "Most references (over 60%) are irrelevant or only marginally related to the topic.",
        "score 2": "A significant portion (40-60%) of references are not closely related to the topic.",
        "score 3": "Some references (20-40%) are not relevant to the topic, but the majority are appropriate.",
        "score 4": "A small number (5-20%) of references are not well aligned, but most are relevant.",
        "score 5": "Nearly all references (over 95%) are relevant and directly related to the topic."
    }
}

CONTENT_EVALUATION_PROMPT = """
Here is an academic survey about the topic "{topic}":
---
{content}
---

Please evaluate this survey based on the criterion provided below, and give a score from 1 to 5 according to the score description:
---
Criterion Description: {criterion_description}
---
Score 1 Description: {score_1}
Score 2 Description: {score_2}
Score 3 Description: {score_3}
Score 4 Description: {score_4}
Score 5 Description: {score_5}
---
Return your answer only in JSON format: {{"{criteria_name}": <score>}} without any other information or explanation.
"""

CONTENT_EVALUATION_SIMULTANEOUS_PROMPT = """
Here is an academic survey about the topic "{topic}":
---
{content}
---

Please evaluate this survey based on the following criteria, and give a score from 1 to 5 for each criterion according to their respective score descriptions:

1. Coverage:
Description: {coverage_description}
Score 1: {coverage_score_1}
Score 2: {coverage_score_2}
Score 3: {coverage_score_3}
Score 4: {coverage_score_4}
Score 5: {coverage_score_5}

2. Structure:
Description: {structure_description}
Score 1: {structure_score_1}
Score 2: {structure_score_2}
Score 3: {structure_score_3}
Score 4: {structure_score_4}
Score 5: {structure_score_5}

3. Relevance:
Description: {relevance_description}
Score 1: {relevance_score_1}
Score 2: {relevance_score_2}
Score 3: {relevance_score_3}
Score 4: {relevance_score_4}
Score 5: {relevance_score_5}

4. Language:
Description: {language_description}
Score 1: {language_score_1}
Score 2: {language_score_2}
Score 3: {language_score_3}
Score 4: {language_score_4}
Score 5: {language_score_5}

5. Criticalness:
Description: {criticalness_description}
Score 1: {criticalness_score_1}
Score 2: {criticalness_score_2}
Score 3: {criticalness_score_3}
Score 4: {criticalness_score_4}
Score 5: {criticalness_score_5}

Return your answer only in JSON format:
{{
    "Coverage": <score>,
    "Structure": <score>,
    "Relevance": <score>,
    "Language": <score>,
    "Criticalness": <score>
}}
without any other information or explanation.
"""

CONTENT_FAITHFULNESS_PROMPT = """
You are an academic reviewer. Given the topic, a sentence from a paper, and the full reference list, please perform the following:

1. Carefully examine the sentence and count the number of in-text citation occurrences (for example, [1], [2,3], [Smith et al., 2020], etc.) present in the sentence text.
2. For each in-text citation found in the sentence, judge whether it is actually supported by a reference in the provided reference list, based on the title and abstract of the references.

Please return ONLY a JSON object in the following format:

{{
  "total": <int>,      // total number of in-text citations found in the sentence text.
  "supported": <int>   // number of those citations that are actually supported by the reference list
}}

Input:
Topic: {topic}

Sentence: {sentence}

References:
{references}

Instructions:
- "total": The number of in-text citation occurrences found in the sentence text.
- "supported": The number of these in-text citations that are actually supported by relevant references in the provided list.
- Only output the JSON, nothing else.
"""

OUTLINE_EVALUATION_PROMPT = """
Here is an outline of an academic survey about the topic "{topic}":
---
{outline}
---

The outline is provided as a plain list of section titles.
Please evaluate the outline based on the clarity, logical grouping, and progression implied by the section titles.

Give a score from 1 to 5 according to the criterion descriptions below:
---
Criterion Description: {criterion_description}
---
Score 1 Description: {score_1}
Score 2 Description: {score_2}
Score 3 Description: {score_3}
Score 4 Description: {score_4}
Score 5 Description: {score_5}
---
Return your answer only in JSON format: {{"{criteria_name}": <score>}} without any other information or explanation.
"""

OUTLINE_COVERAGE_PROMPT = """
You are given the outline of an academic survey on the topic "{topic}":

---
{outline}
---

Please match the outline sections (based on their titles or meanings, not exact words) to the following standard academic survey sections. 

A section is considered matched if its title or meaning corresponds to any of the listed templates, even if the wording is not exactly the same.

Here is the checklist of standard sections (with common synonyms):

1. Abstract
2. Introduction / Background
3. Related Work / Literature Review
4. Problem Definition / Scope / Motivation
5. Methods / Methodology / Taxonomy / Approach
6. Comparative Analysis / Discussion
7. Applications / Use Cases
8. Open Problems / Challenges / Future Directions
9. Conclusion / Summary
10. References / Bibliography

Please analyze the outline and return a JSON object in the following format:

{{
  "matched_count": number of sections matched (an integer from 0 to 10)
}}

Only return the JSON object. Do not add any explanation.
"""

OUTLINE_STRUCTURE_PROMPT = """
Given the following outline structure, analyze the relationship between the parent node and each of its direct child nodes:

- Parent node:
  Index: {parent_index}
  Title: {parent_title}

- Direct child nodes:
{children_list}

For each child node, decide whether it is a *necessary and direct subtopic* of the parent node. Mark as "Yes" only if:
- The child topic is essential for fully understanding or representing the parent node,
- It is directly and specifically related to the parent's core subject,
- It cannot stand alone as an independent section without losing relevance,
- It is not a generic or loosely related section (such as reference, acknowledgment, appendix, background, discussion, or future work).

If the child node is only loosely related, optional, or could be attached to many different parent nodes, answer "No".
If you are unsure, answer "No".

Output only the following JSON format, without any explanation:
{{
  "children": [
    {{
      "child_index": "{{child_index}}",
      "child_title": "{{child_title}}",
      "is_included": "Yes"  // or "No"
    }}
  ]
}}
"""

REFERENCE_EVALUATION_PROMPT = """
Below are the references cited at the end of an academic survey about the topic "{topic}":
---
{reference}
---

Please evaluate the relevance of these references based on the criterion provided below, and give a score from 1 to 5 according to the score descriptions. 
Your evaluation should focus on how many references are relevant to the topic, and penalize the inclusion of irrelevant or only tangentially related entries.

---
Criterion Description: {criterion_description}
---
Score 1 Description: {score_1}
Score 2 Description: {score_2}
Score 3 Description: {score_3}
Score 4 Description: {score_4}
Score 5 Description: {score_5}
---
Return your answer only in JSON format: {{"{criteria_name}": <score>}} without any other information or explanation.
"""

REFERENCE_QUALITY_PROMPT = """
You are an academic reviewer. Given the following topic and a list of references, please answer:

Topic: {topic}

References:
{references}

Task:
1. For the references above, count how many are directly related and provide strong support for the topic (i.e., they are highly relevant and authoritative for the topic).
2. Output your answer in JSON format like: {{"total": X, "supported": Y}}
Where "total" is the total number of references, and "supported" is the number of references that strongly support the topic.

Only output the JSON object, nothing else.
"""

# -------------- Generation Prompts --------------
OUTLINE_REFINE_PROMPT = """
You are given an academic paper outline, currently with only level-1 headings.

You are only allowed to:
1. Delete items that are obviously irrelevant or likely artifacts of the outline extraction process (such as empty, meaningless, or non-heading items).
2. Change the hierarchy level of existing items by modifying the first element of each list from 1 to a higher level (such as 2 or 3), if appropriate.

Do not add any new sections or content. Do not group or merge items. Do not change the order of items.

Your output must be the reorganized outline in JSON array format, where each element is [level, title], with level as an int and title as a string, matching the input format exactly.

Only output the JSON array. Do not include any explanation or commentary.

Here is the original outline:
{outline}
"""

OUTLINE_GENERATE_PROMPT = """
You are an expert researcher in scientific writing. Given a topic for a literature survey, generate a detailed and logically organized outline for the survey.

Instructions:
- The outline should be comprehensive, reflecting the typical structure of a scholarly literature survey, and tailored to the given topic.
- Format the outline as a Python list of lists, where each sublist has the form: [level, "Section Title"].
    - level is an integer (1 for main sections, 2 for subsections, 3 for subsubsections).
    - The section title should be concise and academic, e.g., "1 Introduction", "2 Related Work", "2.1 Methods".
- The outline should include standard sections such as Introduction, Background, Main Content (with subtopics), Discussion, and Conclusion, as well as any topic-specific sections.
- The depth of the outline should be exactly 3 levels, e.g., "1.1.1", "2.1.1", "3.1.1".
- Output only the Python list, nothing else.

Example:
If the survey topic is "Attention Mechanisms in Neural Networks", your output should look like:

[[1, "1 Abstract"],
  ...
  ...
 [1, "n Conclusion"]]

Do not include any other text or explanation.

Survey topic: {topic}
"""

CONTENT_GENERATE_BY_OUTLINE_PROMPT = """
You are a scholarly expert in scientific writing.

Given:
- The survey topic: "{topic}"
- The complete outline of the survey: {outline}
- The current section and its subsections to write: {section_group}

Please write the content for this section group as if for a formal literature survey, following these requirements:

Requirements:
- Use Markdown headings: "# " for level 1, "## " for level 2, "### " for level 3, etc., matching the provided section titles and hierarchy.
- Write clear, academic prose, synthesizing key ideas relevant to the topic and each section heading.
- Where mathematical concepts are important, include appropriate mathematical expressions in LaTeX format (enclosed in $...$ or $$...$$).
- If a section would benefit from an explanatory figure or diagram, insert a Markdown image placeholder where appropriate (e.g., ![]()).
- If a section would benefit from a table, insert a Markdown table placeholder where appropriate (e.g., | Column 1 | Column 2 |).
- The length of the content should be similar to a typical section in a literature survey, with sufficient detail to cover the topic comprehensively.
- Return **only** a single-line JSON object with the structure: {{"content": "..."}}, where the value is your generated Markdown content of the **current section**.

Do not output anything except the JSON object.
"""

CONTENT_GENERATE_WITHOUT_OUTLINE_PROMPT = """
You are a scholarly expert in scientific writing.

Given the survey topic: "{topic}"

Write a comprehensive literature survey in Markdown format on this topic, including an appropriate structure (introduction, main sections, conclusion, etc.) as is standard for such surveys.

Requirements:
- Use proper Markdown headings and formatting.
- Write clear, academic prose, synthesizing key ideas relevant to the topic.
- Where mathematical concepts are important, include appropriate mathematical expressions in LaTeX format (enclosed in $...$ or $$...$$).
- If a section would benefit from an explanatory figure or diagram, insert a Markdown image placeholder (e.g., ![]()).
- If a section would benefit from a table, insert a Markdown table placeholder (e.g., | Column 1 | Column 2 |).
- Return **only** a single-line JSON object with the structure: {{"content": "..."}}, where the value is your generated **Markdown** content.

Do not output anything except the JSON object.

"""

# -------------- Domain-specific Criteria --------------

OUTLINE_DOMAIN_CRITERIA = {
    'cs': {
        'description': 'Structure evaluation specific to Computer Science surveys, focusing on technical organization, methodological frameworks, and computational approaches.',
        'score 1': 'Critically Deficient Structure\nThe outline exhibits fundamental structural problems, characterized by:\n- Absence of a coherent taxonomic structure for categorizing CS concepts, methods, or technologies\n- Missing critical technical foundation sections necessary for understanding the domain\n- No logical progression from fundamental concepts to advanced applications\n- Inconsistent or absent methodology classification (e.g., algorithms, approaches, models)\n- Section titles that use ambiguous terminology or non-standard CS vocabulary\n- Complete lack of comparative analysis frameworks or evaluation metrics sections\n- No sections addressing future research directions, challenges, or open problems',
        'score 2': 'Basic But Problematic Organization\nThe outline shows rudimentary organizational attempts but contains significant flaws:\n- Preliminary taxonomic organization with substantial gaps or misalignments\n- Basic technical foundations included but inadequately structured or sequenced\n- Limited delineation between closely related technical approaches or methodologies\n- Inconsistent granularity across sections (some overly detailed, others too broad)\n- Weak integration of theoretical concepts with practical applications\n- Minimal attention to benchmarking frameworks, datasets, or comparative analyses\n- Future research directions mentioned superficially without systematic development',
        'score 3': 'Functional Structure With Minor Issues\nThe outline demonstrates a generally reasonable structure for a CS survey:\n- Functional taxonomic framework that organizes most content logically\n- Adequate technical foundation sections with appropriate prerequisite information\n- Clear distinction between major methodological approaches\n- Reasonable balance between algorithmic details and practical implementations\n- Moderately well-organized sections on evaluation methodologies and metrics\n- Chronological or evolutionary context provided for most key developments\n- Addresses future research directions with moderate depth and specificity',
        'score 4': 'Well-Structured With Comprehensive Coverage\nThe outline is well-structured with clear organization and comprehensive scope:\n- Well-developed taxonomic structure with logical hierarchical relationships\n- Comprehensive technical foundations with appropriate progressive complexity\n- Thoughtful organization by methodology, chronology, and application domains\n- Clear delineation between related approaches with consistent categorization\n- Dedicated sections for benchmarks, evaluation frameworks, and comparative analyses\n- Strong integration of theoretical foundations with practical implementations\n- Well-structured sections on limitations, challenges, and future research directions',
        'score 5': 'Exceptionally Clear and Comprehensive Organization\nThe outline demonstrates exceptional structural quality and domain understanding:\n- Sophisticated taxonomic organization that elegantly represents the field\'s structure\n- Technical foundations that efficiently scaffold understanding for diverse reader expertise levels\n- Seamless integration of methodological, chronological, and application-based organization\n- Precise categorization of technical approaches that illuminates relationships between concepts\n- Multi-dimensional comparative frameworks that enable insightful cross-approach analysis\n- Balanced coverage of historical evolution, current state-of-the-art, and emerging trends\n- Comprehensive treatment of future directions with specific research challenges and opportunities\n- Novel organizational insights that contribute to better understanding of the field\'s structure'
    },
    'econ': {
        'description': 'Structure evaluation specific to Economics surveys, focusing on theoretical frameworks, empirical methodologies, and economic analysis.',
        'score 1': 'Fundamentally Deficient Structure\nThe outline lacks essential components of economics survey papers. No clear distinction between theoretical frameworks and empirical methodologies. Literature review section is missing or fails to categorize relevant economic literature. Economic models (structural, reduced-form, or theoretical) are undefined or absent. No sections addressing identification strategies, causal inference methods (DiD, IV, RDD, RCTs), or econometric specifications. Section titles are vague, non-technical, or fail to reflect standard economic terminology. There is no logical progression between conceptual foundations and applications.',
        'score 2': 'Basic but Problematic Structure\nThe outline contains basic economics paper components but shows significant organizational flaws. Literature review section is present but fails to differentiate between theoretical and empirical contributions. Theoretical and empirical sections are poorly connected or imbalanced. Economic models or analytical frameworks are mentioned but inadequately structured. Methodological approaches lack clear positioning within the outline. Data description sections are disconnected from empirical methodology. Section titles lack precision regarding specific economic concepts, econometric approaches, or theoretical models.',
        'score 3': 'Adequate Structure with Minor Issues\nThe outline follows standard economics paper structure with reasonable organization. Literature review appropriately categorizes previous research but may inadequately address methodological approaches or identification strategies. Economic models and analytical frameworks are identified with basic distinction between different approaches. Data sources and empirical strategies are mentioned with some discussion of identification challenges. Most sections logically follow economics discourse conventions, though connections between theoretical foundations and empirical applications could be strengthened. Section titles generally reflect economic concepts though some may lack specificity.',
        'score 4': 'Well-Structured with Clear Organization\nThe outline demonstrates strong organizational logic with clear progression from theoretical foundations through methodological approaches to empirical analysis and policy implications. Literature review effectively synthesizes relevant economic literature, distinguishing between theoretical and empirical contributions while identifying research gaps. Section titles precisely reflect economic models, causal inference approaches, and analytical frameworks. The outline shows appropriate balance between conceptual development and empirical applications, with well-defined identification strategies and data sources. Sections addressing limitations, policy implications, and future research directions are properly positioned in the structure.',
        'score 5': 'Exemplary Structure with Sophisticated Organization\nThe outline exemplifies exceptional clarity and sophisticated structure ideal for economics survey papers. Literature review systematically organizes the evolution of economic thought on the topic, critically evaluating competing theoretical models and empirical methodologies. Section titles demonstrate precise economic terminology and reflect a nuanced understanding of theoretical models, identification strategies, and econometric specifications. The outline shows sophisticated integration of theoretical foundations and empirical applications, with clearly articulated sections addressing identification challenges, heterogeneous effects, and robustness considerations. Policy implications, welfare analysis, and research limitations are strategically positioned within the outline structure. The organization reflects deep understanding of both theoretical and empirical economics discourse traditions.'
    },
    'eess': {
        'description': 'Structure evaluation specific to EESS surveys, focusing on technical frameworks, system architectures, and engineering methodologies.',
        'score 1': 'Technically Insufficient and Poorly Structured\nThe outline lacks essential EESS terminology with vague or imprecise section titles. No coherent taxonomy exists for classifying technologies or methodological approaches. Critical components are missing (mathematical frameworks, algorithmic approaches, system architectures). Implementation aspects, evaluation metrics, and practical applications are absent or severely underrepresented. No historical context or future research directions are provided.',
        'score 2': 'Basic Technical Structure with Significant Gaps\nThe outline uses elementary EESS terminology but with inconsistent technical precision. Classification attempts show significant organizational flaws with improper grouping of theoretical concepts and implementation methods. Methodological coverage is unbalanced with disproportionate attention to certain subfields. System implementations, evaluation frameworks, and benchmark comparisons receive minimal attention. Historical development and future challenges are mentioned but lack substantive technical depth.',
        'score 3': 'Technically Adequate with Minor Structural Issues\nThe outline employs appropriate EESS technical terminology in most sections. The structure presents a reasonable organization of theoretical foundations, methodologies, and applications with some minor hierarchical inconsistencies. Major technical approaches are covered, including mathematical formulations and algorithmic frameworks. Basic implementation details, evaluation metrics, and performance parameters are included. The outline provides chronological context and identifies some future research directions, though with limited technical specificity.',
        'score 4': 'Strong Technical Structure with Comprehensive Coverage\nThe outline demonstrates precise EESS terminology throughout with clear technical distinctions between related concepts. The classification system effectively categorizes theoretical foundations, methodological approaches, implementation techniques, and application domains with logical progression. Comprehensive coverage of mathematical frameworks, algorithms, and system designs is provided with appropriate technical depth. Detailed treatment of implementation parameters, evaluation metrics, and comparative analyses across methodologies. Both historical development and future research directions are well-addressed with specific technical challenges identified.',
        'score 5': 'Exceptional Technical Organization with Domain Expertise\nThe outline exhibits expert-level EESS terminology with technically precise section titles that clearly delineate specialized subdomains. The structure provides an exceptional taxonomy that systematically organizes theoretical principles, mathematical frameworks, algorithmic approaches, implementation considerations, and application areas. The progression between sections creates natural connections between foundational concepts and advanced techniques. System parameters, performance metrics, and benchmark frameworks are thoroughly addressed with specific technical indicators. Historical development traces the evolution of key technical advances with appropriate chronology, and future directions identify specific research challenges with substantive technical insights and emerging interdisciplinary connections.'
    },
    'physics': {
        'description': 'Structure evaluation specific to Physics surveys, focusing on theoretical foundations, mathematical frameworks, and experimental evidence.',
        'score 1': 'Fundamentally Flawed Structure\nThe outline lacks essential physics components (theoretical foundations, mathematical framework, experimental evidence) and shows no coherent organization. Section titles are vague, inappropriate, or misuse physics terminology. No clear progression from fundamental principles to applications exists. Mathematical formalism is missing or inappropriately placed. Cross-scale relationships (quantum to classical, micro to macro) are absent when relevant. Connections between theory and experimental/computational methods are missing. Historical development and current research frontiers are disconnected or entirely absent.',
        'score 2': 'Basic but Problematic Organization\nThe outline attempts basic physics organization but contains significant structural flaws. Section titles use physics terminology inconsistently or imprecisely. Topics appear in illogical sequence (e.g., applications before underlying theory, conclusions before methodology). Mathematical formulations appear abruptly without proper context or scaffolding. Experimental and theoretical sections feel disconnected rather than complementary. Computational approaches (when relevant) are inadequately framed. Historical context exists but lacks connection to modern understanding. Multidisciplinary interfaces (physics with chemistry, biology, computer science, etc.) are forced or unclear.',
        'score 3': 'Adequate Physics-Specific Structure\nThe outline demonstrates reasonable physics-specific structure with essential components in a mostly logical order. Progression from fundamental physics principles to applications is generally coherent. Section titles use appropriate physics terminology with occasional imprecision. Mathematical formalism is introduced with basic scaffolding. Theoretical models and experimental evidence are connected, though relationships could be stronger. Computational methods (when relevant) are reasonably positioned. Scale transitions are handled adequately. Historical context is provided with sufficient connections to current understanding. Future directions are identified but may lack depth.',
        'score 4': 'Strong Physics-Appropriate Organization\nThe outline is well-structured with clear physics-specific organization and logical flow. Section titles use precise physics terminology while maintaining clarity. Theoretical foundations, mathematical formalism, and experimental evidence are well-balanced and appropriately sequenced. Mathematical notation builds systematically from basic principles to advanced applications. Computational approaches (when relevant) are well-integrated with theory and experiment. Multidisciplinary connections are meaningfully established. Scale considerations (quantum to classical, micro to macro) are handled competently. Historical development connects to current research questions, and future directions are thoughtfully positioned.',
        'score 5': 'Exemplary Physics Survey Structure\nThe outline exhibits exceptional physics-specific organization with masterful progression from first principles through mathematical frameworks to research frontiers. Section titles demonstrate precise yet accessible physics terminology. Perfect balance and integration of theoretical principles, mathematical formalism, experimental evidence, and computational approaches. Mathematical notation is introduced with expert scaffolding. Multiscale perspectives are elegantly handled when appropriate. Multidisciplinary interfaces are seamlessly integrated. Historical context illuminates the development of current understanding. Open questions and future directions are strategically positioned. The structure clearly reflects both the hierarchical nature of physics knowledge and the interconnections between physics domains.'
    },
    'math': {
        'description': 'Structure evaluation specific to Mathematics surveys, focusing on mathematical coherence, logical progression, and theoretical frameworks.',
        'score 1': 'Fundamentally Deficient Structure\nThe outline lacks mathematical coherence with haphazard organization of topics. Mathematical concepts appear disconnected with no clear progression from foundational to advanced material. Section titles are overly vague or technically imprecise. No apparent logical framework connects different mathematical areas or approaches. The outline fails to establish proper notation conventions or definitional frameworks necessary for the subject matter. Historical context and evolution of mathematical ideas are absent.',
        'score 2': 'Basic Mathematical Organization\nThe outline shows rudimentary attempts at mathematical organization but contains significant structural weaknesses. Some basic mathematical concepts are introduced, but their relationships are poorly articulated. The progression from elementary to complex topics is inconsistent or illogical. Section titles contain mathematical terminology but often lack precision or contain redundancies. Mathematical subfields or approaches are grouped with limited coherence. Theoretical foundations and applications appear imbalanced or disconnected. Limited consideration of notational consistency across sections.',
        'score 3': 'Adequate Mathematical Structure\nThe outline demonstrates a generally reasonable mathematical structure with coherent grouping of related concepts. Most mathematical topics progress logically, though some connections between sections could be strengthened. Section titles are mathematically accurate and reasonably descriptive. The outline includes essential definitions, theorems, and applications in a mostly logical sequence. There is an attempt to balance theoretical foundations with applications, though one may slightly overshadow the other. Historical context is present but may lack depth or integration with technical content. The outline covers most key aspects of the mathematical topic with minor gaps.',
        'score 4': 'Strong Mathematical Framework\nThe outline presents a well-structured mathematical framework with clearly delineated sections that build upon each other. Mathematical concepts progress systematically from foundational principles to advanced topics. Section titles are precise, technically accurate, and effectively convey mathematical content. The outline successfully integrates theoretical foundations with applications and computational aspects where appropriate. Historical development and evolution of mathematical ideas are incorporated meaningfully into the structure. The outline demonstrates thoughtful organization of proofs, theorems, and examples. Different mathematical perspectives or approaches are represented in a balanced manner. The structure facilitates clear connections between related mathematical areas.',
        'score 5': 'Exemplary Mathematical Organization\nThe outline exhibits exceptional mathematical clarity and structural elegance. Mathematical concepts progress with impeccable logical precision from elementary to advanced topics. Section titles are technically precise, mathematically rigorous, and optimally informative. The outline masterfully balances theoretical foundations, computational methods, and applications with clear interconnections. Historical context and evolution of mathematical ideas are seamlessly integrated, enriching the technical structure. Notation and definitional frameworks are established with exceptional clarity and consistency. The outline comprehensively covers the mathematical topic\'s breadth and depth while maintaining focus. Different mathematical perspectives and approaches are presented in optimal balance with clear articulation of their relationships. The structure elegantly facilitates synthesis across mathematical subdisciplines where appropriate.'
    },
    'q-bio': {
        'description': 'Structure evaluation specific to Quantitative Biology surveys, focusing on biological concepts, quantitative methods, and interdisciplinary integration.',
        'score 1': 'Fundamentally Deficient Outline\nThe outline lacks essential elements of quantitative biology integration. Section titles are vague, disconnected, or illogically arranged. There is no clear progression from biological concepts to quantitative methods. The outline fails to address the interdisciplinary nature of the field, with no distinctions between biological scales (molecular, cellular, organismal, etc.). Methodological approaches are chaotically presented without categorization (e.g., statistical analysis, mathematical modeling, computational techniques). Biological data characteristics and challenges are entirely absent. No sections address model validation or experimental verification.',
        'score 2': 'Basic but Problematic Outline\nThe outline shows rudimentary attempts at organizing quantitative biology concepts but contains significant structural issues. Some methodological sections exist but are poorly grouped or inappropriately sequenced. The interdisciplinary integration is superficial, with weak connections between biological mechanisms and mathematical/computational approaches. Biological scales are mentioned but not coherently integrated into the structure. Statistical methods are included but not contextualized for biological data characteristics (high-dimensionality, noise, heterogeneity). Limited coverage of model validation approaches or experimental verification methods. Future directions sections, if present, lack specificity to advancing the field.',
        'score 3': 'Competent Outline with Minor Issues\nThe outline demonstrates reasonable organization of quantitative biology concepts with appropriate methodological groupings. The structure shows adequate progression from fundamental principles to advanced applications. Most biological scales are addressed with some connections between them. Interdisciplinary integration is evident, incorporating biological concepts with mathematical, computational, or physical approaches. Statistical and computational methods are generally well-positioned within the biological context. The outline includes sections on data acquisition, processing, and analysis. Model validation and experimental verification are addressed, though connections between computational predictions and biological reality could be strengthened. Limitations and future directions are present but may lack depth.',
        'score 4': 'Well-Structured and Comprehensive Outline\nThe outline exhibits strong integration of biological concepts with quantitative methods. Section titles clearly communicate content and flow logically. Methodological approaches are well-categorized (e.g., statistical frameworks, mathematical models, computational techniques) and appropriately contextualized within biological frameworks. Multiple biological scales are coherently addressed with clear connections between them. The interdisciplinary nature of quantitative biology is effectively represented through sections bridging biology with mathematics, physics, computer science, or statistics. Data characteristics specific to biological systems (noise, variability, high-dimensionality) are explicitly addressed. Model validation approaches and experimental verification methods are comprehensively covered. The outline includes substantive sections on current limitations, open challenges, and future research directions.',
        'score 5': 'Exceptional and Field-Advancing Outline\nThe outline exemplifies exceptional organization with a perfect balance between biological principles and cutting-edge quantitative approaches. Section titles are precisely formulated and optimally arranged to guide readers through complex interdisciplinary content. Methodological sections are expertly structured, showing sophisticated categorization and sequencing of quantitative techniques. Biological scales are comprehensively addressed with seamless integration across molecular, cellular, tissue, organism, and population levels where appropriate. The outline demonstrates innovative bridging of biology with advanced mathematical, computational, or physical concepts. Data acquisition, processing, and analysis sections reflect state-of-the-art approaches, including considerations of biological data complexity. Model evaluation frameworks incorporate both quantitative performance metrics and biological relevance criteria. The outline includes forward-looking sections that identify paradigm-shifting research directions and emerging methodologies that could transform quantitative biology.'
    },
    'q-fin': {
        'description': 'Structure evaluation specific to Quantitative Finance surveys, focusing on financial models, mathematical frameworks, and market applications.',
        'score 1': 'Fundamentally Deficient\nThe outline shows minimal understanding of quantitative finance survey organization. Mathematical foundations and empirical applications are not differentiated. Financial models and methodologies appear in disjointed sections without logical progression. Core components like literature review, methodology frameworks, or market context are missing. Technical terminology in section titles is inappropriately used or absent. The outline fails to establish connections between theory and practical applications in finance.',
        'score 2': 'Below Standard\nThe outline demonstrates basic attempts at organizing financial concepts but contains significant structural flaws. Theoretical models and empirical applications are inconsistently separated. Limited chronological development of financial methodologies or models is evident. Mathematical foundations appear disconnected from their financial applications. Standard research sections exist but are poorly positioned within the document flow. The outline attempts to use financial terminology in section titles but often does so imprecisely. Important financial contexts (market conditions, regulatory frameworks) are marginally addressed or absent.',
        'score 3': 'Adequate\nThe outline shows a generally reasonable structure with distinct sections for theory, methodology, and application. Most financial concepts progress logically, with foundational elements preceding advanced topics. Mathematical frameworks are adequately connected to their financial contexts. Standard sections (abstract, introduction, literature review, methodology, results, discussion, conclusion) are present in a generally appropriate sequence. Section titles use proper financial terminology that adequately conveys content. The outline includes some discussion of empirical validation and practical implications in financial markets.',
        'score 4': 'Strong\nThe outline exhibits clear organization with well-defined sections that follow the established conventions in quantitative finance literature. Theoretical models and empirical applications are effectively separated yet show clear relationships. Financial methodologies are organized taxonomically, showing evolution and comparative strengths. Mathematical foundations are well-integrated with their financial applications and market contexts. The structure includes comprehensive coverage of data sources, analytical techniques, and validation methods. Section titles effectively use domain-specific terminology and indicate precise content coverage. The outline clearly identifies limitations and potential research extensions.',
        'score 5': 'Exceptional\nThe outline demonstrates superior organization with an optimal structure that enhances comprehension of complex financial concepts. Mathematical foundations, empirical validation, and practical applications are perfectly balanced and integrated. Financial models and methodologies are organized in a sophisticated taxonomy that highlights relationships and evolutionary developments. The structure effectively incorporates historical context, current state-of-the-art practices, and future directions. Interdisciplinary connections to fields like computer science, economics, or data science are clearly articulated where relevant. The outline demonstrates clear awareness of market dynamics, regulatory frameworks, and economic contexts. Section titles use precise technical terminology that expertly conveys content scope and depth.'
    },
    'stat': {
        'description': 'Structure evaluation specific to Statistics surveys, focusing on statistical frameworks, methodological approaches, and analytical techniques.',
        'score 1': 'Fundamentally Flawed Structure\nThe outline lacks a coherent statistical framework, with undefined or improperly categorized statistical concepts. Essential components (data quality assessment, model assumptions, uncertainty quantification) are missing or severely disorganized. Statistical models and techniques appear randomly without logical progression. Statistical terminology is inconsistent or incorrect, and the outline fails to establish connections between theoretical foundations and practical applications. Key methodological sections (e.g., estimation procedures, hypothesis testing frameworks, validation methods) are absent or inappropriately positioned.',
        'score 2': 'Basic but Problematic Organization\nThe outline shows basic attempts at organizing statistical content but contains significant structural deficiencies. Statistical methodology sections exist but are poorly sequenced or inadequately developed. Key components (data description, model specification, parameter estimation, significance testing) lack proper integration or depth. The progression from theoretical statistical foundations to practical applications is unclear or disjointed. Statistical uncertainty quantification and limitations are superficially addressed. The outline presents statistical techniques as isolated entities rather than as an interconnected methodological framework.',
        'score 3': 'Adequate Statistical Structure\nThe outline demonstrates a reasonable structure with appropriate statistical methodology sections. Most statistical concepts follow logical progression, though some connections between related techniques could be strengthened. Data quality assessment and uncertainty quantification are present but may lack comprehensiveness. Statistical models and techniques are mostly well-organized with adequate theoretical justification. Statistical terminology is generally consistent, and the outline provides reasonable coverage of relevant statistical methods, though some specialized techniques may be underrepresented. The balance between theoretical foundations and practical applications is acceptable.',
        'score 4': 'Well-Structured Statistical Framework\nThe outline is well-structured with clearly defined statistical methodology sections and a coherent progression from fundamental concepts to advanced applications. Statistical models and techniques are logically grouped with appropriate connections between related methods. The structure effectively balances theoretical foundations with practical applications and includes comprehensive treatment of data quality, assumptions, and uncertainty quantification. Statistical terminology is precise and consistent throughout, with appropriate coverage of both classical and contemporary statistical methods. The outline effectively contextualizes statistical approaches within the broader research domain and provides clear frameworks for interpretation.',
        'score 5': 'Exemplary Statistical Organization\nThe outline is exceptionally clear and comprehensive, with expertly organized statistical methodology sections. The progression of statistical concepts is perfectly logical, demonstrating mastery of statistical principles and their applications. The outline excels in integrating theoretical statistical foundations with practical applications and includes sophisticated treatment of data quality assessment, uncertainty quantification, and validation methods. Statistical terminology is precise and consistent throughout, with expert handling of both established and emerging statistical concepts. The structure fully represents the breadth and depth of statistical methodology for the topic, with clear connections between related techniques and thoughtful consideration of methodological limitations and future research directions. The outline demonstrates exceptional awareness of statistical best practices and effectively guides readers through complex statistical content.'
    }
}

REFERENCE_DOMAIN_CRITERIA = {
    'cs': {
        'description': 'Reference evaluation specific to Computer Science surveys, focusing on technical relevance, recency, and coverage of key venues.',
        'score 1': 'Deficient Referencing\nCriteria:\n>60% of references lack clear thematic alignment with the survey\'s stated scope (e.g., citing generic machine learning papers in a cybersecurity survey without justifying their relevance).\nOmission of seminal works in the target subfield (e.g., failing to cite ResNet in a deep learning survey).\nOverreliance on outdated sources (>10 years old) without balancing recent advances (2020-2025).\nNo evidence of systematic retrieval (e.g., missing key conferences like NeurIPS, CVPR, or SOSP depending on the domain).',
        'score 2': 'Partial Relevance\nCriteria:\n40-60% of references are weakly connected (e.g., citing broad AI ethics papers in a narrowly focused survey about GPU optimization).\nInconsistent coverage of subfields (e.g., emphasizing convolutional networks but neglecting vision transformers in a computer vision survey).\nLimited engagement with preprint archives (arXiv, SSRN) despite their centrality to CS publishing.\nBiased citation distribution (e.g., >30% of references from a single research group or institution).',
        'score 3': 'Adequate with Gaps\nCriteria:\n20-40% of references lack depth (e.g., citing implementation frameworks without discussing underlying algorithms).\nModerate recency issues: ≥15% of citations predate 2018 in fast-moving areas like LLMs or quantum computing.\nPartial coverage of interdisciplinary links (e.g., citing ML theory but omitting systems papers on deployment challenges).\nInconsistent software/data citation despite their critical role in reproducible CS research.',
        'score 4': 'Strong with Minor Flaws\nCriteria:\n5-20% of citations are non-optimal (e.g., using secondary summaries instead of primary sources for well-established methods).\nComprehensive temporal spread: Balances historical context (20-30%) with recent breakthroughs (50-60% post-2020).\nExplicit methodology for source selection (e.g., snowball sampling from flagship conferences, inclusion/exclusion criteria).\nAcknowledges competing approaches (e.g., cites both PyTorch and JAX ecosystems in ML engineering surveys).',
        'score 5': 'Exemplary Referencing\nCriteria:\n>95% references are domain-critical, including:\n-Seminal papers defining the field\'s trajectory\n-Recent SOTA (last 2-3 years) from premier venues\n-Foundational datasets/benchmarks (e.g., ImageNet, GLUE)\n-Contrastive works illustrating unresolved debates\nMultimodal sourcing: Integrates journal articles (30-40%), conference proceedings (40-50%), and preprints (10-20%) appropriately.\nExplicit citation graphs: Visualizes temporal/thematic relationships between key papers.\nSoftware/data provenance: Cites versioned repositories (GitHub, Hugging Face) and toolkits (TensorFlow, ROS)'
    },
    'econ': {
        'description': 'Reference evaluation specific to Economics surveys, focusing on economic theory, empirical methodology, and journal quality.',
        'score 1': 'Deficient Referencing\nCriteria:\n60% references lack economic relevance (e.g., engineering papers in labor economics survey)\nNo citations to Q1 economics journals\nOmits foundational theorists (Keynes, Friedman, etc.)\nOver 50% sources from non-peer-reviewed platforms',
        'score 2': 'Partial Relevance\nCriteria:\n40-60% references marginally related (e.g., sociology papers without economic theory links)\n<30% citations from Top 50 economics journals\nOnly 1-2 seminal works cited superficially\nRelies heavily on working papers (>40%)',
        'score 3': 'Adequate with Gaps\nCriteria:\n20-40% references lack direct connection to economic mechanisms\n50-70% sources from reputable economics journals\nIdentifies major theories but misses key updates post-2015\nLimited methodological diversity (e.g., only econometric studies)',
        'score 4': 'Strong with Minor Gaps\nCriteria:\n5-20% references lack strong economic framing\n≥80% citations from peer-reviewed economics sources\nCovers 3+ methodological approaches (theoretical/empirical/experimental)\nIncludes recent (≤5 years) studies in evolving fields like behavioral economics',
        'score 5': 'Exemplary Referencing\nCriteria:\n≥95% references demonstrate economic specificity\n30%+ citations from Top 20 economics journals\nTraces theoretical lineage (e.g., cites original Nash paper in game theory surveys)\nBalances classic (pre-2000) and modern (post-2018) sources at 40:60 ratio\nIntegrates interdisciplinary work with explicit economic analysis'
    },
    'eess': {
        'description': 'Reference evaluation specific to EESS surveys, focusing on technical relevance, foundational works, and interdisciplinary connections.',
        'score 1': 'Largely Irrelevant References\nCriteria:\nOver 60% of citations lack clear connection to EE/Systems Science themes\nFails to cite foundational works (e.g., missing key papers on Nyquist stability or Kalman filtering)\nIncludes excessive references to unrelated fields (e.g., citing pure mathematics without EE applications)\nExample deficiency: A survey on power grid optimization citing primarily biomedical signal processing papers',
        'score 2': 'Partially Relevant References\nCriteria:\n40-60% of citations marginally related to EE/Systems Science\nSpotty coverage of major sub-disciplines (e.g., discussing smart grids without citing cybersecurity frameworks)\nLimited engagement with recent advances (≤30% post-2020 citations in fast-moving areas like ML-driven power forecasting)\nExample issue: A review of wireless sensor networks omitting energy harvesting techniques from IoT literature',
        'score 3': 'Mostly Relevant References\nCriteria:\n20-40% of citations lack direct technical alignment\nCovers core theories but misses emerging trends (e.g., includes classical control papers but neglects data-driven control)\nInconsistent balance between seminal works and recent innovations (e.g., cites Shannon\'s 1948 paper but no modern information-theoretic EE applications)\nExample shortcoming: A survey on renewable integration citing grid stability studies but excluding market design papers',
        'score 4': 'Strongly Relevant References\nCriteria:\n5-20% of citations lack optimal relevance\nDemonstrates interdisciplinary awareness (e.g., combines power systems, control theory, and ML in energy management contexts)\nMaintains temporal balance: ≥40% post-2018 citations in rapidly evolving areas like digital twins\nMinor gaps in niche subfields (e.g., covers Li-ion battery models but misses solid-state battery references)',
        'score 5': 'Exemplary References\nCriteria:\nOver 95% of citations directly support EE/Systems Science content\nAchieves four-dimensional coverage:\n-Historical: Seminal works (e.g., Schweppe\'s 1970s energy pricing)\n-Contemporary: Cutting-edge methods (e.g., physics-informed neural networks for grid control)\n-Theoretical: Mathematical foundations (e.g., Lyapunov stability proofs)\n-Applied: Real-world implementations (e.g., IEEE 1547-2018 standard citations)\nMaintains sub-discipline proportionality (e.g., 60% power systems, 30% control theory, 10% signal processing in a smart grid survey)\nIncludes benchmark datasets/codebases where applicable (e.g., GridLAB-D or MATPOWER references)'
    },
    'math': {
        'description': 'Reference evaluation specific to Mathematics surveys, focusing on mathematical relevance, foundational works, and theoretical connections.',
        'score 1': 'Deficient Referencing\nCriteria:\nRelevance: Over 60% of references are tangential to the survey\'s scope (e.g., citing unrelated subfields, outdated preprints, or non-mathematical sources without justification).\nCoverage: Fails to cite seminal works (e.g., foundational theorems, landmark papers) or major advances in the last decade.\nBalance: Heavy reliance on a single research group\'s output or self-citations without contextualizing broader contributions.\nExample: A survey on algebraic geometry that primarily cites computational biology papers or non-peer-reviewed blog posts.',
        'score 2': 'Limited Relevance\nCriteria:\nRelevance: 40-60% of references lack direct connection to the survey\'s focus (e.g., citing peripheral techniques without explaining their relevance).\nCoverage: Omits key historical milestones (e.g., Grothendieck\'s schemes in algebraic geometry) or critical modern developments (e.g., applications of derived categories).\nBalance: Overrepresents one mathematical branch (e.g., differential geometry) while neglecting interrelated areas (e.g., topology or analysis).\nExample: A survey on PDEs that cites numerical methods without addressing existence/uniqueness theory or recent breakthroughs in regularity.',
        'score 3': 'Partial Coherence\nCriteria:\nRelevance: 20-40% of references are marginally useful (e.g., including redundant proofs or minor technical extensions).\nCoverage: Identifies major paradigms but misses influential variants (e.g., citing Hodge theory without mentioning non-Kähler generalizations).\nBalance: Uneven attention to subfields-e.g., emphasizing combinatorial aspects of graph theory while overlooking spectral or probabilistic methods.\nExample: A survey on machine learning theory that cites optimization algorithms but omits PAC-learning frameworks or VC dimension.',
        'score 4': 'Mostly Effective\nCriteria:\nRelevance: 5-20% of references are non-optimal (e.g., citing a weaker result when a stronger theorem exists)\nCoverage: Includes pivotal works and recent advances but misses niche subtopics (e.g., covering Langlands program basics but excluding geometric Langlands).\nBalance: Integrates connections to adjacent fields (e.g., algebraic topology in data science) but lacks depth in interdisciplinary applications.\nExample: A survey on category theory that references Mac Lane and Eilenberg but underrepresents higher category theory or homotopy type theory.',
        'score 5': 'Exemplary Curation\nCriteria:\nRelevance: Over 95% of references directly support the survey\'s narrative, with clear justifications for inclusion.\nCoverage: Exhaustively cites foundational papers (e.g., Weil conjectures), modern breakthroughs (e.g., Scholze\'s perfectoid spaces), and authoritative reviews (e.g., Bourbaki texts).\nBalance: Harmonizes classical results (e.g., Gauss-Bonnet theorem) with contemporary innovations (e.g., Ricci flow in geometric analysis), while acknowledging open problems (e.g., Navier-Stokes existence).\nExample: A survey on mirror symmetry that interweaves references to Yau\'s Calabi-Yau manifolds, Kontsevich\'s homological mirror symmetry, and recent progress in SYZ conjectures.'
    },
    'physics': {
        'description': 'Reference evaluation specific to Physics surveys, focusing on physical relevance, foundational works, and experimental validation.',
        'score 1': 'Deficient Referencing\nCriteria:\n>60% irrelevant citations lacking clear connection to survey topic\nMissing foundational papers establishing core concepts (e.g., omitting Einstein\'s 1905 photoelectric effect paper in quantum optics review)\nHeavy reliance on non-physics sources without cross-disciplinary justification\nContains outdated references (>10 years old) without historical context',
        'score 2': 'Inadequate Referencing\nCriteria:\n40-60% tangential citations with weak thematic links\nIncomplete coverage of major physics subfields relevant to topic\nUnderrepresentation of recent (<5 years) arXiv contributions\nOvercitation of limited research groups without balancing competing perspectives',
        'score 3': 'Acceptable Referencing\nCriteria:\n20-40% marginally relevant citations with some justification\nIdentifies key historical milestones but lacks depth in contemporary developments\nIncludes major Physical Review journals but misses field-specific repositories (e.g., INSPIRE-HEP)\nModerate imbalance between theoretical frameworks and experimental validations',
        'score 4': 'Proficient Referencing\nCriteria:\n5-20% non-optimal citations with minimal impact on utility\nComprehensive coverage of landmark studies across ≥3 decades\nIntegrates peer-reviewed publications with vetted preprints appropriately\nDemonstrates awareness of emerging methodologies through recent (<2 years) citations',
        'score 5': 'Exemplary Referencing\nCriteria:\n>95% directly relevant citations forming cohesive intellectual trajectory\nMasterful synthesis of:\n-Foundational theories from primary literature\n-Recent breakthroughs in high-impact journals (e.g., Phys. Rev. Lett.)\n-Preprint innovations from arXiv\n-Cross-disciplinary connections where applicable\nOptimal temporal distribution with ≤20% citations >10 years old\nExplicit inclusion of contradictory findings and unresolved debates'
    },
    'q-bio': {
        'description': 'Reference evaluation specific to Quantitative Biology surveys, focusing on biological relevance, computational methods, and interdisciplinary integration.',
        'score 1': 'Inadequate Referencing\nCriteria:\n>60% irrelevant or marginal references:\n-References lack alignment with core quantitative biology themes (e.g., omics, dynamical modeling, machine learning applications).\n-Over-reliance on outdated studies (>10 years) without justification.\n-Minimal inclusion of foundational computational frameworks (e.g., Bioconductor, PyTorch for biology) or benchmark datasets (e.g., TCGA, ImageData Resource).\n-Example: A survey on single-cell RNA-seq analysis cites predominantly non-computational wet-lab studies.',
        'score 2': 'Partially Relevant Referencing\nCriteria:\n40-60% irrelevant references:\n-Key methodologies (e.g., differential equation modeling, Bayesian inference) are underrepresented.\n-Limited coverage of reproducibility tools (e.g., Jupyter Notebooks, Snakemake) or community standards (FAIR principles).\n-Sparse citations for emerging areas (spatial transcriptomics, AI-driven drug discovery).\n-Example: A review of phylogenetic tools omits references to widely used software like BEAST or RevBayes.',
        'score 3': 'Moderately Relevant Referencing\nCriteria:\n20-40% irrelevant references:\n-Most references align with the topic but lack depth in critical subfields.\n-Inconsistent inclusion of both preprints (e.g., arXiv, bioRxiv) and peer-reviewed literature.\n-Gaps in citing validation frameworks (e.g., benchmarking studies) or interdisciplinary bridges (e.g., biophysical models integrated with deep learning).\n-Example: A survey on cryo-EM data analysis cites relevant tools but neglects computational scalability challenges.',
        'score 4': 'Strong Referencing\nCriteria:\n5-20% misaligned references:\n-Comprehensive coverage of seminal works (e.g., Michaelis-Menten kinetics, Gillespie algorithms) and modern advances (graph neural networks for protein folding).\n-Balanced representation of theoretical, computational, and experimental studies.\n-Minor omissions in niche areas (e.g., quantum computing applications in genomics).\n-Example: A review of genome-wide association studies (GWAS) largely cites robust tools like PLINK but underrepresents rare-variant analysis methods.',
        'score 5': 'Exemplary Referencing\nCriteria:\n>95% relevant references:\n-References span foundational models (e.g., Lotka-Volterra equations), cutting-edge tools (AlphaFold, CellProfiler), and critical evaluations of reproducibility.\n-Integrates preprints for emerging trends (e.g., foundation models in biology) alongside peer-reviewed validation.\n-Includes interdisciplinary benchmarks (e.g., DREAM Challenges) and datasets essential for reproducibility.\n-Example: A survey on spatial proteomics cites spatialLIBD, Seurat, and mechanistic models while addressing computational limitations.'
    },
    'q-fin': {
        'description': 'Reference evaluation specific to Quantitative Finance surveys, focusing on financial relevance, mathematical frameworks, and market applications.',
        'score 1': 'Deficient Referencing\nCharacteristics:\n-Over 60% of references lack direct connection to quantitative finance (e.g., general machine learning papers without financial use cases, unrelated econometric theories).\n-Seminal works (e.g., Black-Scholes model, Fama-French factor framework) are omitted or underrepresented.\n-Heavy reliance on non-authoritative sources (blogs, non-peer-reviewed preprints without subsequent validation).\n-No discernible structure linking references to subtopics like stochastic modeling, portfolio optimization, or risk management.\nExample Deficiency:\nA survey on AI-driven trading cites 40% generic neural network papers without specifying applications to market prediction or execution algorithms.',
        'score 2': 'Partially Relevant\nCharacteristics:\n-40-60% of references marginally relate to finance (e.g., theoretical math papers with potential but unexplored financial links).\n-Limited coverage of foundational works (≤50% of expected seminal papers cited).\n-Recent advances (post-2020) in areas like quantum finance or LLMs for sentiment analysis are sporadically included but not systematically reviewed.\n-Weak thematic grouping; references to time-series forecasting and derivative pricing are intermingled without clear subsections.\nExample Deficiency:\nA survey on portfolio optimization cites classical Markowitz theory but misses key post-2010 developments in transaction-cost-aware models.',
        'score 3': 'Mostly Adequate\nCharacteristics:\n-20-40% of references are tangential (e.g., broad optimization algorithms without financial benchmarks).\n-70-80% of seminal works included, but gaps exist in niche areas (e.g., cryptoasset pricing models post-2022).\n-Moderate attention to emerging trends (e.g., 5-10 references to quantum computing for option pricing).\n-Subtopics are identified but lack depth (e.g., "machine learning" section cites 10 papers without distinguishing reinforcement learning from NLP applications).\nExample Deficiency:\nA survey on financial NLP adequately covers sentiment analysis but omits critical studies on LLM hallucination risks in earnings report analysis.',
        'score 4': 'Strong with Minor Gaps\nCharacteristics:\n-5-20% of references are misaligned (e.g., including 3-5 marginally relevant physics papers in a section on quantum annealing).\n-90-95% of expected foundational and modern works cited, with 1-2 omissions in fast-moving areas (e.g., missing a 2024 arXiv paper on transformer-based volatility prediction).\n-Clear subsections (e.g., "Stochastic Control," "High-Frequency Trading") with 80% of references correctly categorized.\n-Balanced coverage of theory (e.g., stochastic calculus) and applied studies (e.g., backtests on CRSP/Compustat data).\nExample Deficiency:\nA comprehensive survey on risk modeling cites all major Value-at-Risk methodologies but underrepresents recent regulatory frameworks like FRTB.',
        'score 5': 'Exemplary Referencing\nCharacteristics:\n-Over 95% of references directly address quantitative finance themes, with explicit ties to financial datasets, markets, or regulatory constraints.\n-Seminal works (pre-2010) and modern advances (2020-2025) are proportionately represented (e.g., 20% foundational, 50% post-2010 innovations, 30% 2023-2025 cutting-edge).\n-Thematic clusters are meticulously organized (e.g., subsections on "Market Microstructure," "Explainable AI for Credit Scoring"), each supported by 15-30 highly relevant papers.\n-Interdisciplinary connections (e.g., quantum computing, behavioral finance) are acknowledged through targeted citations to hybrid methodologies.\n-All references pass authority checks: ≥80% from top finance journals (Journal of Financial Economics), arXiv q-fin submissions, or peer-reviewed AI/quant conferences (e.g., NeurIPS Quantitative Finance workshops).\nExemplary Feature:\nA 2024 survey on LLMs in finance cites 100% finance-specific NLP studies, including 5 seminal transformer adaptations for earnings call analysis and 8 recent (2024) papers on mitigating overfitting in financial text generation'
    },
    'stat': {
        'description': 'Reference evaluation specific to Statistics surveys, focusing on statistical relevance, methodological frameworks, and theoretical foundations.',
        'score 1': 'Deficient Referencing\nCriteria:\nOver 60% citations lack statistical relevance (e.g., engineering applications without methodological innovation)\nReliance on non-peer reviewed sources (Wikipedia, unverified preprints)\nOmission of foundational texts in subfield (e.g., missing Efron\'s bootstrap papers in resampling review)',
        'score 2': 'Partial Relevance\nCriteria:\n40-60% citations marginally related (e.g., machine learning papers without statistical theory)\nLimited coverage of statistical literature (≤50% citations from core stats journals)\nTemporal imbalance - either overly historical (pre-2000) or ignoring seminal works',
        'score 3': 'Emerging Competence\nCriteria:\n20-40% citations lack direct connection to statistical themes\n≥60% sources from statistical publications but missing key subfield works\nBasic inclusion of modern developments (e.g., mentions causal inference without Pearl\'s do-calculus)',
        'score 4': 'Proficient Referencing\nCriteria:\n≤20% citations with weak statistical alignment\n≥80% sources from core statistics literature across multiple subdomains\nDemonstrates temporal awareness with 20-30% recent works (last 5 years)\nIncludes both methodological and applied statistical references',
        'score 5': 'Exemplary Scholarship\nCriteria:\n≥95% citations directly advance statistical understanding\nSources span:\n-Foundational texts (≥15% historical landmarks)\n-Modern methodology (≥40% last decade innovations)\n-Interdisciplinary connections (≤20% adjacent fields with statistical relevance)\nFeatures 5-10% citations from premier statistical venues (Annals of Statistics, JRSS-B)\nMaintains arXiv preprints only for emerging topics with peer-reviewed support'
    }
}
