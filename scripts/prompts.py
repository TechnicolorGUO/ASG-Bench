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
        'score 5': 'The outline is exceptionally clear, logically organized, and easy to follow. Section titles are concise and informative, and the structure fully represents the topic’s breadth and depth.'
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
- It is directly and specifically related to the parent’s core subject,
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

REFERENCE_QUALITY_PROMPT = """
You are an academic reviewer. Given the topic, a sentence from a paper, and the references the sentence cites, please judge the following:

1. How many references does the sentence cite in total?
2. How many of these references truly support or are relevant to the content of the sentence?

Please return ONLY a JSON object in the following format:

{{
  "total": <int>,
  "supported": <int>
}}

Input:
Topic: {topic}

Sentence: {sentence}

References:
{references}

Instructions:
- "total_reference_count": The total number of references cited by the sentence (length of the reference list).
- "supported_reference_count": The number of references that are actually relevant or supporting to the sentence content according to their titles and abstracts.
- Only output the JSON, nothing else.
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

# -------------- Generation Prompts --------------
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