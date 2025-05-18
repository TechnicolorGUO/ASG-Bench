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
    "Reference": {
        "description": (
            "Reference relevance evaluates whether the references listed in the References section are closely related to the survey's topic. "
            "A high-quality References section should primarily include publications, articles, or works that are directly relevant to the subject matter. "
            "The score depends on the proportion of irrelevant or tangential entries as identified by the model. "
            "Additionally, the formatting of the references should adhere to standard citation guidelines (e.g., APA, MLA, Chicago), ensuring consistency, accuracy, and completeness. "
            "Poor formatting, missing information, or inconsistencies in style will negatively impact the score."
        ),
        "score 1": "Most references (over 60%) are irrelevant or only marginally related to the topic and/or the references are poorly formatted, with significant inconsistencies or missing details.",
        "score 2": "A significant portion (40-60%) of references are not closely related to the topic and/or the references show notable formatting issues, such as missing key information or inconsistent citation styles.",
        "score 3": "Some references (20-40%) are not relevant to the topic, but the majority are appropriate. Formatting may have minor issues, but does not significantly detract from the overall quality.",
        "score 4": "A small number (5-20%) of references are not well aligned, but most are relevant. The formatting is mostly consistent, with only occasional minor errors.",
        "score 5": "Nearly all references (over 95%) are relevant and directly related to the topic. The formatting is consistent, accurate, and adheres to standard citation guidelines."
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
You are given the outline of an academic survey on the topic "{topic}". Focus on identifying logical, domain-specific, and practically relevant sections that align with real academic outlines.

---
{outline}
---

Please match the outline sections (based on their titles, meanings, and relevance, not just exact words) to the following standard academic survey sections. Emphasize accurate alignment with standard academic structures commonly found in literature surveys.

A section is considered matched only if:
- Its title or meaning corresponds directly and specifically to any of the listed templates below, even if the wording differs,
- It demonstrates clear logical flow and relevance to the academic survey topic,
- It reflects practical relevance and grounded domain expertise,
- It avoids speculative, overly broad, or tangential interpretations.
Here is the checklist of standard sections (with common synonyms):

1. Abstract
2. Introduction / Background
3. Related Work / Literature Review
4. Problem Definition / Scope / Motivation / Objectives / Goals
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
Given the survey topic "{topic}" and the following outline structure, analyze the relationship between the parent node and each of its direct child nodes. Prioritize the logical flow, domain expertise, and practical relevance commonly found in literature surveys:

- Parent node:
  Index: {parent_index}
  Title: {parent_title}

- Direct child nodes:
{children_list}

For each child node, decide whether it is a *necessary and direct subtopic* of the parent node. Mark as "Yes" if:
- The child topic is critical for fully understanding or representing the parent node **OR** it represents a key application or real-world use case that highlights the parent node's practical relevance,
- It reflects practical relevance and is grounded in the domain expertise of the subject,
- It directly supports, expands, **or demonstrates the application** of the parent's core subject, avoiding speculative or overly broad topics,
- It aligns with the logical structure and flow of well-crafted human-generated surveys,
- It cannot stand alone as an independent section without losing connection to the parent topic, **unless its inclusion strengthens the overall relevance of the parent node by demonstrating real-world use cases.**

If the child node is only loosely related, optional, speculative, or could fit under multiple different parent nodes, answer "No".
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
        'score 1': 'Disjointed Technical Narrative\nLacks fundamental CS survey components (e.g., problem taxonomies, methodology comparison tables, algorithmic analysis)\nPresents technical concepts in isolation without connecting foundational theories to modern applications\nFails to distinguish between computer science subdomains (e.g., conflating machine learning principles with cybersecurity architectures)\nContains redundant technical explanations across sections without progressive complexity',
        'score 2': 'Partial Technical Organization\nIdentifies key CS domains but struggles with cross-paradigm comparisons (e.g., imperative vs. functional programming paradigms)\nTechnical timelines mix historical developments with contemporary innovations without clear phase demarcation\nVisual aids (algorithm pseudocode, architecture diagrams) appear disconnected from textual explanations\nTransitional phrases exist but fail to bridge technical complexity gradients between sections',
        'score 3': 'Conventional Technical Flow\nFollows standard CS survey structure: abstract → problem space → methodology review → case studies → future directions\nTechnical content organized by computational complexity levels (e.g., separating polynomial-time algorithms from NP-hard solutions)\nContains basic comparative tables for algorithm complexity or system architectures\nTransitions use technical signposting (e.g., "Having discussed asymptotic analysis, we now examine practical runtime constraints") but lack depth in connecting theoretical and applied aspects',
        'score 4': 'Cohesive Technical Synthesis\nEmploys adaptive structure matching CS subfield requirements (e.g., separate hardware/software stacks in embedded systems surveys)\nTechnical progression follows computational dependency chains (e.g., prerequisite algorithms introduced before dependent systems)\nIntegrates interactive elements for complex topics (expandable proof sketches, clickable architecture diagrams in digital formats)\nMaintains parallel technical narratives for different computational paradigms (e.g., quantum vs. classical computing comparisons)',
        'score 5': 'Innovative Computational Architecture\nFeatures subfield-tailered structures (e.g., timeline matrices for AI evolution, multidimensional taxonomies for cybersecurity threats)\nTechnical transitions employ computational metaphors (e.g., "This neural architecture naturally composes with the previously discussed optimization pipeline as shown in Figure 3")\nContains self-adaptive sections that adjust depth based on cited evidence density and impact factors\nImplements formal verification of structural logic through computational models (e.g., dependency graphs validating citation flow)\nIntroduces novel organizational paradigms for emerging CS domains (e.g., hybrid quantum-classical algorithm surveys with entanglement-aware grouping)'
    },
    'econ': {
        'description': 'Structure evaluation specific to Economics surveys, focusing on theoretical frameworks, empirical methodologies, and policy implications.',
        'score 1': 'Disjointed Economic Narrative\nFails to distinguish between microeconomic and macroeconomic perspectives\nNo clear progression from theoretical models to empirical validation\nMixes heterodox and mainstream economic theories without contextualization\nLacks sections on policy implications or welfare economics considerations\nOmits standard economics survey components (e.g., stylized facts, identification strategies)',
        'score 2': 'Partial Economic Framework\nBasic separation of topics (e.g., labor vs monetary economics) but weak thematic integration\nLimited connection between econometric methods and empirical findings\nSuperficial treatment of causal inference techniques in policy evaluation\nInconsistent use of economic models across sections\nTransitional phrases ignore important economic relationships (e.g., price-quantity linkages)',
        'score 3': 'Conventional Economic Organization\nStandard structure (theory → methods → applications) with basic coherence\nIdentifies major economic schools of thought but limited critical synthesis\nContains expected sections (welfare analysis, equilibrium models) with some redundancy\nModerate success in linking microfoundations to macroeconomic outcomes\nBasic transitions between neoclassical and behavioral economic paradigms',
        'score 4': 'Sophisticated Economic Architecture\nExplicit mapping of economic theory to empirical testing protocols\nEffective integration of structural vs reduced-form approaches\nClear progression from identification strategies to policy relevance\nThematic clustering of related economic subfields (e.g., labor/education economics)\nTransitions highlight economic mechanisms (e.g., general equilibrium effects)',
        'score 5': 'Masterful Economic Synthesis\nUnified framework reconciling competing economic paradigms\nHierarchical organization of models by assumptions and predictive power\nSeamless integration of causal inference methods with economic theory\nDynamic structure adapting to heterodox vs mainstream debates\nTransitions explicitly model economic relationships (e.g., elasticity substitutions)'
    },
    'eess': {
        'description': 'Structure evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical frameworks, system architectures, and engineering methodologies.',
        'score 1': 'Disjointed Technical Narrative\nPresents concepts in random order without alignment to EE methodologies (e.g., mixing control theory with semiconductor physics without justification)\nFails to separate foundational principles (e.g., Maxwell\'s equations) from applied domains (e.g., power systems)\nContains redundant technical explanations across sections (e.g., repeating matrix decomposition methods in signal processing and machine learning chapters)\nLacks standardized section hierarchy (e.g., missing "Challenges in Smart Grid Cybersecurity" subsection under "Energy Systems" section)',
        'score 2': 'Partial Technical Organization\nGroups related EE topics (e.g., power electronics and renewable energy systems) but provides weak justification for their sequence\nCreates ambiguous subsection boundaries (e.g., overlapping content between "Optimization Algorithms" and "Energy Management Systems")\nUses inconsistent depth in technical explanations (e.g., detailed semiconductor physics vs. superficial treatment of control theory)\nContains abrupt shifts between mathematical formalism (e.g., differential equations) and applied case studies without transitional paragraphs',
        'score 3': 'Functionally Structured Technical Survey\nFollows EE research lifecycle structure: 1) Fundamental principles 2) Implementation architectures 3) Validation methodologies 4) Emerging applications\nImplements modular section design for complex systems (e.g., separate "Communication Protocols" and "Hardware Security" subsections under IoT chapter)\nMaintains consistent technical depth using EE standards (e.g., IEEE format for equations, SI units in measurements)\nIncludes transitional paragraphs connecting theory to practice (e.g., "The Kalman filter derivation above enables the following state estimation applications in smart grids...")',
        'score 4': 'Cohesive Systems-Oriented Architecture\nEmploys systems engineering V-model structure: Requirements → Design → Verification → Deployment\nImplements cross-layer analysis (e.g., linking device-level semiconductor characteristics to grid-level stability impacts)\nUses standardized EE taxonomy (IEEE Thesaurus terms) for subsection headers\nFeatures matrix-based transitional devices (e.g., "Table 3 compares the surveyed power flow algorithms against the criteria established in Section 2")\nContains only minor structural imperfections (e.g., slightly disproportionate emphasis on embedded systems vs. power electronics)',
        'score 5': 'Optimized Technical Synthesis Structure\nImplements recursive systems framework:\n-Fundamentals: ∇⋅D=ρv(Maxwell\'s Equations)\n-Subsystems: Power electronics ↔ Control theory interfaces\n-Integration: Cyber-physical system co-design\n-Validation: Hardware-in-the-loop testing methodologies\nFeatures context-aware transitions:\n-"The semiconductor physics discussed in Section 2.1 directly enables the wide-bandgap devices analyzed in Section 3.2"\n-"These communication protocols (Section 4.3) address the latency constraints identified in the smart grid requirements (Section 1.2)"\nIncludes dynamic structural elements:\n-Adaptive depth control via technical appendices for specialized topics (e.g., detailed derivation of space vector modulation)\n-Cross-referential matrices linking theoretical models  to application case studies\nDemonstrates Pareto-optimal content distribution between:\n-Mathematical formalism (20-25%)\n-Implementation architectures (35-40%)\n-Comparative analysis (25-30%)\n-Future research vectors (10-15%)'
    },
    'math': {
        'description': 'Structure evaluation specific to Mathematics surveys, focusing on mathematical coherence, logical progression, and theoretical frameworks.',
        'score 1': 'Disjointed Framework\nLogical Flow: No discernible progression of ideas; sections lack purpose or connection.\nSection Organization: Content appears randomly ordered (e.g., advanced theorems precede definitions).\nTransitions: Abrupt shifts between topics without justification (e.g., switching from algebraic geometry to stochastic calculus without contextual linkage).\nRedundancy: Critical repetitions of definitions/results without incremental value.\nTaxonomy: Fails to classify mathematical paradigms (e.g., conflating analytical and combinatorial methods).',
        'score 2': 'Fragmented Structure\nLogical Flow: Partial coherence with isolated logical leaps (e.g., introducing PDE applications before establishing variational principles).\nSection Organization: Subsections misaligned with parent sections (e.g., "Topological Data Analysis" nested under "Linear Algebra").\nTransitions: Minimal bridging phrases (e.g., "Next, we discuss..." without explaining relevance).\nRedundancy: Overlapping case studies in distinct sections (e.g., re-proving Bézout\'s theorem in both algebraic geometry and cryptography sections).\nTaxonomy: Incomplete categorization (e.g., omitting key subfields of category theory).',
        'score 3': 'Functionally Adequate\nLogical Flow: Generally sequential but with minor gaps (e.g., delayed motivation for abstract measure theory in probability surveys).\nSection Organization: Subsections logically grouped but occasionally misplaced (e.g., "Graph Isomorphism" under "Complexity Classes" instead of "Discrete Mathematics").\nTransitions: Formulaic connectors (e.g., "Having discussed X, we now consider Y") without deeper synthesis.\nRedundancy: Limited unintentional overlaps (e.g., restating Banach fixed-point theorem in both functional analysis and dynamical systems).\nTaxonomy: Basic classification of methods/theorems but lacks subfield granularity (e.g., grouping all optimization techniques under "Calculus of Variations").',
        'score 4': 'Cohesive Architecture\nLogical Flow: Purposeful sequencing with few discontinuities (e.g., deriving stochastic differential equations before exploring their numerical approximations).\nSection Organization: Subsections align with parent themes (e.g., "Elliptic Curve Cryptography" nested under "Number Theory Applications").\nTransitions: Contextualized pivots (e.g., "The preceding homological algebra framework naturally extends to..." followed by examples).\nRedundancy: Strategic repetition only for emphasis (e.g., restating key lemmas before major proofs).\nTaxonomy: Multilevel classifications (e.g., partitioning optimization into convex, non-convex, and stochastic subfields with technique-specific subtrees).',
        'score 5': 'Exemplary Synthesis\nLogical Flow: Seamless progression from foundations to frontiers (e.g., beginning with Hilbert spaces, advancing to spectral theory, concluding with quantum computing applications).\nSection Organization: Hierarchical nesting of concepts (e.g., "Manifold Learning" → "Riemannian Geometry" → "Information Geometry").\nTransitions: Thematic threads'
    },
    'physics': {
        'description': 'Structure evaluation specific to Physics surveys, focusing on physical relevance, foundational works, and experimental validation.',
        'score 1': 'The survey lacks coherence, with disjointed sections and no identifiable thematic framework. Key physics concepts (e.g., theoretical foundations, methodologies, applications) are presented haphazardly, and transitions between topics are abrupt or nonexistent. Redundant subsections or misplaced content (e.g., experimental methods in a theory-focused section) obscure the narrative.',
        'score 2': 'The survey exhibits weak thematic organization, with sections loosely grouped by broad topics (e.g., "Theoretical Background" or "Applications") but lacking sub-structure. Transitions between physics subfields (e.g., classical mechanics to quantum systems) are poorly justified, and connections to overarching research trends (e.g., machine learning in physics) are superficial. Some subsections repeat ideas or fail to align with the paper\'s stated scope.',
        'score 3': 'The survey has a recognizable structure (e.g., theory → methods → applications → challenges) but lacks depth in subfield integration. Transitions between foundational physics principles (e.g., Newtonian mechanics) and modern advancements (e.g., AI-driven simulations) are functional but formulaic. Subsections exist but may omit critical linkages (e.g., multiscale modeling in materials science ) or overemphasize niche topics.',
        'score 4': 'The survey demonstrates strong logical flow, with sections organized by physics themes (e.g., "Quantum Computing Architectures" or "Multiphase Fluid Dynamics") and subsections addressing specific methodologies (e.g., lattice Boltzmann methods ) or applications (e.g., medical physics ). Transitions between experimental, theoretical, and computational approaches are purposeful, though occasional gaps remain (e.g., insufficient discussion of cross-scale interactions ). Recent advancements (e.g., physics-informed machine learning ) are contextualized within historical frameworks.',
        'score 5': 'The survey is masterfully structured, with a tightly woven narrative that integrates foundational physics principles, cutting-edge methodologies, and interdisciplinary applications. Sections are hierarchically organized (e.g., "Fundamental Theories" → "Computational Advances" → "Emerging Applications") and subsections explore nuanced topics (e.g., baryonic feedback in cosmology , tensor networks in quantum simulations ). Transitions highlight causal relationships (e.g., how discretization techniques enable large-scale fluid simulations ) and synthesize multidisciplinary insights (e.g., biomechanics and fracture modeling ). The framework anticipates reader needs, balancing depth with accessibility, and concludes with forward-looking syntheses of open challenges (e.g., validation gaps in additive manufacturing ).'
    },
    'q-bio': {
        'description': 'Structure evaluation specific to Quantitative Biology surveys, focusing on biological relevance, computational methods, and interdisciplinary integration.',
        'score 1': 'The survey lacks a coherent framework, with no discernible thematic or methodological organization. Sections are disjointed, failing to establish connections between biological concepts, computational methods, and applications. Critical elements such as categorization of techniques (e.g., sequence-based vs. structure-based methods) or evaluation metrics (e.g., precision-recall curves for protein function prediction) are absent or poorly defined. Transitions between topics are abrupt, and the paper does not guide readers through foundational principles, advancements, or future challenges in quantitative biology.',
        'score 2': 'The survey exhibits fragmented logic, with limited alignment to the core themes of quantitative biology. While some sections (e.g., "Deep Learning Applications") are identifiable, their arrangement lacks a unifying narrative. Methodological categories (e.g., hybrid information-based approaches) are mentioned but not systematically compared. Descriptions of biological datasets (e.g., protein interaction networks) or computational frameworks (e.g., graph neural networks) are inconsistently integrated, leading to redundancy or gaps in coverage. Transitions between traditional and modern techniques (e.g., from BLAST to AlphaFold) are underdeveloped.',
        'score 3': 'The survey demonstrates a basic organizational structure, with sections broadly aligned to quantitative biology standards (e.g., IMRaD format). Methodological categories (sequence-based, structure-based, network-based) are defined but lack critical analysis of their trade-offs in specific biological contexts. Evaluative components (e.g., benchmarking on CASP or CAFA datasets) are included but not contextualized within broader biological challenges. Transitions between subsections (e.g., "Data Sources" to "Model Architectures") are functional but formulaic, with occasional repetition of concepts like "encoder-decoder frameworks" without progressive depth.',
        'score 4': 'The survey is logically structured, with clear alignment to quantitative biology paradigms. Major sections (e.g., "Evolution of Protein Function Prediction Methods") are subdivided into thematic pillars (e.g., phylogenetic profiling, multi-omics integration), each analyzed through computational and biological lenses. Methodological comparisons (e.g., accuracy of residue contact prediction in AlphaFold vs. RoseTTAFold) are supported by quantitative metrics (e.g., root-mean-square deviation). Transitions between foundational concepts (e.g., sequence alignment algorithms) and emerging areas (e.g., language models for protein design) are smooth, though deeper synthesis of interdisciplinary implications (e.g., clinical translation) could enhance cohesion.',
        'score 5': 'The survey exemplifies a masterfully organized framework, seamlessly integrating quantitative rigor with biological relevance. Sections are hierarchically structured to reflect the field\'s complexity-for example, distinguishing data types (omics, imaging), methodologies (physics-based simulations, deep learning), and applications (drug discovery, synthetic biology). Subsections critically evaluate method families (e.g., convolutional vs. transformer architectures for protein folding) using domain-specific benchmarks (e.g., TM-score, pLDDT). The narrative progresses from historical context (e.g., homology modeling) to cutting-edge advancements (e.g., diffusion models for protein generation), culminating in a unified discussion of open challenges (e.g., interpretability of AI models in wet-lab validation). Transitions are purposeful, such as linking hierarchical learning frameworks (e.g., ProtBoost\'s use of Gene Ontology) to real-world biological scalability. Redundancy is absent, with each section building upon prior insights to create a cumulative, interdisciplinary perspective.'
    },
    'q-fin': {
        'description': 'Structure evaluation specific to Quantitative Finance surveys, focusing on financial models, mathematical frameworks, and market applications.',
        'score 1': 'Disjointed Framework\nStructural flaws: No discernible progression between foundational theories (e.g., stochastic calculus), computational methods (e.g., Monte Carlo simulations), and financial applications (e.g., derivative pricing).\nContent gaps: Missing critical components of quantitative finance pipelines such as data preprocessing techniques, backtesting protocols, or risk management considerations.\nThematic chaos: Random sequencing of topics without differentiation between established practices (e.g., Black-Scholes models) and emerging paradigms (e.g., quantum portfolio optimization).\nTransition failures: Abrupt jumps between mathematical formulations and empirical results without explanatory bridges.',
        'score 2': 'Partial Coherence with Notable Deficits\nWeak methodological linkage: Superficial treatment of connections between econometric models (e.g., GARCH) and machine learning approaches (e.g., LSTM networks).\nIncomplete taxonomy: Cursory categorization of financial models without clear differentiation between parametric (e.g., HJM framework) and non-parametric approaches (e.g., neural SDEs).\nTemporal disorganization: Historical developments in quantitative methods presented out of chronological sequence, obscuring evolutionary patterns.\nSection imbalance: Overemphasis on theoretical constructs (e.g., measure changes) with inadequate coverage of implementation challenges (e.g., numerical stability in PDE solvers).',
        'score 3': 'Functional Organization with Improvement Opportunities\nBasic pipeline structure: Recognizable progression from data sources → feature engineering → model development → performance validation, but lacks depth in explaining interdependencies.\nModerate cross-referencing: Some connections drawn between financial mathematics (e.g., Ito calculus) and computational techniques (e.g., finite difference methods), but misses opportunities for synthesis.\nEmerging trends addressed: Includes sections on AI/ML applications or quantum algorithms, but treats them as isolated additions rather than integrated components.\nTransition adequacy: Uses standard section bridges ("Having discussed X, we now consider Y") but lacks thematic continuity between mathematical theory and trading system architectures.',
        'score 4': 'Professional-Grade Structure\nPipeline optimization: Explicit mapping of model development stages from hypothesis formulation (e.g., arbitrage detection) to deployment challenges (e.g., latency constraints).\nInterdisciplinary synthesis: Effective integration of financial economics principles with computational statistics (e.g., explaining Bayesian methods in volatility surface calibration).\nTemporal layering: Clear delineation of historical milestones (Markowitz optimization), current practices (risk parity strategies), and frontier research (ZK-SNARKs for private trading).\nDynamic transitions: Purposeful sequencing between adjacent sections using financial motivation→mathematical formalization→empirical validation patterns.',
        'score 5': 'Exemplary Architectural Design\nHolistic integration: Seamless weaving of theoretical models, numerical implementations, and regulatory considerations throughout all sections (e.g., linking CVA computations to Basel III requirements).\nInnovative taxonomy: Original classification frameworks that reveal hidden connections between disparate domains (e.g., topological data analysis in market microstructure studies).\nAnticipatory structure: Sections naturally flow from well-established techniques (PCA for yield curve modeling) to cutting-edge approaches (attention mechanisms in limit order book prediction).\nRecursive reinforcement: Key concepts reintroduced at multiple abstraction levels (e.g., stochastic integration first as mathematical tool, later as risk factor aggregator).\nMeta-commentary: Explicit discussion of structural choices explaining why certain model families (structural vs reduced-form) receive particular organizational emphasis'
    },
    'stat': {
        'description': 'Structure evaluation specific to Statistics surveys, focusing on statistical frameworks, methodological approaches, and theoretical foundations.',
        'score 1': 'Disjointed Framework\nContains fragmented discussions of statistical methods without mathematical connections\nFails to distinguish between core theory and application variants (e.g., conflates kernel density estimation with nonparametric regression)\nLacks standard statistical survey components: No separate methodology comparison, assumption analysis, or error propagation sections',
        'score 2': 'Partial Organization\nIdentifies major statistical domains but provides uneven depth (e.g., detailed treatment of regression analysis while superficially covering time series)\nAttempts methodological categorization but mixes abstraction levels (e.g., discusses EM algorithm without connecting to general missing data frameworks)\nContains redundant mathematical presentations (e.g., rederives basic probability theorems across multiple sections)',
        'score 3': 'Coherent Baseline\nGroups methods by statistical families (parametric vs. nonparametric, frequentist vs. Bayesian) with adequate mathematical definitions\nFollows standard progression: Probability foundations → Estimation theory → Hypothesis testing → Advanced topics\nIncludes comparative tables of estimator properties (bias, variance, convergence rates) but lacks synthesis across tables',
        'score 4': 'Integrated Architecture\nEmbeds computational advancements within theoretical frameworks (e.g., places Markov chain Monte Carlo within Bayesian computation legacy)\nFeatures specialized structural elements:\n-Assumption Taxonomies: Hierarchical breakdown of model prerequisites (e.g., linear regression conditions vs. generalized additive model requirements)\n-Convergence Bridges: Explicit links between asymptotic theory and finite-sample properties\nEmploys transitional devices connecting mathematical proofs to practical implementation challenges',
        'score 5': 'Exemplary Statistical Synthesis\nThematic Modularity: Self-contained sections for methodological paradigms (e.g., likelihood-based inference, resampling methods) with cross-referenced connections\nMultilayer Organization:\n-Foundational Layer: Measure-theoretic probability, estimation theory\n-Methodological Layer: Regression analysis, multivariate analysis, experimental design\n-Computational Layer: EM algorithm variations, bootstrap implementations, MCMC innovations\nDynamic Flow Mechanisms:\n-Conceptual Cascades: Natural progression from point estimation → interval estimation → hypothesis testing\n-Methodological Phylogenies: Visual mappings of statistical technique evolution (e.g., ANOVA → MANOVA → repeated measures ANOVA)\nContains validation gateways connecting theoretical properties to application guidelines (e.g., deriving sample size requirements from power function analyses)'
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

COVERAGE_DOMAIN_CRITERIA = {
    "cs": {
        'description': 'Coverage evaluation specific to Computer Science surveys, focusing on technical breadth, depth, and interdisciplinary connections.',
        'score 1': 'Very Limited Coverage\nSurveys only address isolated technical components (e.g., a single algorithm or framework) without contextualizing their role in broader research landscapes.\nMajor subfields (e.g., "efficient inference" vs. "model alignment" in LLMs) are omitted.\nNo discussion of interdisciplinary connections (e.g., AI ethics, hardware-software co-design).\nFails to include recent advancements (past 2-3 years), critical in fast-moving fields like generative AI.',
        'score 2': 'Partial Coverage with Notable Gaps\nCovers foundational concepts but lacks depth in emerging paradigms (e.g., mentions transformer architectures but omits speculative decoding or dynamic sparse training).\nIncomplete treatment of key challenges (e.g., discusses LLM hallucination but ignores privacy-utility tradeoffs).\nLimited analysis of real-world applications (e.g., healthcare or robotics use cases).\nOverlooks critical benchmarks or datasets (e.g., HELM for holistic evaluation).',
        'score 3': 'Generally Comprehensive with Minor Omissions\nAddresses major technical approaches (e.g., quantization, distillation, pruning for model efficiency) but lacks nuanced comparisons (e.g., Pareto frontiers for accuracy vs. latency).\nSurveys ethical considerations but does not operationalize them into actionable frameworks.\nCovers theoretical advancements but underrepresents deployment challenges (e.g., serving infrastructure, energy costs).\nOmits niche but impactful areas (e.g., neuromorphic computing for AI hardware).',
        'score 4': 'Near-Complete Coverage with Marginal Shortcomings\nSynthesizes classical and cutting-edge methods (e.g., RLHF and constitutional AI for alignment).\nIntegrates cross-disciplinary insights (e.g., neuroscience-inspired architectures or legal constraints on AI).\nDiscusses scalability across hardware tiers (edge devices to data centers) but lacks case studies.\nMinor gaps in addressing longitudinal trends (e.g., evolution of attention mechanisms from 2017-2025).',
        'score 5': 'Exhaustive and Insight-Driven Coverage\nHolistic exploration of all technical dimensions (e.g., model architectures, training protocols, inference optimizations, evaluation frameworks).\nCritically analyzes tradeoffs (e.g., precision-recall curves vs. carbon footprint in LLM deployment).\nMaps open challenges to future research pathways (e.g., "post-scaling era" innovations in modular AI).\nIncludes meta-discussions on reproducibility, dataset licensing, and societal impact.\nCovers peripheral but transformative areas (e.g., quantum machine learning or bio-inspired algorithms).'
    },
    "econ": {
        'description': 'Coverage evaluation specific to Economics surveys, focusing on theoretical frameworks, empirical methodologies, and policy implications.',
        'score 1': 'Highly Limited Coverage\nScope: Addresses only narrow subtopics (e.g., a single model or empirical technique) without connecting to broader economic frameworks.\nOmissions: Fails to discuss foundational theories (e.g., neoclassical economics, Keynesian macroeconomics) or major subfields (e.g., labor, development, behavioral economics).\nMethodological Gaps: Ignores critical methodologies such as econometric techniques, experimental economics, or computational models.\nPolicy Relevance: Lacks discussion of real-world applications or policy implications.',
        'score 2': 'Partial Coverage with Notable Gaps\nScope: Covers 2-3 subfields (e.g., microeconomics and econometrics) but omits others (e.g., international trade, environmental economics).\nTheoretical Weaknesses: Briefly mentions theories like rational choice or game theory but does not compare competing frameworks (e.g., classical vs. behavioral economics).\nEmpirical Limitations: Discusses basic regression analysis but neglects advanced methods like causal inference, machine learning, or structural modeling.\nContextual Gaps: Fails to address historical evolution (e.g., post-2008 macroeconomic shifts) or interdisciplinary links (e.g., economics and sociology).',
        'score 3': 'Generally Comprehensive with Minor Omissions\nScope: Addresses most major subfields (e.g., macro/microeconomics, econometrics, development) but lacks depth in niche areas (e.g., health economics, auction theory).\nTheoretical Coverage: Explains core theories (e.g., supply-demand, Nash equilibrium) but provides limited critique or synthesis (e.g., debates on efficient markets).\nMethodological Range: Includes traditional and modern techniques (e.g., RCTs, DSGE models) but overlooks emerging tools (e.g., agent-based modeling, big data analytics).\nPolicy and Practice: Connects theories to policy design (e.g., taxation, monetary policy) but misses case studies or regional comparisons.',
        'score 4': 'Near-Exhaustive Coverage with Minimal Gaps\nScope: Systematically covers all major subfields and emerging areas (e.g., climate economics, inequality research).\nTheoretical Rigor: Analyzes foundational and contemporary theories (e.g., matching markets, network economics) with critical evaluations of their assumptions.\nMethodological Depth: Integrates diverse approaches, including structural econometrics, experimental designs, and AI-driven forecasting.\nPolicy Synthesis: Evaluates policy impacts across contexts (e.g., universal basic income trials, carbon pricing) and discusses trade-offs.\nInterdisciplinary Links: Explores connections to political science, psychology, and data science (e.g., behavioral nudges, algorithmic bias).',
        'score 5': 'Fully Comprehensive and Nuanced Coverage\nScope: Exhaustively addresses all subfields, including peripheral topics (e.g., cultural economics, cryptoeconomics) and cutting-edge trends (e.g., decentralized finance, pandemic economics).\nTheoretical Mastery: Synthesizes competing paradigms (e.g., neoclassical vs. heterodox economics) and charts their evolution over time.\nMethodological Innovation: Critiques traditional tools and highlights advances in causal machine learning, high-dimensional data analysis, and experimental ethics.\nPolicy and Global Relevance: Provides cross-country comparisons (e.g., Nordic vs. U.S. welfare systems) and assesses scalability of interventions (e.g., microfinance in developing nations).\nInterdisciplinary Integration: Bridges economics with climate science, public health, and AI ethics, addressing grand challenges like inequality and sustainability.'
    },
    "eess": {
        'description': 'Coverage evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical frameworks, system architectures, and engineering methodologies.',
        'score 1': 'Fragmentary Coverage\nSurveys exhibit severe omissions across fundamental EESS domains. Examples include:\n-No discussion of core power system components (generation, transmission, distribution) or foundational theories (Maxwell\'s equations, control system stability criteria).\n-Limited reference to standardized methodologies (e.g., IEEE reliability assessment protocols) or industry practices.\n-Complete absence of emerging trends like grid-edge technologies or cyber-physical system security frameworks.',
        'score 2': 'Partial Coverage with Major Gaps\nSurveys address isolated subdomains but lack systemic integration:\n-Covers traditional areas (e.g., analog circuit design) but omits modern counterparts (e.g., wide-bandgap semiconductor applications).\n-Mentions renewable energy systems superficially without analyzing grid integration challenges or storage solutions.\n-Fails to address critical interdisciplinary intersections (e.g., machine learning in fault detection, blockchain for energy transactions).',
        'score 3': 'Broad Coverage with Selective Depth\nSurveys demonstrate wide scope but uneven analytical rigor:\n-Encompasses major subfields (power electronics, signal processing, control systems) but provides cursory treatment of niche areas (e.g., microgrid resilience in extreme weather).\n-Discusses AI/ML applications but lacks comparative analysis of algorithms (e.g., LSTM vs. transformer models for load forecasting).\n-Identifies current challenges (e.g., grid decarbonization) without exploring solution pathways or policy implications.',
        'score 4': 'Comprehensive Coverage with Minor Omissions\nSurveys achieve near-exhaustive scope while maintaining technical depth:\n-Detailed analysis of conventional systems (transmission line modeling) and emerging paradigms (distributed energy resource management systems).\n-Integrates cross-domain insights (e.g., power quality implications of EV charging infrastructure).\n-Minor gaps may exist in rapidly evolving areas (e.g., quantum computing applications in grid optimization) or regional-specific case studies.',
        'score 5': 'Encyclopedic Coverage with Future-Oriented Synthesis\nSurveys set benchmark standards through:\n-Exhaustive treatment of all EESS strata: from foundational principles (Kron\'s reduction in network analysis) to speculative innovations (neuromorphic computing for real-time grid control).\n-Critical synthesis of competing methodologies (e.g., comparative review of SCADA vs. IoT-based grid monitoring systems).\n-Forward-looking analysis of socio-technical trends (e.g., regulatory frameworks for AI-driven energy markets).'
    },
    "math": {
        'description': 'Coverage evaluation specific to Mathematics surveys, focusing on mathematical coherence, logical progression, and theoretical frameworks.',
        'score 1': 'Incomplete and Superficial Coverage\nScope: Limited to a narrow subtopic without contextualizing its place in broader mathematics.\nKey Areas: Fails to address foundational theories, major subfields (e.g., algebra, topology, applied mathematics), or seminal results.\nMethodologies: Omits critical proof techniques, computational tools, or analytical frameworks.\nApplications: Lacks discussion of real-world applications (e.g., cryptography, physics) or interdisciplinary links.\nRecent Trends: Excludes advancements from the past decade, rendering the survey outdated.\nOpen Problems: Does not identify unresolved conjectures or future research directions.\nExample: A survey on algebraic geometry that ignores scheme theory or fails to mention Grothendieck\'s contributions.',
        'score 2': 'Partial Coverage with Significant Gaps\nScope: Addresses a few subfields but neglects others of comparable importance.\nKey Areas: Mentions major theorems (e.g., Fermat\'s Last Theorem) but lacks depth in their proofs or implications.\nMethodologies: Describes only elementary methods (e.g., classical analysis) while omitting modern approaches (e.g., category-theoretic frameworks).\nApplications: Superficially notes applications without detailing mathematical underpinnings (e.g., mentioning fluid dynamics without Navier-Stokes equations).\nRecent Trends: Cites fewer than 30% of pivotal post-2015 papers in the field.\nOpen Problems: Lists open questions without contextualizing their significance or connecting them to existing work.\nExample: A survey on graph theory that covers basic combinatorics but excludes spectral graph theory or network science applications.',
        'score 3': 'Broad but Uneven Coverage\nScope: Surveys most major subfields but underrepresents emerging areas (e.g., machine learning-driven mathematics).\nKey Areas: Explains central results (e.g., Gödel\'s incompleteness theorems) but overlooks nuanced extensions (e.g., reverse mathematics).\nMethodologies: Reviews standard techniques (e.g., variational methods) but neglects computational advancements (e.g., automated theorem proving).\nApplications: Discusses applications in physics/engineering but omits newer domains (e.g., blockchain cryptography).\nRecent Trends: Includes 50-70% of post-2020 literature but misses key breakthroughs (e.g., progress on the Riemann hypothesis).\nOpen Problems: Identifies major conjectures (e.g., P vs. NP) but does not analyze partial results or proposed strategies.\nExample: A survey on differential equations that covers PDEs but inadequately addresses stochastic DEs or numerical solvers.',
        'score 4': 'Near-Comprehensive Coverage\nScope: Systematically reviews all major subfields and select niche areas (e.g., tropical geometry).\nKey Areas: Details proofs, historical evolution (e.g., from Euclidean to non-Euclidean geometry), and paradigm shifts (e.g., Langlands program).\nMethodologies: Compares classical and modern approaches (e.g., analytic vs. algebraic number theory) and evaluates their efficacy.\nApplications: Examines interdisciplinary impact (e.g., algebraic topology in data science) with specific mathematical examples.\nRecent Trends: Integrates 80-90% of critical post-2020 advances, including preprints from arXiv.\nOpen Problems: Synthesizes unresolved issues (e.g., Birch and Swinnerton-Dyer conjecture) with current progress and barriers.\nExample: A survey on quantum computing algorithms that covers Shor\'s algorithm, topological quantum codes, and recent hybrid classical-quantum methods.',
        'score 5': 'Exhaustive and Insightful Coverage\nScope: Spans all relevant subfields, peripheral topics (e.g., homotopy type theory), and cutting-edge intersections (e.g., AI-driven conjecture generation).\nKey Areas: Provides rigorous analysis of landmark results (e.g., Perelman\'s proof of the Poincaré conjecture) and their methodological implications.\nMethodologies: Critiques tools across abstraction levels (e.g., Coq formalization vs. intuitive heuristics) and contextualizes their use cases.\nApplications: Explores mathematical impact in unexpected domains (e.g., algebraic statistics in genomics) with technical depth.\nRecent Trends: Exhaustively surveys post-2020 literature, including niche preprints and conference proceedings.\nOpen Problems: Maps the landscape of unsolved problems (e.g., Yang-Mills existence), links them to active research programs, and proposes novel pathways.\nExample: A survey on elliptic curves that integrates arithmetic geometry, cryptographic applications, modularity theorems, and the ABC conjecture\'s implications.'
    },
    "physics": {
        'description': 'Coverage evaluation specific to Physics surveys, focusing on physical relevance, foundational works, and experimental validation.',
        'score 1': 'Fragmentary Coverage\nFails to address core subfields or methodologies. The survey omits major branches of the topic (e.g., neglecting experimental validation while focusing solely on theoretical frameworks) and lacks references to seminal works. For example, a review on quantum gravity that excludes loop quantum gravity or string theory would score here. Peripheral topics (e.g., interdisciplinary applications in condensed matter systems) are entirely absent, and citations are limited to outdated or niche studies.',
        'score 2': 'Partial Coverage with Critical Gaps\nAddresses isolated aspects but misses structurally important components. While introducing basic concepts (e.g., Maxwell\'s equations in electromagnetism surveys), the review overlooks pivotal advancements like transformation optics or meta-material applications. Methodological diversity is sparse-computational approaches may be mentioned without discussing Monte Carlo simulations or finite-element analysis. Key subfields (e.g., non-equilibrium thermodynamics in a statistical mechanics survey) are underrepresented, and citation of post-2020 breakthroughs is inconsistent.',
        'score 3': 'Broad but Superficial Coverage\nCovers major subfields unevenly, with variable depth. The survey outlines central theories (e.g., Standard Model physics) but provides minimal analysis of unresolved issues like the hierarchy problem. Experimental techniques (e.g., cryogenic particle detectors) are listed without critiquing their sensitivity limits or scalability. While recent studies (2018-2023) are cited, their implications for future research are not synthesized. Cross-disciplinary links (e.g., machine learning in astrophysical data analysis) are acknowledged but lack technical specificity.',
        'score 4': 'Near-Complete Coverage with Minor Omissions\nSystematically addresses >90% of critical topics and methodologies. Foundational theories (e.g., quantum field theory renormalization) are contextualized with modern extensions like effective field theories. Emerging areas (e.g., quantum machine learning in high-energy physics) receive dedicated subsections, though niche applications (e.g., topological solitons in biophysics) may be abbreviated. Methodological critiques compare lattice QCD with tensor network approaches, noting computational trade-offs. Citations include landmark pre-2010 papers and >15 post-2020 studies, but a few influential preprints (e.g., arXiv:2303.11696) are omitted.',
        'score 5': 'Encyclopedic Coverage\nExhaustively integrates all major and peripheral dimensions. The survey delineates historical evolution (e.g., path from SU(5) unification to modern string theory compactifications), current challenges (e.g., baryogenesis in beyond-Standard-Model cosmologies), and methodological frontiers (e.g., Bayesian inference in gravitational-wave parameter estimation). Interdisciplinary bridges (e.g., quantum error correction in neuromorphic computing) are analyzed through physics-first principles. All subsections balance theoretical rigor (e.g., Ward-Takahashi identities in gauge theories) with empirical validations (e.g., LHC constraints on supersymmetry). Citations span 50+ sources, including 10+ preprints from 2023-2024 and seminal works from the 20th century.'
    },
    "q-bio": {
        'description': 'Coverage evaluation specific to Quantitative Biology surveys, focusing on biological relevance, computational methods, and interdisciplinary integration.',
        'score 1': 'Very Limited Coverage\nScope: Focuses narrowly on a single technique, model, or biological subsystem without contextualizing its role in broader quantitative frameworks.\nKey Omissions: Fails to address foundational methodologies (e.g., fluorescence microscopy, next-generation sequencing, or statistical genetics), omits interdisciplinary connections (e.g., physics-biology integration), and neglects major subfields (e.g., evolutionary quantitative genetics or omics data analysis).\nExamples: A survey on protein structure prediction that ignores deep learning advancements or omits discussion of experimental validation pipelines.',
        'score 2': 'Partial Coverage with Significant Gaps\nScope: Addresses 2-3 major topics but lacks depth or misses critical subtopics.\nKey Omissions:\n-Fails to integrate instrumented techniques (e.g., quantitative microscopy pitfalls) with computational workflows (e.g., Bioconductor tools).\n-Overlooks data challenges (e.g., batch effects in sequencing, photobleaching in imaging) or statistical frameworks (e.g., hypothesis testing in genomics).\n-Excludes emerging areas like single-cell omics or machine learning in ecology.\nExamples: A review of genomic heritability that does not discuss environmental confounding factors or a survey on imaging without addressing scattering artifacts.',
        'score 3': 'Generally Comprehensive with Minor Omissions\nScope: Covers core methodologies (e.g., microscopy, sequencing, statistical models) and major biological applications (e.g., gene expression, evolutionary adaptations).\nKey Strengths:\n-Discusses quantitative pitfalls (e.g., autofluorescence, sampling bias).\n-Integrates multiscale approaches (e.g., linking molecular dynamics to population genetics).\nKey Omissions:\n-Limited exploration of interdisciplinary tools (e.g., physics-based models in plant biology).\n-Superficial treatment of educational challenges (e.g., student difficulties in quantitative topics) or ethics in data-intensive biology.\nExamples: A survey on deep learning in proteomics that neglects physics-inspired neural architectures or experimental validation benchmarks.',
        'score 4': 'Near-Complete Coverage with Minimal Gaps\nScope: Systematically addresses most subfields, including instrumentation, data science, theory, and applications.\nKey Strengths:\n-Details workflow integration (e.g., from image acquisition to topological data analysis).\n-Explores cross-disciplinary links (e.g., statistical genetics in ecology or physics in plant hydraulics).\n-Includes practical considerations (e.g., reproducibility in omics, survey design).\nMinor Omissions:\n-Lacks depth in niche areas (e.g., non-coding RNA in viral latency or stereology in histology).\n-Does not fully address translational impacts (e.g., clinical applications of quantitative models).\nExamples: A review of quantitative microscopy that covers scattering artifacts but omits recent advances in cryo-electron tomography.',
        'score 5': 'Exhaustive Coverage of Key and Peripheral Topics\nScope: Holistically synthesizes all major and emerging areas, including:\nCore Techniques: Fluorescence microscopy, sequencing, mass spectrometry, and sensor technologies.\nAnalytic Frameworks: Deep learning, Bayesian statistics, topological data analysis, and multiscale modeling.\nBiological Systems: Molecular networks, cellular dynamics, organismal adaptations, and ecosystem-level patterns.\nMeta-Science Topics: Reproducibility, education, ethics, and interdisciplinary collaboration.\nKey Strengths:\n-Balances depth (e.g., photobleaching correction algorithms) with breadth (e.g., evolutionary implications of sperm morphology).\n-Anticipates future trends (e.g., AI-driven hypothesis generation or quantum computing in genomics).\n-Critically evaluates method trade-offs (e.g., resolution vs. throughput in imaging).\nExamples: A survey on self-organization that integrates order parameters, ecological case studies, and educational frameworks for teaching complexity.'
    },
    "q-fin": {
        'description': 'Coverage evaluation specific to Quantitative Finance surveys, focusing on financial models, mathematical frameworks, and market applications.',
        'score 1': 'Fragmentary Coverage\nLimited discussion of canonical topics (e.g., Black-Scholes model, Markowitz optimization) with no critical analysis of their assumptions or limitations.\nOmits major subfields such as derivative pricing, risk management, or market microstructure.\nFails to address interdisciplinary connections (e.g., econometrics, operations research).',
        'score 2': 'Partial Overview\nCovers basic models (e.g., CAPM, VaR) but lacks depth in advanced techniques (e.g., Lévy processes, rough volatility).\nMentions 1-2 subfields (e.g., algorithmic trading) but neglects others (e.g., fixed-income analytics, credit risk modeling).\nSuperficial treatment of computational methods (e.g., Monte Carlo simulations, finite difference schemes).',
        'score 3': 'Moderate Integration\nSurveys traditional ML applications (e.g., portfolio optimization with neural networks) but omits cutting-edge approaches (e.g., transformers for high-frequency data).\nDiscusses supervised learning but inadequately addresses reinforcement learning or generative models in trading.\nLimited analysis of data challenges (e.g., low signal-to-noise ratios, survivorship bias).',
        'score 4': 'Robust Synthesis\nSystematically reviews ML paradigms (e.g., graph neural networks for systemic risk, NLP for earnings call analysis).\nCompares hybrid models (e.g., physics-informed neural networks for option pricing) against classical methods.\nCritically evaluates implementation hurdles (e.g., latency in reinforcement learning, overfitting in backtests).',
        'score 5': 'Exhaustive Scope\nExplores frontier areas:\n-DeFi: Automated market makers, liquidity pool dynamics, MEV (miner-extractable value).\n-ESG integration: Climate risk modeling, green portfolio optimization.\n-Quantum finance: Quantum algorithms for arbitrage detection, portfolio rebalancing.\nSynthesizes cross-disciplinary insights (e.g., behavioral finance meets deep learning).\nProvides taxonomies for emerging research directions (e.g., federated learning in cross-asset strategies).'
    },
    "stat": {
        'description': 'Coverage evaluation specific to Statistics surveys, focusing on statistical frameworks, methodological approaches, and theoretical foundations.',
        'score 1': 'Fragmentary Coverage\nDiscusses ≤2 major statistical paradigms (e.g., only frequentist methods without Bayesian counterparts)\nOmits foundational components: No mention of core concepts like likelihood theory, experimental design, or asymptotic theory\nLacks application contexts: Fails to connect methods to real-world implementations in healthcare, econometrics, or spatial statistics\nIgnores 75%+ of essential subtopics (e.g., covers regression but excludes survival analysis, causal inference, and nonparametric methods)',
        'score 2': 'Partial Coverage with Critical Gaps\nAddresses 3-4 statistical domains but with uneven depth (e.g., detailed ML methods but superficial treatment of traditional time-series analysis)\nMissing ≥2 major methodological pillars: Omits key areas like Bayesian computation, robust statistics, or high-dimensional inference\nLimited application spectrum: Only demonstrates methods through toy examples without substantive case studies from genomics or official statistics\nOverlooks 50-75% of expected content: Fails to discuss modern developments like conformal prediction or federated learning architectures',
        'score 3': 'Substantive but Incomplete Coverage\nCovers 5-6 core areas with reasonable balance (e.g., includes GLMs, MCMC, and causal diagrams but gives sparse attention to spatial statistics)\nAddresses both frequentist and Bayesian paradigms but lacks depth in emerging hybrid approaches\nProvides application examples in 2-3 domains (clinical trials, social networks) but omits critical implementations in environmental monitoring or official surveys\nMisses 25-50% of expected content: Includes traditional experimental design but neglects adaptive trial methodologies and digital twin applications',
        'score 4': 'Near-Exhaustive Coverage\nSystematically reviews ≥7 statistical domains with technical rigor (e.g., survival analysis, causal inference, ML integration, and measurement error models)\nBalances classical theory (Neyman-Pearson lemma, EM algorithm) with modern computational methods (variational inference, Hamiltonian Monte Carlo)\nDemonstrates applications across 4-5 substantive fields: Includes detailed case studies in pharmacometrics, astronomical surveys, and census data harmonization\nOmits ≤2 niche areas: May lack coverage of specialized topics like functional data analysis for motion capture or exoplanet detection statistics',
        'score 5': 'Encyclopedic Coverage\nExhaustively documents all major statistical paradigms: Includes decision-theoretic frameworks, empirical Bayes methods, and pre-registration protocols\nIntegrates cutting-edge developments: Covers differentiable programming, quantum statistical models, and AI-assisted survey methodology\nProvides cross-domain implementation templates: Details applications in rare disease epidemiology, dark matter detection, and multinational policy evaluation\nAddresses peripheral innovations: Discusses ethical considerations in algorithmic fairness, reproducibility crisis solutions, and FAIR data standards\nIncludes meta-analytical depth: Compares methodological performance through simulation studies and real-data benchmarks across 10+ application scenarios'
    }
}

STRUCTURE_DOMAIN_CRITERIA = {
    "cs": {
        'description': 'Structure evaluation specific to Computer Science surveys, focusing on technical organization, methodological frameworks, and computational approaches.',
        'score 1': 'Disjointed Technical Narrative\nLacks fundamental CS survey components (e.g., problem taxonomies, methodology comparison tables, algorithmic analysis)\nPresents technical concepts in isolation without connecting foundational theories to modern applications\nFails to distinguish between computer science subdomains (e.g., conflating machine learning principles with cybersecurity architectures)\nContains redundant technical explanations across sections without progressive complexity',
        'score 2': 'Partial Technical Organization\nIdentifies key CS domains but struggles with cross-paradigm comparisons (e.g., imperative vs. functional programming paradigms)\nTechnical timelines mix historical developments with contemporary innovations without clear phase demarcation\nVisual aids (algorithm pseudocode, architecture diagrams) appear disconnected from textual explanations\nTransitional phrases exist but fail to bridge technical complexity gradients between sections',
        'score 3': 'Conventional Technical Flow\nFollows standard CS survey structure: abstract → problem space → methodology review → case studies → future directions\nTechnical content organized by computational complexity levels (e.g., separating polynomial-time algorithms from NP-hard solutions)\nContains basic comparative tables for algorithm complexity or system architectures\nTransitions use technical signposting (e.g., "Having discussed asymptotic analysis, we now examine practical runtime constraints") but lack depth in connecting theoretical and applied aspects',
        'score 4': 'Cohesive Technical Synthesis\nEmploys adaptive structure matching CS subfield requirements (e.g., separate hardware/software stacks in embedded systems surveys)\nTechnical progression follows computational dependency chains (e.g., prerequisite algorithms introduced before dependent systems)\nIntegrates interactive elements for complex topics (expandable proof sketches, clickable architecture diagrams in digital formats)\nMaintains parallel technical narratives for different computational paradigms (e.g., quantum vs. classical computing comparisons)',
        'score 5': 'Innovative Computational Architecture\nFeatures subfield-tailered structures (e.g., timeline matrices for AI evolution, multidimensional taxonomies for cybersecurity threats)\nTechnical transitions employ computational metaphors (e.g., "This neural architecture naturally composes with the previously discussed optimization pipeline as shown in Figure 3")\nContains self-adaptive sections that adjust depth based on cited evidence density and impact factors\nImplements formal verification of structural logic through computational models (e.g., dependency graphs validating citation flow)\nIntroduces novel organizational paradigms for emerging CS domains (e.g., hybrid quantum-classical algorithm surveys with entanglement-aware grouping)'
    },
    "econ": {
        'description': 'Structure evaluation specific to Economics surveys, focusing on theoretical frameworks, empirical methodologies, and policy implications.',
        'score 1': 'Disjointed Economic Narrative\nFails to distinguish between microeconomic and macroeconomic perspectives\nNo clear progression from theoretical models to empirical validation\nMixes heterodox and mainstream economic theories without contextualization\nLacks sections on policy implications or welfare economics considerations\nOmits standard economics survey components (e.g., stylized facts, identification strategies)',
        'score 2': 'Partial Economic Framework\nBasic separation of topics (e.g., labor vs monetary economics) but weak thematic integration\nLimited connection between econometric methods and empirical findings\nSuperficial treatment of causal inference techniques in policy evaluation\nInconsistent use of economic models across sections\nTransitional phrases ignore important economic relationships (e.g., price-quantity linkages)',
        'score 3': 'Conventional Economic Organization\nStandard structure (theory → methods → applications) with basic coherence\nIdentifies major economic schools of thought but limited critical synthesis\nContains expected sections (welfare analysis, equilibrium models) with some redundancy\nModerate success in linking microfoundations to macroeconomic outcomes\nBasic transitions between neoclassical and behavioral economic paradigms',
        'score 4': 'Sophisticated Economic Architecture\nExplicit mapping of economic theory to empirical testing protocols\nEffective integration of structural vs reduced-form approaches\nClear progression from identification strategies to policy relevance\nThematic clustering of related economic subfields (e.g., labor/education economics)\nTransitions highlight economic mechanisms (e.g., general equilibrium effects)',
        'score 5': 'Masterful Economic Synthesis\nUnified framework reconciling competing economic paradigms\nHierarchical organization of models by assumptions and predictive power\nSeamless integration of causal inference methods with economic theory\nDynamic structure adapting to heterodox vs mainstream debates\nTransitions explicitly model economic relationships (e.g., elasticity substitutions)'
    },
    "eess": {
        'description': 'Structure evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical frameworks, system architectures, and engineering methodologies.',
        'score 1': 'Disjointed Technical Narrative\nPresents concepts in random order without alignment to EE methodologies (e.g., mixing control theory with semiconductor physics without justification)\nFails to separate foundational principles (e.g., Maxwell\'s equations) from applied domains (e.g., power systems)\nContains redundant technical explanations across sections (e.g., repeating matrix decomposition methods in signal processing and machine learning chapters)\nLacks standardized section hierarchy (e.g., missing "Challenges in Smart Grid Cybersecurity" subsection under "Energy Systems" section)',
        'score 2': 'Partial Technical Organization\nGroups related EE topics (e.g., power electronics and renewable energy systems) but provides weak justification for their sequence\nCreates ambiguous subsection boundaries (e.g., overlapping content between "Optimization Algorithms" and "Energy Management Systems")\nUses inconsistent depth in technical explanations (e.g., detailed semiconductor physics vs. superficial treatment of control theory)\nContains abrupt shifts between mathematical formalism (e.g., differential equations) and applied case studies without transitional paragraphs',
        'score 3': 'Functionally Structured Technical Survey\nFollows EE research lifecycle structure: 1) Fundamental principles 2) Implementation architectures 3) Validation methodologies 4) Emerging applications\nImplements modular section design for complex systems (e.g., separate "Communication Protocols" and "Hardware Security" subsections under IoT chapter)\nMaintains consistent technical depth using EE standards (e.g., IEEE format for equations, SI units in measurements)\nIncludes transitional paragraphs connecting theory to practice (e.g., "The Kalman filter derivation above enables the following state estimation applications in smart grids...")',
        'score 4': 'Cohesive Systems-Oriented Architecture\nEmploys systems engineering V-model structure: Requirements → Design → Verification → Deployment\nImplements cross-layer analysis (e.g., linking device-level semiconductor characteristics to grid-level stability impacts)\nUses standardized EE taxonomy (IEEE Thesaurus terms) for subsection headers\nFeatures matrix-based transitional devices (e.g., "Table 3 compares the surveyed power flow algorithms against the criteria established in Section 2")\nContains only minor structural imperfections (e.g., slightly disproportionate emphasis on embedded systems vs. power electronics)',
        'score 5': 'Optimized Technical Synthesis Structure\nImplements recursive systems framework:\n-Fundamentals: ∇⋅D=ρv(Maxwell\'s Equations)\n-Subsystems: Power electronics ↔ Control theory interfaces\n-Integration: Cyber-physical system co-design\n-Validation: Hardware-in-the-loop testing methodologies\nFeatures context-aware transitions:\n-"The semiconductor physics discussed in Section 2.1 directly enables the wide-bandgap devices analyzed in Section 3.2"\n-"These communication protocols (Section 4.3) address the latency constraints identified in the smart grid requirements (Section 1.2)"\nIncludes dynamic structural elements:\n-Adaptive depth control via technical appendices for specialized topics (e.g., detailed derivation of space vector modulation)\n-Cross-referential matrices linking theoretical models  to application case studies\nDemonstrates Pareto-optimal content distribution between:\n-Mathematical formalism (20-25%)\n-Implementation architectures (35-40%)\n-Comparative analysis (25-30%)\n-Future research vectors (10-15%)'
    },
    "math": {
        'description': 'Structure evaluation specific to Mathematics surveys, focusing on mathematical coherence, logical progression, and theoretical frameworks.',
        'score 1': 'Disjointed Framework\nLogical Flow: No discernible progression of ideas; sections lack purpose or connection.\nSection Organization: Content appears randomly ordered (e.g., advanced theorems precede definitions).\nTransitions: Abrupt shifts between topics without justification (e.g., switching from algebraic geometry to stochastic calculus without contextual linkage).\nRedundancy: Critical repetitions of definitions/results without incremental value.\nTaxonomy: Fails to classify mathematical paradigms (e.g., conflating analytical and combinatorial methods).',
        'score 2': 'Fragmented Structure\nLogical Flow: Partial coherence with isolated logical leaps (e.g., introducing PDE applications before establishing variational principles).\nSection Organization: Subsections misaligned with parent sections (e.g., "Topological Data Analysis" nested under "Linear Algebra").\nTransitions: Minimal bridging phrases (e.g., "Next, we discuss..." without explaining relevance).\nRedundancy: Overlapping case studies in distinct sections (e.g., re-proving Bézout\'s theorem in both algebraic geometry and cryptography sections).\nTaxonomy: Incomplete categorization (e.g., omitting key subfields of category theory).',
        'score 3': 'Functionally Adequate\nLogical Flow: Generally sequential but with minor gaps (e.g., delayed motivation for abstract measure theory in probability surveys).\nSection Organization: Subsections logically grouped but occasionally misplaced (e.g., "Graph Isomorphism" under "Complexity Classes" instead of "Discrete Mathematics").\nTransitions: Formulaic connectors (e.g., "Having discussed X, we now consider Y") without deeper synthesis.\nRedundancy: Limited unintentional overlaps (e.g., restating Banach fixed-point theorem in both functional analysis and dynamical systems).\nTaxonomy: Basic classification of methods/theorems but lacks subfield granularity (e.g., grouping all optimization techniques under "Calculus of Variations").',
        'score 4': 'Cohesive Architecture\nLogical Flow: Purposeful sequencing with few discontinuities (e.g., deriving stochastic differential equations before exploring their numerical approximations).\nSection Organization: Subsections align with parent themes (e.g., "Elliptic Curve Cryptography" nested under "Number Theory Applications").\nTransitions: Contextualized pivots (e.g., "The preceding homological algebra framework naturally extends to..." followed by examples).\nRedundancy: Strategic repetition only for emphasis (e.g., restating key lemmas before major proofs).\nTaxonomy: Multilevel classifications (e.g., partitioning optimization into convex, non-convex, and stochastic subfields with technique-specific subtrees).',
        'score 5': 'Exemplary Synthesis\nLogical Flow: Seamless progression from foundations to frontiers (e.g., beginning with Hilbert spaces, advancing to spectral theory, concluding with quantum computing applications).\nSection Organization: Hierarchical nesting of concepts (e.g., "Manifold Learning" → "Riemannian Geometry" → "Information Geometry").\nTransitions: Thematic threads'
    },
    "physics": {
        'description': 'Structure evaluation specific to Physics surveys, focusing on physical relevance, foundational works, and experimental validation.',
        'score 1': 'The survey lacks coherence, with disjointed sections and no identifiable thematic framework. Key physics concepts (e.g., theoretical foundations, methodologies, applications) are presented haphazardly, and transitions between topics are abrupt or nonexistent. Redundant subsections or misplaced content (e.g., experimental methods in a theory-focused section) obscure the narrative.',
        'score 2': 'The survey exhibits weak thematic organization, with sections loosely grouped by broad topics (e.g., "Theoretical Background" or "Applications") but lacking sub-structure. Transitions between physics subfields (e.g., classical mechanics to quantum systems) are poorly justified, and connections to overarching research trends (e.g., machine learning in physics) are superficial. Some subsections repeat ideas or fail to align with the paper\'s stated scope.',
        'score 3': 'The survey has a recognizable structure (e.g., theory → methods → applications → challenges) but lacks depth in subfield integration. Transitions between foundational physics principles (e.g., Newtonian mechanics) and modern advancements (e.g., AI-driven simulations) are functional but formulaic. Subsections exist but may omit critical linkages (e.g., multiscale modeling in materials science ) or overemphasize niche topics.',
        'score 4': 'The survey demonstrates strong logical flow, with sections organized by physics themes (e.g., "Quantum Computing Architectures" or "Multiphase Fluid Dynamics") and subsections addressing specific methodologies (e.g., lattice Boltzmann methods ) or applications (e.g., medical physics ). Transitions between experimental, theoretical, and computational approaches are purposeful, though occasional gaps remain (e.g., insufficient discussion of cross-scale interactions ). Recent advancements (e.g., physics-informed machine learning ) are contextualized within historical frameworks.',
        'score 5': 'The survey is masterfully structured, with a tightly woven narrative that integrates foundational physics principles, cutting-edge methodologies, and interdisciplinary applications. Sections are hierarchically organized (e.g., "Fundamental Theories" → "Computational Advances" → "Emerging Applications") and subsections explore nuanced topics (e.g., baryonic feedback in cosmology , tensor networks in quantum simulations ). Transitions highlight causal relationships (e.g., how discretization techniques enable large-scale fluid simulations ) and synthesize multidisciplinary insights (e.g., biomechanics and fracture modeling ). The framework anticipates reader needs, balancing depth with accessibility, and concludes with forward-looking syntheses of open challenges (e.g., validation gaps in additive manufacturing ).'
    },
    "q-bio": {
        'description': 'Structure evaluation specific to Quantitative Biology surveys, focusing on biological relevance, computational methods, and interdisciplinary integration.',
        'score 1': 'The survey lacks a coherent framework, with no discernible thematic or methodological organization. Sections are disjointed, failing to establish connections between biological concepts, computational methods, and applications. Critical elements such as categorization of techniques (e.g., sequence-based vs. structure-based methods) or evaluation metrics (e.g., precision-recall curves for protein function prediction) are absent or poorly defined. Transitions between topics are abrupt, and the paper does not guide readers through foundational principles, advancements, or future challenges in quantitative biology.',
        'score 2': 'The survey exhibits fragmented logic, with limited alignment to the core themes of quantitative biology. While some sections (e.g., "Deep Learning Applications") are identifiable, their arrangement lacks a unifying narrative. Methodological categories (e.g., hybrid information-based approaches) are mentioned but not systematically compared. Descriptions of biological datasets (e.g., protein interaction networks) or computational frameworks (e.g., graph neural networks) are inconsistently integrated, leading to redundancy or gaps in coverage. Transitions between traditional and modern techniques (e.g., from BLAST to AlphaFold) are underdeveloped.',
        'score 3': 'The survey demonstrates a basic organizational structure, with sections broadly aligned to quantitative biology standards (e.g., IMRaD format). Methodological categories (sequence-based, structure-based, network-based) are defined but lack critical analysis of their trade-offs in specific biological contexts. Evaluative components (e.g., benchmarking on CASP or CAFA datasets) are included but not contextualized within broader biological challenges. Transitions between subsections (e.g., "Data Sources" to "Model Architectures") are functional but formulaic, with occasional repetition of concepts like "encoder-decoder frameworks" without progressive depth.',
        'score 4': 'The survey is logically structured, with clear alignment to quantitative biology paradigms. Major sections (e.g., "Evolution of Protein Function Prediction Methods") are subdivided into thematic pillars (e.g., phylogenetic profiling, multi-omics integration), each analyzed through computational and biological lenses. Methodological comparisons (e.g., accuracy of residue contact prediction in AlphaFold vs. RoseTTAFold) are supported by quantitative metrics (e.g., root-mean-square deviation). Transitions between foundational concepts (e.g., sequence alignment algorithms) and emerging areas (e.g., language models for protein design) are smooth, though deeper synthesis of interdisciplinary implications (e.g., clinical translation) could enhance cohesion.',
        'score 5': 'The survey exemplifies a masterfully organized framework, seamlessly integrating quantitative rigor with biological relevance. Sections are hierarchically structured to reflect the field\'s complexity-for example, distinguishing data types (omics, imaging), methodologies (physics-based simulations, deep learning), and applications (drug discovery, synthetic biology). Subsections critically evaluate method families (e.g., convolutional vs. transformer architectures for protein folding) using domain-specific benchmarks (e.g., TM-score, pLDDT). The narrative progresses from historical context (e.g., homology modeling) to cutting-edge advancements (e.g., diffusion models for protein generation), culminating in a unified discussion of open challenges (e.g., interpretability of AI models in wet-lab validation). Transitions are purposeful, such as linking hierarchical learning frameworks (e.g., ProtBoost\'s use of Gene Ontology) to real-world biological scalability. Redundancy is absent, with each section building upon prior insights to create a cumulative, interdisciplinary perspective.'
    },
    "q-fin": {
        'description': 'Structure evaluation specific to Quantitative Finance surveys, focusing on financial models, mathematical frameworks, and market applications.',
        'score 1': 'Disjointed Framework\nStructural flaws: No discernible progression between foundational theories (e.g., stochastic calculus), computational methods (e.g., Monte Carlo simulations), and financial applications (e.g., derivative pricing).\nContent gaps: Missing critical components of quantitative finance pipelines such as data preprocessing techniques, backtesting protocols, or risk management considerations.\nThematic chaos: Random sequencing of topics without differentiation between established practices (e.g., Black-Scholes models) and emerging paradigms (e.g., quantum portfolio optimization).\nTransition failures: Abrupt jumps between mathematical formulations and empirical results without explanatory bridges.',
        'score 2': 'Partial Coherence with Notable Deficits\nWeak methodological linkage: Superficial treatment of connections between econometric models (e.g., GARCH) and machine learning approaches (e.g., LSTM networks).\nIncomplete taxonomy: Cursory categorization of financial models without clear differentiation between parametric (e.g., HJM framework) and non-parametric approaches (e.g., neural SDEs).\nTemporal disorganization: Historical developments in quantitative methods presented out of chronological sequence, obscuring evolutionary patterns.\nSection imbalance: Overemphasis on theoretical constructs (e.g., measure changes) with inadequate coverage of implementation challenges (e.g., numerical stability in PDE solvers).',
        'score 3': 'Functional Organization with Improvement Opportunities\nBasic pipeline structure: Recognizable progression from data sources → feature engineering → model development → performance validation, but lacks depth in explaining interdependencies.\nModerate cross-referencing: Some connections drawn between financial mathematics (e.g., Ito calculus) and computational techniques (e.g., finite difference methods), but misses opportunities for synthesis.\nEmerging trends addressed: Includes sections on AI/ML applications or quantum algorithms, but treats them as isolated additions rather than integrated components.\nTransition adequacy: Uses standard section bridges ("Having discussed X, we now consider Y") but lacks thematic continuity between mathematical theory and trading system architectures.',
        'score 4': 'Professional-Grade Structure\nPipeline optimization: Explicit mapping of model development stages from hypothesis formulation (e.g., arbitrage detection) to deployment challenges (e.g., latency constraints).\nInterdisciplinary synthesis: Effective integration of financial economics principles with computational statistics (e.g., explaining Bayesian methods in volatility surface calibration).\nTemporal layering: Clear delineation of historical milestones (Markowitz optimization), current practices (risk parity strategies), and frontier research (ZK-SNARKs for private trading).\nDynamic transitions: Purposeful sequencing between adjacent sections using financial motivation→mathematical formalization→empirical validation patterns.',
        'score 5': 'Exemplary Architectural Design\nHolistic integration: Seamless weaving of theoretical models, numerical implementations, and regulatory considerations throughout all sections (e.g., linking CVA computations to Basel III requirements).\nInnovative taxonomy: Original classification frameworks that reveal hidden connections between disparate domains (e.g., topological data analysis in market microstructure studies).\nAnticipatory structure: Sections naturally flow from well-established techniques (PCA for yield curve modeling) to cutting-edge approaches (attention mechanisms in limit order book prediction).\nRecursive reinforcement: Key concepts reintroduced at multiple abstraction levels (e.g., stochastic integration first as mathematical tool, later as risk factor aggregator).\nMeta-commentary: Explicit discussion of structural choices explaining why certain model families (structural vs reduced-form) receive particular organizational emphasis'
    },
    "stat": {
        'description': 'Structure evaluation specific to Statistics surveys, focusing on statistical frameworks, methodological approaches, and theoretical foundations.',
        'score 1': 'Disjointed Framework\nContains fragmented discussions of statistical methods without mathematical connections\nFails to distinguish between core theory and application variants (e.g., conflates kernel density estimation with nonparametric regression)\nLacks standard statistical survey components: No separate methodology comparison, assumption analysis, or error propagation sections',
        'score 2': 'Partial Organization\nIdentifies major statistical domains but provides uneven depth (e.g., detailed treatment of regression analysis while superficially covering time series)\nAttempts methodological categorization but mixes abstraction levels (e.g., discusses EM algorithm without connecting to general missing data frameworks)\nContains redundant mathematical presentations (e.g., rederives basic probability theorems across multiple sections)',
        'score 3': 'Coherent Baseline\nGroups methods by statistical families (parametric vs. nonparametric, frequentist vs. Bayesian) with adequate mathematical definitions\nFollows standard progression: Probability foundations → Estimation theory → Hypothesis testing → Advanced topics\nIncludes comparative tables of estimator properties (bias, variance, convergence rates) but lacks synthesis across tables',
        'score 4': 'Integrated Architecture\nEmbeds computational advancements within theoretical frameworks (e.g., places Markov chain Monte Carlo within Bayesian computation legacy)\nFeatures specialized structural elements:\n-Assumption Taxonomies: Hierarchical breakdown of model prerequisites (e.g., linear regression conditions vs. generalized additive model requirements)\n-Convergence Bridges: Explicit links between asymptotic theory and finite-sample properties\nEmploys transitional devices connecting mathematical proofs to practical implementation challenges',
        'score 5': 'Exemplary Statistical Synthesis\nThematic Modularity: Self-contained sections for methodological paradigms (e.g., likelihood-based inference, resampling methods) with cross-referenced connections\nMultilayer Organization:\n-Foundational Layer: Measure-theoretic probability, estimation theory\n-Methodological Layer: Regression analysis, multivariate analysis, experimental design\n-Computational Layer: EM algorithm variations, bootstrap implementations, MCMC innovations\nDynamic Flow Mechanisms:\n-Conceptual Cascades: Natural progression from point estimation → interval estimation → hypothesis testing\n-Methodological Phylogenies: Visual mappings of statistical technique evolution (e.g., ANOVA → MANOVA → repeated measures ANOVA)\nContains validation gateways connecting theoretical properties to application guidelines (e.g., deriving sample size requirements from power function analyses)'
    }
}

RELEVANCE_DOMAIN_CRITERIA = {
    "cs": {
        'description': 'Relevance evaluation specific to Computer Science surveys, focusing on technical accuracy, current methodologies, and field-specific applications.',
        'score 1': 'Irrelevant or Obsolete\nThe survey fails to address the core subject area or relies on outdated methodologies, frameworks, or technologies. Key subfields or seminal works are omitted, and the content diverges significantly from the stated scope. Examples include:\n-Surveys on machine learning that ignore foundational algorithms (e.g., transformers, reinforcement learning) in favor of deprecated techniques.\n-Reviews of cybersecurity that lack coverage of zero-day exploits or modern encryption standards.',
        'score 2': 'Partially Relevant with Major Gaps\nThe survey identifies the core subject but includes substantial digressions or omits critical advancements. The narrative inconsistently aligns with the field\'s current trajectory. For instance:\n-A blockchain survey focusing on Proof of Work without addressing energy-efficient consensus mechanisms (e.g., Proof of Stake).\n-A natural language processing review that overlooks large language models (LLMs) like GPT-4 or BERT.',
        'score 3': 'Broadly Relevant with Minor Deviations\nThe survey covers the primary topic but includes peripheral details or underemphasizes emerging trends. While foundational works are acknowledged, the analysis lacks depth in cutting-edge innovations. Examples:\n-A computer vision review detailing convolutional neural networks (CNNs) but only superficially mentioning vision transformers.\n-A quantum computing survey emphasizing Shor\'s algorithm without exploring recent noise-mitigation techniques.',
        'score 4': 'Focused with Minimal Digressions\nThe survey maintains a strong focus on the core subject, integrating both classical and contemporary advancements. Minor deviations (e.g., brief comparisons to adjacent fields) enhance clarity without diluting relevance. Indicators include:\n-A robotics survey contextualizing SLAM (Simultaneous Localization and Mapping) within modern autonomous systems while briefly contrasting it with traditional control theory.\n-A review of graph neural networks (GNNs) that connects them to real-world applications like social network analysis or drug discovery.',
        'score 5': 'Exceptionally Focused and Comprehensive\nThe survey is tightly centered on the subject, offering a novel taxonomy or framework to organize the literature. Every section contributes to a holistic understanding, and the analysis anticipates future directions. Hallmarks include:\n-A cybersecurity survey proposing a threat-model hierarchy that unifies hardware vulnerabilities, adversarial ML, and post-quantum cryptography.\n-An AI ethics review synthesizing technical fairness metrics, regulatory policies, and societal impacts into a unified governance framework.'
    },
    "econ": {
        'description': 'Relevance evaluation specific to Economics surveys, focusing on economic theory, empirical validation, and policy implications.',
        'score 1': 'Economically Irrelevant\nFocuses on non-economic phenomena without demonstrating connections to economic systems\nUses outdated models (pre-2010) without addressing modern computational methods\nFails to engage with current economic debates (e.g., AI impacts, climate economics, post-pandemic recovery)\nExample: Survey of agricultural techniques without cost-benefit analysis or market implications',
        'score 2': 'Marginally Relevant\nMentions economic concepts but lacks substantive integration\nLimited to single methodology (e.g., pure theoretical models) without empirical validation\nReferences fewer than 20% seminal economic works from past decade\nExample: Literature review on labor markets ignoring gig economy transformations',
        'score 3': 'Generally Relevant\nCovers established economic theories with some modern applications\nBalances theoretical and empirical approaches (50/50 split)\nEngages with 2-3 current policy debates but lacks depth\nContains 1-2 sections diverging into adjacent fields (e.g., sociology)\nExample: Survey of monetary policy tools with limited fintech integration',
        'score 4': 'Highly Relevant\nSystematically maps theoretical frameworks to contemporary challenges\nIntegrates multiple methodologies (theoretical, empirical, computational)\nAddresses 4+ active research frontiers (e.g., causal machine learning, behavioral nudges)\nMaintains 90% focus on core economic questions\nExample: Meta-analysis of experimental economics in development policy',
        'score 5': 'Exemplary Relevance\nRedefines economic problem spaces through novel synthesis\nDemonstrates multi-scale analysis (micro-macro linkages)\nProvides actionable insights for 3+ stakeholder groups (policymakers, firms, households)\nAnticipates emerging trends through computational forecasting\nExample: Cross-disciplinary survey of blockchain economics with regulatory simulations'
    },
    "eess": {
        'description': 'Relevance evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical frameworks, system architectures, and engineering methodologies.',
        'score 1': 'Non-Compliant with Domain Standards\nContent: Surveys lack alignment with EESS fundamentals (e.g., omitting key concepts like grid stability metrics, signal modulation techniques, or control system architectures).\nFocus: Over 50% of content addresses unrelated fields (e.g., prolonged biomedical engineering case studies in power electronics review).\nSources: Primarily cites pre-2015 literature missing critical advances (e.g., neglects deep learning in smart grid optimization).\nImpact: Fails to identify EESS-specific challenges (e.g., omits discussion of renewable integration challenges in modern power systems).',
        'score 2': 'Partial Relevance with Structural Deficits\nContent: 30-50% digressions into tangential domains (e.g., spends multiple sections on general machine learning theory without EESS applications).\nFocus: Core EESS subject apparent but inconsistently developed (e.g., reviews wireless sensor networks without connecting to EESS-specific deployment challenges).\nSources: 40-60% citations from non-EESS venues (e.g., over-relies on generic AI conferences without IEEE Trans. Power Systems/Power Electronics references).\nImpact: Identifies EESS problems superficially (e.g., mentions "grid stability" without analyzing specific instability mechanisms like sub-synchronous oscillations).',
        'score 3': 'Generally Relevant with Localized Gaps\nContent: <20% peripheral material (e.g., includes brief primer on reinforcement learning in AI-for-grids survey).\nFocus: Maintains EESS narrative despite minor detours (e.g., reviews general optimization methods before specializing to power flow problems).\nSources: 70%+ citations from EESS/IEEE journals with some outdated key papers (e.g., cites foundational 2010s works but misses 2023-25 breakthroughs in HVDC fault detection).\nImpact: Documents EESS challenges without synthesizing solutions (e.g., catalogs smart grid cybersecurity threats but doesn\'t compare mitigation architectures).',
        'score 4': 'Focused with Strategic Depth\nContent: <10% ancillary material tightly coupled to EESS themes (e.g., explains graph neural networks through power system topology applications).\nFocus: Coherent progression from fundamentals to frontiers (e.g., structures signal processing survey as: 1) Traditional methods → 2) Deep learning → 3) EESS deployment challenges).\nSources: 85%+ EESS/IEEE citations including 2023-25 preprints (e.g., integrates latest IEEE PESGM findings on distributed energy resource management).\nImpact: Connects technical advances to EESS use cases (e.g., analyzes how physics-informed ML reduces simulation costs in grid planning).',
        'score 5': 'Exemplary Domain Integration\nContent: 100% EESS-aligned with interdisciplinary synthesis (e.g., unites control theory, embedded systems, and power electronics in microgrid survey).\nFocus: Thematic consistency across all sections (e.g., maintains power quality thread through harmonics analysis → mitigation devices → standards compliance).\nSources: 95%+ EESS primary sources including 2024/25 preprints (e.g., covers IEEE Trans. Smart Grid papers through Q2 2025).\nImpact: Advances EESS research trajectory by:\n-Resolving conflicting findings (e.g., reconciles disparate results in FACTS device placement)\n-Identifying understudied areas (e.g., highlights lack of co-simulation frameworks for cyber-physical power systems)\n-Proposing EESS-specific evaluation metrics (e.g., adapts ML performance measures for grid contingency screening)'
    },
    "math": {
        'description': 'Relevance evaluation specific to Mathematics surveys, focusing on mathematical coherence, logical progression, and theoretical frameworks.',
        'score 1': 'Irrelevant or Obsolete Content\nThe survey fails to address the stated mathematical topic, either by focusing on unrelated subfields (e.g., discussing algebraic topology in a survey on stochastic differential equations) or relying on outdated frameworks no longer central to modern research. Key theories or recent breakthroughs (post-2010) are omitted, and cited works lack relevance to the core subject. Examples include misclassifying theorems (e.g., conflating PDE analysis with ODE techniques) or including non-mathematical content (e.g., applied engineering case studies in a pure mathematics survey).',
        'score 2': 'Partial Relevance with Major Divergences\nThe survey identifies the core subject but includes substantial off-topic sections. For instance, a review of graph theory might devote excessive space to algorithmic complexity without linking it to structural graph properties. Critical subtopics (e.g., neglecting étale cohomology in a survey on algebraic geometry) are underdeveloped, while peripheral areas (e.g., historical anecdotes about mathematicians) dominate. Citations are inconsistently related, mixing seminal papers with irrelevant works.',
        'score 3': 'Broadly Relevant with Minor Lapses\nThe survey covers the primary subject adequately but includes minor digressions (e.g., a deep dive into specific lemma proofs in a high-level overview of category theory). Most cited works are foundational or recent (within the last decade), but 1–2 key advancements (e.g., Perelman\'s Ricci flow results in a geometric analysis survey) are missing. The narrative occasionally loses focus, such as discussing numerical methods in a theoretical linear algebra survey without clarifying their relevance.',
        'score 4': 'Focused with Occasional Non-Critical Deviations\nThe survey maintains strong alignment with the core subject, with deviations limited to contextual examples (e.g., brief applications of knot theory to DNA topology in a pure mathematics review). All major subtopics are addressed, including recent advances (e.g., AI-assisted theorem proving in a logic survey). Citations are comprehensive, though 1–2 niche preprints may lack peer-reviewed validation. The structure is logical, with clear transitions between themes (e.g., linking Hodge conjecture progress to mirror symmetry developments).',
        'score 5': 'Exceptional Precision and Thematic Rigor\nEvery section directly contributes to a nuanced understanding of the subject. The survey synthesizes classical results (e.g., Gauss\'s contributions to number theory) with cutting-edge advances (e.g., Scholze\'s perfectoid spaces in arithmetic geometry), avoiding superfluous content. Interdisciplinary connections (e.g., Langlands program bridges to quantum physics) are explicitly tied to the core narrative. Citations are meticulously curated, balancing milestone papers (e.g., Wiles\'s proof of Fermat\'s Last Theorem) and preprints from leading repositories (e.g., arXiv quant-ph/math-ph cross-listings). The structure mirrors the field\'s conceptual hierarchy, such as progressing from axiomatic foundations to open conjectures in a set theory survey.'
    },
    "physics": {
        'description': 'Relevance evaluation specific to Physics surveys, focusing on physical relevance, foundational works, and experimental validation.',
        'score 1': 'Non-Compliant Survey\nContains >50% content unrelated to stated scope (e.g., quantum gravity paper devoting major sections to classical fluid dynamics)\nFails to cite 75% of landmark papers from the past decade in the target subfield\nDemonstrates conceptual misunderstandings of core physics principles (e.g., misapplying renormalization group techniques)',
        'score 2': 'Partially Relevant\n30-50% content drift into adjacent fields without justification (e.g., condensed matter survey digressing into pure mathematics)\nOmits 2+ key experimental/theoretical breakthroughs from the past 5 years\nContains outdated paradigm references (>10 years old) without critical reassessment',
        'score 3': 'Minimally Acceptable\n<20% tangential content with weak thematic links (e.g., cosmological inflation survey briefly mentioning unrelated dark matter models)\nCovers 60-75% of essential sub-topics in the target domain\nIncludes some recent preprints (past 2 years) but lacks critical synthesis',
        'score 4': 'Strong Relevance\n95% content directly advances survey\'s stated scope\nIntegrates findings from 3+ major collaborations (e.g., LHC results alongside astrophysical observations)\nProvides original cross-domain insights (e.g., connecting quantum information theory to black hole thermodynamics)',
        'score 5': 'Exemplary Focus\n100% content contributes to unified narrative without redundant material\nAnticipates emerging trends through analysis of 10+ recent preprints (<6 months old)\nResolves apparent contradictions between competing theories (e.g., reconciling loop quantum gravity with string theory approaches)\nIncludes interactive elements (Jupyter notebooks, simulation tools) for technical verification'
    },
    "q-bio": {
        'description': 'Relevance evaluation specific to Quantitative Biology surveys, focusing on biological relevance, computational methods, and interdisciplinary integration.',
        'score 1': 'Irrelevant or Outdated Content\nSurveys lack connection to quantitative biology\'s foundational pillars (e.g., dynamical modeling, omics data integration, machine learning for biological systems).\nExamples: Reviews focused purely on wet-lab techniques without computational integration, or outdated surveys that omit advances in deep learning for genomics.\nFails to address modern challenges like scalability of single-cell analysis tools or interpretability of AI-driven biological predictions.',
        'score 2': 'Partial Alignment with Core Themes\nSurveys touch on quantitative biology topics but exhibit major digressions (e.g., lengthy sections on general machine learning theory without biological examples).\nCore subject (e.g., spatial transcriptomics or protein design) is mentioned but not explored in depth, with limited discussion of computational methodologies.\nMay include outdated case studies (e.g., early neural networks) without addressing cutting-edge tools like AlphaFold or CRISPR-dCas9 screens.',
        'score 3': 'General Relevance with Minor Divergences\nSurveys cover central themes (e.g., multi-omics integration, network biology) but include tangential sections (e.g., excessive historical context or non-biological applications).\nKey methodologies (e.g., differential equation modeling, Bayesian inference) are described but lack critical analysis of their limitations in biological contexts.\nMisses opportunities to connect topics (e.g., failing to link single-cell RNA-seq tools to spatial transcriptomics advancements).',
        'score 4': 'Focused and Cohesive Coverage\nSurveys maintain strong focus on quantitative biology\'s interdisciplinary nature, with minimal off-topic content.\nDetailed exploration of emerging areas (e.g., AI-driven drug discovery, causal inference in gene regulatory networks).\nIntegrates case studies effectively (e.g., applying graph neural networks to protein-protein interaction networks).\nMinor gaps include insufficient discussion of reproducibility challenges or underrepresented subfields (e.g., metabolic flux analysis).',
        'score 5': 'Exceptional Precision and Comprehensiveness\nEvery section advances understanding of quantitative biology\'s cutting edge, such as:\n-Algorithmic rigor: Critical evaluation of tools like scVI for single-cell data denoising.\n-Translational impact: Discussion of clinically validated models (e.g., cancer prognosis using spatial proteomics).\n-Interdisciplinary synthesis: Bridging stochastic modeling with single-molecule imaging data.\nAnticipates future directions (e.g., foundation models for multi-modal biological data).\nExemplified by surveys that balance technical depth (e.g., mathematical derivations of gene regulatory models) with biological relevance (e.g., applications to developmental patterning).'
    },
    "q-fin": {
        'description': 'Relevance evaluation specific to Quantitative Finance surveys, focusing on financial models, mathematical frameworks, and market applications.',
        'score 1': 'Irrelevant or Outdated Content\nThe survey lacks connection to quantitative finance\'s foundational or contemporary themes. It may focus on unrelated financial domains (e.g., qualitative macroeconomic analysis) or rely on obsolete methodologies (e.g., pre-2010 stochastic models without modern adaptations). Key subfields like portfolio optimization, derivatives pricing, or machine learning applications are absent. Examples include surveys that conflate quantitative finance with general financial journalism or fail to address computational advances post-2015.',
        'score 2': 'Partial Relevance with Major Gaps\nThe survey identifies quantitative finance as its subject but exhibits significant digressions into peripheral topics (e.g., lengthy sections on blockchain ethics without linking to quantitative trading strategies). Core areas like stochastic calculus, factor models, or backtesting frameworks are mentioned but not explored systematically. The paper may overlook critical advancements, such as the role of reinforcement learning in algorithmic trading or the impact of high-frequency data on volatility modeling.',
        'score 3': 'Broad Alignment with Occasional Lapses\nThe survey covers major quantitative finance themes but includes sections of limited utility (e.g., an overlong primer on basic statistics). It addresses both classical techniques (e.g., Black-Scholes-Merton models) and modern approaches (e.g., transformer-based price prediction) but fails to synthesize their interplay. While subfields like risk parity or statistical arbitrage are acknowledged, their treatment lacks depth or misses key literature post-2020.',
        'score 4': 'Focused with Minor Deviations\nThe survey maintains strong alignment with quantitative finance\'s technical demands. It provides a coherent narrative on topics such as multi-asset portfolio optimization, Monte Carlo methods for exotic derivatives, or the use of LLMs in sentiment-driven trading. Minor deviations-such as a brief detour into qualitative behavioral finance-do not detract from the overall focus. The paper critically engages with recent advances, such as the application of neural SDEs or federated learning in cross-institutional data sharing.',
        'score 5': 'Exceptional Precision and Comprehensiveness\nThe survey is a paradigm of relevance, tightly focused on quantitative finance\'s theoretical and applied frontiers. It seamlessly integrates traditional domains (e.g., stochastic portfolio theory) with cutting-edge topics like quantum financial models or adversarial robustness in trading algorithms. Every section contributes to a unified thesis, such as the convergence of deep learning and econometrics in alpha generation. The paper demonstrates mastery of the literature, citing seminal works (e.g., Fama-French factor models) alongside 2023–2025 breakthroughs in areas like real-time risk simulation using differentiable programming.'
    },
    "stat": {
        'description': 'Relevance evaluation specific to Statistics surveys, focusing on statistical frameworks, methodological approaches, and theoretical foundations.',
        'score 1': 'Irrelevant or Obsolete Content\nThe survey misrepresents the scope of statistical research, focusing on deprecated methods (e.g., overly simplistic parametric tests without discussing robust alternatives) or unrelated domains (e.g., non-probabilistic machine learning without statistical grounding).\nFails to address core statistical paradigms (e.g., Bayesian vs. frequentist frameworks) or emerging trends (e.g., causal inference, reproducibility crises).\nExamples and case studies lack statistical rigor or rely on outdated datasets (e.g., Iris dataset without contextualizing limitations).',
        'score 2': 'Partial Relevance with Major Deviations\nThe core statistical theme is identifiable but diluted by tangential discussions (e.g., lengthy explanations of general machine learning pipelines in a survey about spatial statistics).\nOmits critical subfields (e.g., neglecting nonparametric methods in a review of hypothesis testing) or misrepresents interdisciplinary connections (e.g., conflating statistical significance with clinical significance).\nSources are disproportionately historical (e.g., overciting pre-2000s papers in a survey about high-dimensional inference).',
        'score 3': 'Generally Relevant with Minor Lapses\nCovers major statistical areas (e.g., regression, experimental design) but lacks depth in nuanced topics (e.g., insufficient discussion of post-selection inference or multiple testing corrections).\nIncludes some modern advancements (e.g., conformal prediction) but overlooks key trends (e.g., the role of statistics in generative AI or large language models).\nCase studies are relevant but lack methodological diversity (e.g., focusing solely on biomedical applications in a survey about causal discovery).',
        'score 4': 'Focused and Cohesive with Occasional Digressions\nSystematically reviews both foundational (e.g., likelihood theory) and contemporary topics (e.g., differential privacy, debiased machine learning) while maintaining a clear narrative.\nConnects subfields (e.g., explaining how bootstrap methods apply to Bayesian posterior estimation) and addresses open challenges (e.g., scalability of MCMC in big data contexts).\nExamples are well-chosen but occasionally overemphasize niche applications (e.g., disproportionate focus on astrophysics in a general survey about missing data imputation).',
        'score 5': 'Exceptional Focus and Comprehensiveness\nSeamlessly integrates theoretical rigor, computational advancements, and real-world applicability (e.g., discussing Hamiltonian Monte Carlo alongside convergence diagnostics and applications in pharmacometrics).\nBalances classical (e.g., Fisherian inference) and modern themes (e.g., federated learning\'s statistical implications) with no redundant or off-topic content.\nAnticipates interdisciplinary challenges (e.g., statistical guarantees for AI-driven decision systems) and provides a unifying framework for future research (e.g., categorizing resampling methods by robustness, scalability, and interpretability).'
    }
}

LANGUAGE_DOMAIN_CRITERIA = {
    "cs": {
        'description': 'Language evaluation specific to Computer Science surveys, focusing on technical precision, mathematical notation, and scholarly communication.',
        'score 1': 'Non-Academic Technical Communication\nLanguage informality: Contains colloquial expressions ("Let\'s dive into..."), first-person anecdotes, or conversational phrasings incompatible with scholarly discourse.\nTechnical deficiencies: Misuses fundamental CS terminology (e.g., conflating "algorithm" with "heuristic"), contains critical mathematical notation errors, or demonstrates misunderstanding of core concepts.\nStructural issues: Lacks standard survey components (taxonomies, comparative tables, research timelines), with incoherent flow between technical sections\nCitation malpractice: Fails to properly reference seminal works (e.g., omitting Knuth\'s algorithms or Turing Award papers in relevant domains).',
        'score 2': 'Developing Technical Writing\nInconsistent formality: Mixes formal explanations with informal analogies ("Think of neural networks like pizza toppings...").\nTerminology issues: Uses correct CS terms but with imprecise modifiers ("somewhat efficient algorithm") or improper adjective-noun pairings ("strong privacy").\nMathematical flaws: Contains minor notation errors (misusing ∃/∀ quantifiers) or inconsistent variable definitions across equations.\nStructural weaknesses: Includes survey elements but with poor organization (e.g., placing methodology after results) or inadequate subsection transitions.',
        'score 3': 'Competent Technical Exposition\nGenerally formal style: Maintains academic tone with rare lapses into colloquialisms during complex concept explanations.\nTechnical accuracy: Correctly uses CS terminology (e.g., distinguishes NP-hard vs NP-complete) with occasional over-simplification.\nMathematical rigor: Properly formats equations but may lack derivational clarity or sufficient contextualization.\nStandard structure: Follows conventional survey organization (historical context → taxonomies → analysis → open challenges) with logical progression.',
        'score 4': 'Proficient Scholarly Communication\nPrecise technical language: Employs discipline-specific terms (e.g., "amortized complexity," " Byzantine fault tolerance") with appropriate qualifiers.\nMathematical clarity: Uses consistent notation aligned with CS conventions (Big O formatting, proper recurrence relations).\nEffective synthesis: Creates original classification frameworks (e.g., novel taxonomy of GAN variants) while properly contextualizing prior work.\nStrategic formatting: Uses algorithms/pseudocode following IEEE/ACM standards with optimal abstraction levels.',
        'score 5': 'Exemplary CS Scholarship\nTechnical mastery: Demonstrates nuanced understanding through precise distinctions (e.g., differentiating PAC-learning vs statistical learning theory).\nMathematical elegance: Presents complex proofs/derivations with exceptional clarity using computer science-specific proof techniques (probabilistic method, reduction arguments).\nSeminal integration: Critically engages with foundational texts (e.g., properly contextualizes Cook\'s theorem in complexity theory surveys).\nGenre innovation: Advances survey methodology through novel presentation formats (interactive taxonomy diagrams, evolutionary timelines with technical milestones).\nReproducibility focus: Includes artifact appendices with version-controlled code repositories and dataset metadata following ACM reproducibility standards.'
    },
    "econ": {
        'description': 'Language evaluation specific to Economics surveys, focusing on economic terminology, mathematical formalism, and scholarly communication.',
        'score 1': 'Deficient Academic Communication\nTone & Formality: Pervasive use of colloquialisms, conversational phrasing, or journalistic stylistic devices (e.g., rhetorical questions, hyperbolic comparisons). Contains personal anecdotes or unsubstantiated opinion statements presented as fact.\nTechnical Precision: Misuses fundamental economic terminology (e.g., conflating "elasticity" with "slope," misapplying "externality" concepts). Fails to distinguish between normative and positive economic statements.\nStructural Coherence: Lacks clear transitions between literature synthesis, methodological critique, and theoretical analysis. Sections read as disjointed commentary rather than integrated survey.\nMathematical Formalism: Equations presented without proper LaTeX formatting or contextual economic interpretation. Variables undefined or inconsistent with standard notation (e.g., using Y for individual income rather than aggregate output).\nCitation Practice: Omits in-text citations for foundational theories or uses non-academic sources (e.g., blog posts, unvetted working papers) without justification. Fails to follow (Author, Year) citation format.',
        'score 2': 'Developing Scholarly Expression\nTone & Formality: Occasional lapses into informal constructions (e.g., contractions, first-person narratives without analytical purpose). Overuses simplistic transitional phrases ("Another thing is...") rather than conceptual connectors.\nTechnical Precision: Inconsistently applies specialized vocabulary-correctly uses "opportunity cost" in one section but misapplies "comparative advantage" in another. Provides incomplete definitions of econometric terms (e.g., mentioning "instrumental variables" without specifying relevance conditions).\nStructural Coherence: Attempts literature categorization (e.g., "classical vs. behavioral approaches") but lacks critical synthesis of conflicting findings. Methodology sections describe techniques without addressing economic plausibility.\nMathematical Formalism: States equations correctly but fails to articulate their economic intuition (e.g., presenting a production function without discussing returns to scale implications). Intermittent LaTeX errors in subscripts/superscripts.\nCitation Practice: Cites seminal works but neglects recent advancements. Over-relies on secondary summaries rather than primary theoretical sources.',
        'score 3': 'Competent Economic Discourse\nTone & Formality: Maintains formal register with rare informalities ("Let\'s now turn to..."). Generally avoids anthropomorphism of economic forces ("The GDP wanted to grow...").\nTechnical Precision: Accurately employs core terminology (e.g., distinguishes "Pareto efficiency" from "Kaldor-Hicks efficiency"). Provides adequate definitions for advanced concepts (e.g., "GMM estimation") upon first use.\nStructural Coherence: Logically groups literature by thematic clusters (e.g., "New Keynesian DSGE models") rather than chronological listing. Identifies methodological tradeoffs in surveyed empirical approaches.\nMathematical Formalism: Correctly formats equations with proper economic context (e.g., deriving Euler equations with explicit utility function assumptions). Minor notational inconsistencies in auxiliary proofs.\nCitation Practice: Balances foundational citations (e.g., Arrow-Debreu) with post-2010 advancements. Appropriately uses working papers for emerging topics with clear labeling.',
        'score 4': 'Proficient Scholarly Communication\nTone & Formality: Consistently formal with precise hedging ("The evidence suggests..." vs. "This proves..."). Masterfully employs economic metaphors without anthropomorphism (e.g., "liquidity traps constrain monetary transmission").\nTechnical Precision: Deploys subfield-specific lexicon appropriately (e.g., "Hicksian vs. Marshallian demand" in microtheory). Anticipates terminological ambiguity by defining contested terms (e.g., multiple "efficiency" metrics in environmental economics).\nStructural Coherence: Seamlessly connects empirical findings to theoretical debates (e.g., reconciling conflicting elasticity estimates with identification strategies). Critically evaluates literature gaps rather than merely cataloging papers.\nMathematical Formalism: Integrates equations as narrative elements (e.g., using production functions to motivate growth accounting surveys). Maintains notational consistency across models and appendices.\nCitation Practice: Demonstrates citational awareness through curated references-prioritizing high-impact journals (Econometrica, AER) while including policy-relevant grey literature where applicable.',
        'score 5': 'Exemplary Economic Scholarship\nTone & Formality: Achieves analytical rigor through restrained prose, avoiding both excessive formalism and populist simplification. Expertly modulates voice for complex material (e.g., intuitive explanations of measure-theoretic probability in econometrics).\nTechnical Precision: Deploys cutting-edge terminology (e.g., "machine learning causal forests") with pedagogical clarity. Reconciles conflicting disciplinary definitions (e.g., "capital" in growth vs. finance contexts).\nStructural Coherence: Organizes surveys as conceptual frameworks rather than annotated bibliographies-using sections to debate competing paradigms (e.g., "Rational Expectations vs. Adaptive Learning in Macro Models").\nMathematical Formalism: Equations enhance rather than replace economic reasoning, with variables explicitly tied to observable phenomena (e.g., θ parameterized as labor share in CES production).\nCitation Practice: Curates citations to trace intellectual evolution (e.g., linking modern heterogeneous agent models to early Lucas critiques). Integrates preprint archives (e.g., NBER, arXiv) judiciously with clear recency justifications.'
    },
    "eess": {
        'description': 'Language evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical terminology, mathematical notation, and IEEE-style formatting.',
        'score 1': 'Non-Compliant Academic Language\nInformality: Frequent colloquialisms (e.g., "This method works like a charm") or contractions ("don\'t," "can\'t").\nTechnical Errors: Incorrect terminology (e.g., "voltage drop" misapplied to current) or mislabeled equations (e.g., using x instead of x for vectors).\nStructural Flaws: Disorganized sections, missing IEEE-style headings (e.g., "II. Related Work"), and inconsistent citation formatting.\nExamples: "The algo\'s pretty good at stabilizing the grid, but sometimes it messes up."',
        'score 2': 'Developing Academic Tone with Inconsistencies\nMixed Formality: Occasional informal phrases (e.g., "a lot of researchers") amid technical descriptions.\nTerminology Lapses: Imprecise terms (e.g., "machine learning" used generically instead of specifying reinforcement learning).\nEquation Issues: Minor notation errors, such as unitalicized scalars (e.g., "R=10Ω" instead of R=10 Ω).\nStructural Weaknesses: Inconsistent subsection hierarchy (e.g., using ### headers for non-critical topics).',
        'score 3': 'Competent but Unpolished Academic Style\nGeneral Formality: Mostly formal tone with rare lapses (e.g., "Recent work has tackled this issue head-on").\nTechnical Accuracy: Correct use of terms like phasor analysis or Nyquist stability criterion, but occasional oversimplification.\nEquation Compliance: Proper LaTeX formatting for equations, though numbering may misalign with text references.\nStructural Compliance: Logical flow with IEEE-style headings, but uneven depth in subsections (e.g., sparse details in "IV. Challenges").',
        'score 4': 'Proficient and Polished Academic Writing\nPrecision: Exact terminology (e.g., differentiating total harmonic distortion from intermodulation distortion).\nMathematical Rigor: Flawless equation formatting (e.g., Y=GV for admittance matrices) and alignment with IEEE guidelines.\nStructural Excellence: Clear hierarchy (e.g., "III. Methods" subdivided into "A. Simulation Framework," "B. Validation Metrics").\nStyle Consistency: Citations strictly follow IEEE numerical order, and abbreviations are defined at first use (e.g., "PV (photovoltaic) systems").',
        'score 5': 'Exemplary Scholarly Exposition\nMastery of Technical Language: Nuanced discussion of niche topics (e.g., "multi-agent reinforcement learning in microgrid dispatch") without jargon overload.\nMathematical Elegance: Equations are contextualized pedagogically (e.g., "Applying Kirchhoff\'s laws yields: [equation]," followed by intuitive interpretations).\nStructural Sophistication: Seamless transitions between sections, with meta-commentary guiding readers (e.g., "Having established the taxonomy, we now evaluate scalability challenges").\nEditorial Perfection: Zero deviations from IEEE style, including proper use of em dashes, en dashes, and SI units.'
    },
    "math": {
        'description': 'Language evaluation specific to Mathematics surveys, focusing on mathematical notation, proof techniques, and scholarly communication.',
        'score 1': 'Deficient Mathematical Communication\nTone: Overly informal with colloquial phrases (e.g., "Let\'s check out this formula") and subjective interjections.\nGrammar: Frequent errors in syntax (e.g., misplaced modifiers in theorem statements) and punctuation misuse in equations.\nTerminology: Inconsistent or incorrect use of mathematical terms (e.g., conflating "ring" with "field" or misusing "if and only if").\nNotation: Mixes LaTeX and Unicode symbols haphazardly (e.g., x2vs. x²), violates standard typographical conventions.\nCitations: Fails to cite foundational results (e.g., omitting key references to Birkhoff\'s theorems in lattice theory).\nStructure: Disorganized progression of ideas without clear section headers (e.g., jumping between modular lattices and Hurwitz numbers without transitions).',
        'score 2': 'Emerging Mathematical Rigor\nTone: Occasionally informal (e.g., "As we saw earlier...") but attempts academic formality in definitions.\nGrammar: Recurrent minor errors in complex sentences (e.g., dangling participles in lemma explanations).\nTerminology: Generally correct but imprecise (e.g., using "function" instead of "operator" in functional analysis contexts).\nNotation: Mostly uses LaTeX but with formatting inconsistencies (e.g., sinx vs. sin(x)).\nCitations: Lists references but fails to connect them contextually (e.g., mentioning Jónsson\'s work without relating it to Arguesian lattices).\nStructure: Basic section headers (e.g., "Introduction," "Results") without subsections for specialized topics like modular vs. distributive lattices.',
        'score 3': 'Competent Mathematical Exposition\nTone: Consistently formal with rare lapses (e.g., overusing "Note that" in proofs).\nGrammar: Occasional comma splices in long technical sentences but no meaning-obscuring errors.\nTerminology: Correct usage of domain-specific terms (e.g., distinguishing "quasigroup" vs. "loop" in algebra).\nNotation: Standard LaTeX for equations but inconsistent bold/italic styling for special sets.\nCitations: Appropriately credits sources for major theorems but omits historical context (e.g., citing Haiman\'s work on linear lattices without mentioning Birkhoff\'s precursors).\nStructure: Clear ###-level subsections for topics like "Modular Lattice Characterizations" but uneven depth in specialized areas.',
        'score 4': 'Proficient Scholarly Synthesis\nTone: Formally precise with disciplined use of passive voice where appropriate (e.g., "It can be shown that...").\nGrammar: Negligible errors, even in multi-clause explanations of categorical duals.\nTerminology: Exact phrasing for technical concepts (e.g., "finitely generated projective module" vs. "free module").\nNotation: Flawless LaTeX with proper spacing and alignment in commutative diagrams.\nCitations: Contextualizes references within broader literature (e.g., contrasting Goulden-Jackson\'s immanant work with earlier Schur function approaches).\nStructure: Hierarchical ### and #### headers for nested topics (e.g., "4.2.2. Monotone Hurwitz Numbers") with purposeful transitions.',
        'score 5': 'Exemplary Mathematical Writing\nTone: Masterful balance of formality and clarity, avoiding both stiffness and vagueness (e.g., "Theorem 2.12 generalizes Lemma 1.7 via categorical equivalence").\nGrammar: Impeccable syntax even in dense passages about lattice isomorphisms.\nTerminology: Nuanced distinctions maintained throughout (e.g., "finitely presented" vs. "finitely generated" in algebra).\nNotation: Professionally typeset equations with consistent typography for operators/variables (e.g., sl(2,C) vs. SL2 (R)).\nCitations: Seamlessly integrates historical context (e.g., tracing Arguesian identity from Jónsson to Haiman\'s self-dual form).\nStructure: Thematically cohesive with nested subsections (e.g., "3.1.4. Counterexamples to Dual Inequalities") that mirror mathematical dependencies.'
    },
    "physics": {
        'description': 'Language evaluation specific to Physics surveys, focusing on physical terminology, mathematical notation, and scholarly communication.',
        'score 1': 'Fundamentally Deficient\nContains frequent equation formatting errors (e.g., unnumbered displays, incorrect LaTeX syntax for operators like H^or ∇⋅E)\nMisuses key physics terminology (e.g., conflating "Hamiltonian" with "Lagrangian," misapplying "cross-section" definitions)\nExhibits structural disorganization incompatible with physics review conventions (e.g., missing comparative analysis tables, inadequate subsections for theoretical vs. experimental approaches)\nFails to maintain technical precision in describing methods (e.g., vague references to "the equation" without specifying L=T−V)',
        'score 2': 'Developing Competence\nShows inconsistent SI unit handling (e.g., mixing GeV/c² with informal energy descriptions)\nContains ambiguous variable definitions (e.g., using α without specifying fine-structure vs. scattering angle context)\nDemonstrates weak literature synthesis (e.g., listing papers chronologically rather than by conceptual clusters)\nUses improper citation practices for physics sources (e.g., failing to cite seminal works like Weinberg\'s QFT texts when appropriate)',
        'score 3': 'Functional Proficiency\nGenerally applies correct tensor notation (e.g., gμν for metric tensor) but makes occasional index placement errors\nMaintains standardized terminology (e.g., proper use of "renormalization group flow" vs. "scaling behavior") with rare lapses\nFollows journal structural conventions (IMRAD with physics adaptations) but lacks nuanced section transitions\nContains minor LaTeX issues (e.g., inconsistent boldface for vectors vs. tensors: p vs Tμν)',
        'score 4': 'Advanced Mastery\nImplements disciplined equation numbering aligned with discussion flow (e.g., Eq. (5) immediately precedes relevant text analysis)\nExhibits precise terminology for subfield conventions (e.g., distinguishing "anyonic statistics" from "fractional statistics" in topological matter reviews)\nDemonstrates effective notation systems (e.g., consistent use of ℏ=c=1 natural units with proper contextualization)\nMaintains rigorous citation density (2-3 references per key claim) using APS/RevTeX style',
        'score 5': 'Exemplary Scholarship\nAchieves flawless mathematical typography (e.g., proper use of L for Lagrangian densities vs L for discrete systems)\nEmbodies field-specific rhetorical patterns (e.g., problem-solution narratives in quantum gravity reviews)\nImplements multiscale technical communication (accessible overviews with footnoted mathematical rigor)\nDemonstrates conceptual density optimization (>5 key theories/experiments per page in high-energy physics contexts)'
    },
    "q-bio": {
        'description': 'Language evaluation specific to Quantitative Biology surveys, focusing on biological terminology, computational methods, and interdisciplinary communication.',
        'score 1': 'Non-Compliant with Academic Standards\nTone & Formality: Language is excessively informal, with colloquial phrases (e.g., "a lot of," "pretty good") and contractions (e.g., "don\'t," "can\'t").\nTerminology: Misuses core quantitative biology terms (e.g., conflating "sequence alignment" with "sequence assembly" or misdefining "fold recognition"). Fails to distinguish between methods like ab initio modeling and homology-based prediction.\nGrammar & Syntax: Frequent errors in subject-verb agreement (e.g., "the data shows") or misplaced modifiers disrupt readability. Sentences lack subordination, resulting in a fragmented narrative.\nExamples from Low-Scoring Work: Overuse of vague descriptors like "some researchers think" without citations, or informal analogies (e.g., comparing protein folding to "origami").',
        'score 2': 'Partially Compliant with Modest Rigor\nTone & Formality: Occasional lapses into informality, such as first-person pronouns ("we believe") or conversational transitions ("now, let\'s talk about").\nTerminology: Inconsistent use of standardized terms (e.g., alternating between "gene expression" and "gene activity"). Misapplies ML terms (e.g., using "neural network" without specifying architecture type).\nGrammar & Syntax: Ambiguous pronoun references (e.g., "this is important" without clarifying "this") or run-on sentences in method descriptions.\nExamples: Statements like "Deep learning is better than old methods" without defining "old methods" or quantifying improvements.',
        'score 3': 'Competent with Minor Shortcomings\nTone & Formality: Generally formal but with sporadic informality, such as rhetorical questions ("Why does this matter?") or mildly subjective phrasing ("interestingly, the model...").\nTerminology: Correctly uses foundational terms (e.g., "multiple sequence alignment," "Markov models") but struggles with nuanced distinctions (e.g., "sensitivity" vs. "specificity" in variant calling).\nGrammar & Syntax: Occasional punctuation errors in complex sentences (e.g., missing commas in appositives). Overuse of passive voice in methodology sections.\nExamples: Sentences like "The algorithm, which was developed recently, improves accuracy" lack specificity about the algorithm or metrics.',
        'score 4': 'Proficient with Occasional Refinement Needs\nTone & Formality: Consistently formal, with discipline-appropriate hedging (e.g., "these results suggest" rather than "prove"). Maintains objectivity in critiques of prior work.\nTerminology: Precise use of advanced terms (e.g., "attention mechanisms in transformer models," "k-mer frequency distributions") and acronyms (e.g., correctly defining LSTM before abbreviation).\nGrammar & Syntax: Minor errors in article usage ("a RNA-seq" vs. "an RNA-seq") or pluralization of mass nouns ("datas").\nExamples: Clear statements like "AlphaFold2\'s RMSD of 0.96 Å outperformed RosettaFold\'s 1.5 Å in CASP14", but occasional overuse of nominalizations ("the implementation of the computation" vs. "how we computed").',
        'score 5': 'Exemplary Mastery of Domain Conventions\nTone & Formality: Unwaveringly formal with judicious use of field-specific conventions (e.g., "we hypothesize that..." in developmental models). Avoids redundancy through concise phrasing.\nTerminology: Expertly deploys niche terms (e.g., "coevolutionary coupling analysis," "diffusion models for protein generation") and contextualizes emerging jargon (e.g., "foundation models" in bioinformatics).\nGrammar & Syntax: Flawless syntax even in multi-clause explanations of algorithms (e.g., "Given a sequence S={s1,...,sn}, the model computes P(si∣si−k,...,si+k) using a sliding window approach").\nExamples: Sentences like "The ESM-2 embedding space, parameterized by θ, captures latent structural dependencies through self-attention layers L1to L33", balancing mathematical notation with clear biological context.'
    },
    "q-fin": {
        'description': 'Language evaluation specific to Quantitative Finance surveys, focusing on financial terminology, mathematical notation, and scholarly communication.',
        'score 1': 'Non-Compliant Academic Standards\nContains frequent undefined abbreviations (e.g., "BS model" without expanding to Black-Scholes)\nMathematical symbols lack proper contextualization (e.g., using μ without specifying it represents drift rate)\nOver 5 grammatical errors per page that obscure meaning, such as misplaced modifiers in probability statements: "The model assumes returns normally distributed"',
        'score 2': 'Partial Compliance with Domain Norms\nInconsistent capitalization of proper nouns (e.g., alternating between "Markowitz" and "markowitz")\nOccasional formula formatting errors, like using dSt=μStdt+σStdWt without defining Wiener process Wt\n3-4 ambiguous phrases per page, such as "some researchers suggest" without specifying authors or studies',
        'score 3': 'Baseline Academic Acceptability\nGenerally correct usage of terms like Value-at-Risk vs. Expected Shortfall with 1-2 definitional oversights\nMinor equation alignment issues, e.g., misplaced E[Ri] in CAPM derivations\n1-2 instances per section of informal transitions like "Now, let\'s look at..." instead of formal equivalents',
        'score 4': 'High-Quality Technical Communication\nPrecise differentiation between related concepts (e.g., local volatility vs. stochastic volatility models)\nFlawless integration of theorems using AMS-LaTeX packages for financial mathematics\nSingle minor oversight per 10 pages, such as an undefined abbreviation in peripheral content',
        'score 5': 'Exemplary Domain-Specific Prose\nMasterful explanations of advanced topics like rough volatility models or deep hedging strategies through layered paragraph structures\nMathematical appendices demonstrating G-Brownian motion proofs with textbook-level rigor\nZero tolerance for ambiguity in critical sections, with all stochastic integrals properly defined as ∫0THtdSt under specified filtrations'
    },
    "stat": {
        'description': 'Language evaluation specific to Statistics surveys, focusing on statistical terminology, mathematical notation, and scholarly communication.',
        'score 1': 'Deficient Scholarly Communication\nManuscripts exhibit pervasive informality through colloquial phrases ("Our model kinda nailed the predictions") and unsubstantiated hyperbole ("This method blows others out of the water"). Statistical terminology shows critical misunderstandings, such as conflating Bayesian credible intervals with frequentist confidence intervals or misapplying p-value interpretations. Grammatical errors obstruct meaning: "The datas shows significants results when apply random forest." Mathematical notation contains inconsistent formatting (using "X~N(μ,σ)" and "Y ≈ Normal(mean, sd)" interchangeably) and fails to define variables. Narrative flow lacks logical signposting between foundational concepts (parametric tests) and advanced methods (Bayesian hierarchical modeling).',
        'score 2': 'Developing Academic Rigor\nWriting intermittently lapses into conversational phrasing ("As luck would have it, the bootstrap worked better") alongside proper technical passages. Statistical terms appear with occasional imprecision, such as using "correlation" without specifying Pearson/Spearman/Kendall variants or stating "ANOVA results" without checking homogeneity of variance assumptions. Moderate grammatical issues persist in complex sentences: "The researchers, having collected the data which was cleaned and normalized, then applies machine learning algorithms." Mathematical expressions show inconsistent LaTeX formatting (mixing $x_i$ and \\textit{x\\textsubscript{i}}) and undefined symbols. Literature synthesis jumps abruptly between classical (Fisher exact test) and modern (deep learning) methods without establishing conceptual connections.',
        'score 3': 'Competent Technical Writing\nLanguage maintains general formality with rare informal slips ("The t-test really came through"). Statistical terminology demonstrates functional accuracy in describing procedures like "Welch\'s t-test for unequal variances" or "Benjamini-Hochberg correction for multiple comparisons". Minor grammatical oversights occur in subordinate clauses: "The team whom developed the Bayesian framework..." Mathematical notation follows discipline conventions with isolated formatting lapses (using "β_1" instead of "$\\beta_1$"). Methodological explanations balance brevity and completeness, though occasionally omit justification for key choices (selecting AIC over BIC for model selection). Transitions between statistical concepts (frequentist vs. Bayesian paradigms) use standard connective phrases but lack deeper synthesis.',
        'score 4': 'Proficient Scholarly Discourse\nWriting demonstrates consistent formality with precise statistical phrasing: "Maximum likelihood estimation under MAR missingness assumptions". Technical terminology shows nuanced understanding, distinguishing between "homoscedasticity" and "homogeneity of regression slopes" in ANCOVA contexts. Grammar remains error-free except in highly complex syntactic constructions involving nested equations. Mathematical expressions adhere to journal-specific LaTeX standards, though occasional alignment issues arise in multi-line equations. Literature reviews systematically connect historical developments (Pearson correlation) with modern extensions (distance correlation). Explanations of advanced methods (Markov chain Monte Carlo) include accessible analogies without sacrificing rigor.',
        'score 5': 'Exemplary Statistical Communication\nManuscripts achieve flawless integration of formal language and statistical precision. Terminology reflects cutting-edge developments, accurately employing phrases like "doubly robust estimation in causal inference" and "frequentist calibration of Bayesian credible intervals". Complex mathematical derivations maintain notational consistency per ISO 80000-2 standards, with careful symbol definition: "Let $\\mathcal{D} = {(x_i,y_i)}_{i=1}^n$ denote the dataset..." Grammar and syntax enhance readability even in dense methodological sections: "Whereas the EM algorithm guarantees convergence to local maxima, stochastic variational inference enables scalable approximation of posterior distributions." Narrative flow expertly guides readers through technical landscapes, using meta-commentary like "This paradox emerges because..." to bridge classical and modern approaches. Literature synthesis demonstrates encyclopedic command of the field while maintaining critical perspective: "Although random forests dominated early ensemble research, gradient boosting\'s explicit loss function optimization represents a theoretical advancement".'
    }
}

CRITICALNESS_DOMAIN_CRITERIA = {
    "cs": {
        'description': 'Criticalness evaluation specific to Computer Science surveys, focusing on technical analysis, methodological critique, and future research directions.',
        'score 1': 'Minimal or No Criticalness\nThe survey primarily summarizes existing work without any evaluative commentary.\nDoes not identify methodological limitations, inconsistencies, or gaps in the literature.\nLacks discussion on challenges or unresolved problems in the field.\nNo original insights or novel perspectives are presented.\nFuture research directions, if present, are absent or purely generic (e.g., "more work needed").',
        'score 2': 'Basic and Superficial Criticalness\nProvides limited critique, mostly descriptive with occasional mention of minor weaknesses.\nIdentifies some gaps but without detailed explanation or contextualization.\nFuture directions are mentioned but remain broad, vague, or conventional (e.g., "improve accuracy," "explore new datasets").\nOriginal insights are minimal and not well integrated into the survey\'s narrative.\nLimited assessment of assumptions or limitations of key methodologies.',
        'score 3': 'Moderate Criticalness with Some Depth\nIdentifies several relevant gaps, challenges, or inconsistencies in the literature with reasonable justification.\nDiscusses strengths and weaknesses of prominent methods, datasets, or evaluation protocols.\nProposes future research directions that are somewhat specific but could benefit from deeper elaboration or stronger justification.\nOffers some original perspectives or synthesis that add value beyond mere summary.\nBegins to critically assess assumptions, scalability, reproducibility, or applicability of surveyed works.',
        'score 4': 'Strong and Well-Justified Criticalness\nProvides a thorough critique highlighting significant gaps, challenges, and limitations in current research.\nEvaluates methodologies rigorously, including their assumptions, performance trade-offs, and practical implications.\nFuture research directions are clearly articulated, actionable, and supported by evidence or trends observed in the literature.\nPresents novel insights or conceptual frameworks that help unify or clarify the field.\nAddresses emerging issues such as fairness, robustness, efficiency, or interpretability where relevant.\nIdentifies under-explored areas or potential interdisciplinary connections.',
        'score 5': 'Exceptional and Insightful Criticalness\nDelivers incisive and comprehensive evaluation of the entire landscape, including nuanced analysis of methodologies, experimental designs, results, and theoretical foundations.\nUncovers hidden assumptions, methodological flaws, or biases that significantly impact the field\'s progress.\nProposes innovative, well-grounded, and feasible future research directions that push boundaries or redefine research agendas.\nProvides highly original conceptual contributions, new taxonomies, or integrative frameworks that advance understanding.\nCritically discusses broader impacts, ethical considerations, and long-term challenges with scholarly rigor.\nDemonstrates mastery of the field by synthesizing diverse perspectives and guiding future work with clarity and vision.'
    },
    "econ": {
        'description': 'Criticalness evaluation specific to Economics surveys, focusing on methodological critique, theoretical analysis, and policy implications.',
        'score 1': 'Non-Critical Compilation\nMethodology: Fails to interrogate identification strategies (e.g., IV validity, DiD parallel trends) or estimation techniques. No discussion of endogeneity threats.\nData: Accepts data limitations (e.g., selection bias in household surveys) without proposing solutions. Ignores measurement error in key variables like wages or inflation expectations.\nTheory: Does not challenge underlying rational expectations or equilibrium assumptions.\nPolicy: Makes generic statements about "policy implications" without mechanism analysis.\nSynthesis: Treats subfields in isolation (e.g., labor vs. macro) without cross-pollination insights.\nFuture Work: Suggests "more research needed" without prioritizing identification challenges or data infrastructure gaps.',
        'score 2': 'Surface-Level Engagement\nMethodology: Notes common techniques (e.g., fixed effects) but doesn\'t compare their relative strengths for causal inference.\nData: Mentions data scarcity in developing contexts but offers no novel collection approaches.\nTheory: Acknowledges behavioral critiques but doesn\'t formalize alternatives.\nPolicy: Links findings to SDGs but lacks cost-benefit analysis.\nSynthesis: Identifies ML applications in econometrics without addressing external validity concerns.\nFuture Work: Proposes extending models to new contexts without addressing fundamental specification issues.',
        'score 3': 'Structured Critique\nMethodology: Evaluates synthetic control vs. interactive fixed effects for policy evaluation, considering finite-sample performance.\nData: Critiques administrative data linkage challenges and proposes blockchain-based solutions.\nTheory: Contrasts neoclassical and complexity economics approaches to market dynamics.\nPolicy: Quantifies tradeoffs between inflation targeting and distributional outcomes using cited simulations.\nSynthesis: Integrates experimental finance findings with macroprudential regulation literature.\nFuture Work: Prioritizes research on heterogeneous treatment effects in universal basic income trials.',
        'score 4': 'Rigorous Interrogation\nMethodology: Exposes overreliance on two-way fixed effects for staggered adoption, demonstrating bias via Monte Carlo simulations.\nData: Develops framework for combining traditional surveys with LLM-generated expectations, addressing measurement error.\nTheory: Reformulates DSGE models with ML-based expectation formation, testing against survey data.\nPolicy: Maps identified causal mechanisms to WTO negotiation positions using game-theoretic analysis.\nSynthesis: Unifies matching estimators from labor economics with macro heterogeneous agent models.\nFuture Work: Proposes federated learning consortiums to bypass data sovereignty barriers in cross-country studies, with governance blueprints.',
        'score 5': 'Field-Defining Insight\nMethodology: Establishes formal equivalence between causal panel methods and structural VARs, deriving optimal estimator selection criteria.\nData: Designs cryptographic protocol for privacy-preserving wage data aggregation, validated through ECB partnership.\nTheory: Synthesizes bounded rationality and rational inattention into unified expectation formation metric, empirically validated across 40 countries.\nPolicy: Demonstrates via counterfactual analysis how incorporating informal sector dynamics would have altered IMF structural adjustment programs.\nSynthesis: Creates taxonomy linking microeconometric tools to macroeconomic externalities through general equilibrium channels.\nFuture Work: Charts 5-year agenda to replace representative agent models with AI-driven heterogeneous system simulations, including NSF funding roadmap.'
    },
    "eess": {
        'description': 'Criticalness evaluation specific to Electrical Engineering and Systems Science surveys, focusing on technical analysis, methodological critique, and practical implications.',
        'score 1': 'Non-Critical Compilation\nFails to analyze technical trade-offs in methodologies (e.g., power grid stability models vs. renewable integration frameworks).\nOmits discussion of reproducibility challenges in hardware-dependent experiments (e.g., FPGA implementations, sensor calibration variances).\nNo evaluation of scalability limits in proposed solutions (e.g., neural network architectures for smart grids under high-dimensional data).\nFuture directions lack alignment with industry roadmaps (e.g., IEEE PES initiatives) or foundational theoretical gaps.',
        'score 2': 'Superficial Technical Assessment\nLimited critique of measurement uncertainties in empirical studies (e.g., ±5% error margins in power quality assessments).\nBriefly mentions but does not quantify interoperability issues (e.g., communication protocols for hybrid AC/DC microgrids).\nGeneric suggestions for future work (e.g., "improve algorithm efficiency") without linking to specific bottlenecks like compute-in-memory hardware constraints.\nOverlooks comparative analysis of competing paradigms (e.g., digital twins vs. physics-based models for fault detection).',
        'score 3': 'Structured Technical Critique\nIdentifies methodological weaknesses in 2–3 domains (e.g., oversimplified assumptions in lithium-ion battery degradation models).\nContrasts simulation vs. real-world performance gaps (e.g., 15–20% overestimation of PV output in MATLAB/Simulink models).\nProposes future work aligned with documented challenges (e.g., federated learning for privacy-preserving load forecasting).\nPartially addresses standardization gaps (e.g., absence of IEEE guidelines for quantum-resistant grid cryptography).',
        'score 4': 'Rigorous Systems-Level Analysis\nExposes critical path limitations in emerging technologies (e.g., 23% efficiency ceiling in perovskite-Si tandem solar cells under real-world soiling conditions).\nQuantifies trade-offs in multi-objective optimization approaches (e.g., 23ms latency reduction vs. 18% increased energy consumption in edge AI systems).\nFuture directions specify performance targets (e.g., "achieve 99.99% distribution system reliability through topology-aware reinforcement learning").\nIntegrates cross-domain insights (e.g., applying blockchain timestamping to mitigate synchrophasor data integrity risks).',
        'score 5': 'Foundational Paradigm Interrogation\nDeconstructs core assumptions in field-establishment theories (e.g., linearity constraints in traditional small-signal stability analysis).\nReveals hidden scalability barriers through first-principles analysis (e.g., 48% commutation failure rate in 10kV SiC MOSFETs under high dV/dt).\nProposes disruptive frameworks validated via counterfactuals (e.g., "achieving 94% fault detection accuracy through neuromorphic event-based sampling" vs. conventional Nyquist-rate methods).\nSynthesizes cross-disciplinary innovation pathways (e.g., leveraging bio-inspired swarm intelligence for self-healing microgrids with <100ms recovery times).'
    },
    "math": {
        'description': 'Criticalness evaluation specific to Mathematics surveys, focusing on theoretical analysis, proof techniques, and mathematical foundations.',
        'score 1': 'Non-Critical Compilation\nLacks mathematical depth: Merely lists results/theorems without analyzing proof techniques, assumptions, or logical dependencies.\nIgnores foundational gaps: Fails to address unresolved conjectures (e.g., Riemann Hypothesis analogues) or limitations in axiomatic frameworks.\nNo original synthesis: Does not identify connections between disparate areas like algebraic topology and category theory.\nFuture directions absent: Omits discussion of open problems from major mathematical institutions (Clay Institute, Hilbert Problems descendants).',
        'score 2': 'Surface-Level Analysis\nLimited technical critique: Acknowledges but doesn\'t dissect methodological weaknesses (e.g., "The proof uses non-constructive methods" without analyzing ZFC implications).\nPartial gap identification: Mentions well-known open problems but ignores emerging challenges in fields like arithmetic dynamics or derived algebraic geometry.\nDerivative insights: Restates standard comparisons (e.g., "Geometric vs algebraic methods") without novel perspectives.\nGeneric future suggestions: Proposes "Further research needed" without specifying tools from motivic integration or homotopy type theory.',
        'score 3': 'Methodological Engagement\nComparative technique analysis: Evaluates competing approaches to major problems (e.g., circle method vs modular forms in additive number theory).\nIdentifies proof-theoretic limitations: Notes where results depend on controversial axioms (Axiom of Choice, Large Cardinal Axioms).\nStructured open problems: Classifies conjectures by difficulty/impact (e.g., "Accessible vs Millennium Prize-level" in geometric analysis).\nPlausible research pathways: Suggests specific tools (e.g., "Apply perverse sheaves to Langlands program geometric aspects").',
        'score 4': 'Foundational Critique\nDeconstructs mathematical paradigms: Analyzes competing definitions (e.g., étale vs crystalline cohomology frameworks) with historical context.\nExposes hidden dependencies: Maps how conjectures in representation theory assume unproven lemmas from model theory.\nOriginal synthesis: Demonstrates how tropical geometry bridges real algebraic geometry and combinatorics.\nActionable innovation pathways: Proposes concrete programs (e.g., "Develop derived moduli spaces using ∞-category theory") with milestone targets.',
        'score 5': 'Field-Redefining Analysis\nMetamathematical evaluation: Critiques entire proof cultures (e.g., "Computer-assisted vs human-verifiable proofs in 4-manifold theory") with epistemological analysis.\nIdentifies foundational crises: Exposes tensions between constructive mathematics and classical results in analysis.\nParadigm-shifting insights: Demonstrates how motivic integration resolves equidistribution problems across multiple fields.\nPrecision-mapped future: Designs research agendas with:\n-Temporal phases: Short-term (e.g., "Complete Fargues-Fontaine curve computations 2025-2027")\n-Technical requirements: "Develop mixed-characteristic Hodge theory for p-adic cohomology"\n-Collaboration matrices: Interdisciplinary bridges between arithmetic geometry and quantum complexity theory.'
    },
    "physics": {
        'description': 'Criticalness evaluation specific to Physics surveys, focusing on theoretical consistency, experimental validation, and fundamental principles.',
        'score 1': 'Non-Critical Compilation\nMerely catalogs existing works without analysis.\nFails to address fundamental physics challenges (e.g., singularities in GR [2303.11696], reproducibility in condensed matter experiments [2301.09434]).\nNo discussion of conflicting theoretical frameworks (e.g., regular BH models vs. semiclassical approximations).\nFuture directions lack connection to open physics problems.',
        'score 2': 'Basic Technical Comparison\nSuperficially contrasts methodologies (e.g., compares numerical relativity approaches without addressing their gauge dependencies).\nIdentifies obvious experimental limitations (e.g., detector sensitivity in gravitational wave astronomy) but lacks depth.\nSuggests generic next steps like "improve computational power" without linking to specific physics goals.\nOverlooks foundational debates (e.g., information paradox implications for regular BHs [2303.11696]).',
        'score 3': 'Domain-Informed Analysis\nEvaluates theoretical consistency (e.g., energy condition violations in modified gravity [2303.11696]).\nDiscusses experimental/observational tensions (e.g., JWST vs. ΛCDM predictions [2406.14684]).\nProposes focused directions like "develop conformal schemes for singularity resolution" with physics justification.\nPartially addresses cross-field connections (e.g., quantum computing applications in lattice QCD [2407.15371]).',
        'score 4': 'Rigorous Physics Critique\nSystematically deconstructs foundational assumptions (e.g., challenges the cosmic censorship hypothesis through regular BH thermodynamics [2303.11696]).\nExposes measurement-theory gaps (e.g., analyzes discrepancies between lab-scale and astrophysical plasma simulations [2407.05004]).\nCharts pathways with concrete milestones (e.g., "Develop experimental protocols for laser-induced nucleation controlling for Kerr nonlinearities [2301.09434]").\nIntegrates multi-scale perspectives (e.g., connects quantum gravity proposals to observable BH shadows [2404.04793]).',
        'score 5': 'Transformative Physics Insight\nReconciles paradoxical results (e.g., resolves tension between AdS/CFT and regular BH thermodynamics [2303.11696]).\nIdentifies underappreciated failure modes (e.g., demonstrates how standard QFT approximations break down in early-universe phase transitions [2406.19780]).\nProposes paradigm-shifting approaches (e.g., "Apply thermodynamic uncertainty relations to BH information paradox [2410.09413]").\nDelivers actionable frameworks (e.g., develops criteria for singularity avoidance across modified gravity theories [2303.11696]).'
    },
    "q-bio": {
        'description': 'Criticalness evaluation specific to Quantitative Biology surveys, focusing on biological relevance, methodological critique, and experimental validation.',
        'score 1': 'Foundational Deficiencies\nMethodologies: Fails to distinguish between computational models (e.g., ML vs. mechanistic models) or biological contexts (e.g., protein folding vs. network biology).\nData Critique: No analysis of dataset limitations (e.g., PDB imbalance, single-cell sequencing batch effects).\nBiological Relevance: Treats biological systems as generic data sources without domain-specific validation.\nReproducibility: Ignores workflow containerization, parameter sensitivity, or benchmark standardization.',
        'score 2': 'Nascent Critical Engagement\nMethod Comparison: Surface-level contrast of tools (AlphaFold vs. RoseTTAFold) without error profile analysis.\nGap Identification: Lists obvious challenges (e.g., "limited training data") without quantifying data scarcity impacts.\nInterdisciplinary Links: Mentions "multi-omics integration" without mechanistic modeling of cross-modality interactions.\nFuture Directions: Suggests generic improvements ("better algorithms") without biological problem grounding.',
        'score 3': 'Structured Critical Analysis\nMethod Evaluation: Systematically compares accuracy-speed tradeoffs in docking software (AutoDock vs. Glide).\nDomain-Specific Gaps: Identifies understudied areas (e.g., membrane protein prediction) with citation analysis.\nBiological Contextualization: Links model performance to experimental validation rates across organism types.\nReproducibility Plan: Proposes benchmark suites for specific tasks (e.g., CASP-style challenges for ligand binding).',
        'score 4': 'Advanced Critical Synthesis\nMethodological Innovation: Deconstructs attention mechanisms in protein language models against biophysical constraints.\nQuantified Gaps: Calculates performance drop-offs for low-abundance protein families using UniProt frequency data.\nCross-Domain Critique: Evaluates systems biology models through both information theory and wet-lab feasibility lenses.\nActionable Roadmaps: Proposes adversarial validation frameworks for single-cell analysis with NIH funding priorities.',
        'score 5': 'Transformative Critical Mastery\nParadigm Analysis: Exposes fundamental limitations of equilibrium assumptions in dynamic system modeling.\nBiological Insight Generation: Derives new protein folding principles from model error patterns across taxonomic groups.\nReproducibility Innovation: Designs blockchain-based protocol for distributed validation of synthetic biology models.\nField-Redirecting Vision: Integrates cryo-EM advancements with active learning pipelines to overcome current resolution barriers.'
    },
    "q-fin": {
        'description': 'Criticalness evaluation specific to Quantitative Finance surveys, focusing on financial models, market applications, and methodological critique.',
        'score 1': 'Non-Critical Compilation\nGaps/Weaknesses: Fails to address well-documented limitations in quantitative finance (e.g., overreliance on stationary market assumptions, neglect of transaction costs, or inadequate backtesting protocols).\nOriginal Insights: Provides no novel synthesis of methods like stochastic volatility modeling, reinforcement learning (RL) in portfolio optimization, or explainable AI (XAI) for trading strategies.\nFuture Directions: Offers generic suggestions (e.g., "more research is needed") without addressing pressing issues like market regime adaptation or high-frequency data latency.\nExample Deficiency: Surveys ML applications without critiquing the reproducibility crisis in financial ML.',
        'score 2': 'Surface-Level Critique\nGaps/Weaknesses: Identifies isolated issues (e.g., "Black-Scholes model limitations") but lacks systemic analysis of interconnected problems like liquidity risk or feedback loops in algorithmic trading.\nOriginal Insights: Limited to restating known challenges (e.g., "curse of dimensionality in option pricing") without linking them to modern solutions like meta-learning or fractional calculus.\nFuture Directions: Suggests broad areas (e.g., "improve deep learning") but ignores domain-specific pathways such as embedding market microstructure into RL agents or dynamic ESG metric integration.\nExample Deficiency: Mentions "data quality issues" without addressing synthetic data generation or alternative data vetting methods.',
        'score 3': 'Moderately Critical Analysis\nGaps/Weaknesses: Discusses specific methodological flaws (e.g., backtest overfitting in factor models or reward function misalignment in RL) but lacks cross-paradigm comparisons (e.g., deep learning vs. econometric approaches).\nOriginal Insights: Partially connects trends (e.g., NLP for earnings call analysis) to broader themes like asymmetric information in multi-agent markets.\nFuture Directions: Proposes plausible ideas (e.g., "incorporate macroeconomic indicators") but misses technical specificity (e.g., using conformal prediction for tail-risk estimation).\nExample Deficiency: Acknowledges non-stationarity but does not evaluate solutions like online learning or regime-switching models.',
        'score 4': 'Rigorous Domain-Specific Critique\nGaps/Weaknesses: Systematically evaluates limitations across paradigms (e.g., comparing stochastic volatility models against neural SDEs in capturing volatility smiles).\nOriginal Insights: Identifies underappreciated synergies (e.g., graph neural networks for interbank contagion analysis or physics-informed ML for arbitrage detection).\nFuture Directions: Prioritizes actionable solutions (e.g., adaptive market impact models for institutional RL agents or federated learning for privacy-preserving alpha generation).\nExample Strength: Critiques LLMs\' hallucination risks in financial text analysis and proposes retrieval-augmented fine-tuning with regulatory disclosures.',
        'score 5': 'Foundational and Transformative Critique\nGaps/Weaknesses: Incisively deconstructs foundational assumptions (e.g., Efficient Market Hypothesis (EMH) validity in LLM-driven markets or fractal inefficiencies in crypto markets).\nOriginal Insights: Introduces novel frameworks (e.g., quantum-inspired optimization for high-dimensional portfolio selection or multi-scale agent-based market simulators).\nFuture Directions: Proposes paradigm-shifting research (e.g., ethical AI arbitrageurs to mitigate flash crashes or decentralized federated learning for cross-institutional risk modeling).\nExample Strength: Reconciles conflicting results in RL-based trading (e.g., policy gradient instability under fat-tailed distributions) and proposes distributionally robust actor-critic architectures.'
    },
    "stat": {
        'description': 'Criticalness evaluation specific to Statistics surveys, focusing on methodological critique, theoretical foundations, and practical applications.',
        'score 1': 'Lacks Statistical Rigor in Critique\nThe survey fails to critically evaluate statistical methodologies, assumptions, or data limitations. Gaps in theoretical foundations (e.g., overlooked biases in estimators, unaddressed violations of model assumptions) are not identified. No discussion of reproducibility crises, computational trade-offs, or emerging challenges in statistical practice. Future directions are generic (e.g., "more research is needed") without ties to statistical innovation.',
        'score 2': 'Superficial Engagement with Statistical Limitations\nWeaknesses in reviewed methods (e.g., reliance on asymptotic properties without finite-sample analysis, incomplete handling of missing data) are mentioned but not contextualized within broader statistical discourse. Limited originality in insights-may cite common critiques (e.g., "p-hacking concerns") without probing root causes. Future directions lack statistical specificity (e.g., "improve models" without addressing causal inference, nonparametric methods, or uncertainty quantification).',
        'score 3': 'Moderately Rigorous Statistical Analysis\nIdentifies methodological gaps (e.g., inadequate treatment of high-dimensional data in classical tests, unexamined robustness to distributional shifts) and references foundational statistical literature. Proposes plausible future work (e.g., integrating Bayesian and frequentist frameworks) but lacks actionable pathways. Original insights are present but underdeveloped (e.g., notes limitations of p-values without proposing alternatives like false discovery rate control or Bayesian posterior predictive checks).',
        'score 4': 'Strong Methodological Critique with Statistical Depth\nSystematically evaluates statistical validity of reviewed approaches (e.g., critiques reliance on Gaussian assumptions in mixed models, highlights collider bias in observational studies). Pinpoints understudied areas (e.g., scalable inference for streaming data, fairness guarantees in predictive modeling) with references to contemporary research. Future directions are statistically grounded (e.g., "develop semiparametric estimators for heterogeneous treatment effects" or "address identifiability challenges in latent variable models"). Novel perspectives include reinterpreting classical paradigms through modern computational lenses.',
        'score 5': 'Transformative Statistical Insight and Innovation\nIncisively deconstructs methodological trade-offs (e.g., bias-variance implications of regularization in sparse regression, pitfalls of post-selection inference). Challenges foundational statistical assumptions (e.g., critiques independence in clustered data, re-examines sufficiency principles in era of big data). Future directions are both technically precise and visionary (e.g., "unify causal discovery algorithms with differential privacy constraints" or "design multi-agent hypothesis testing frameworks for federated learning"). Original contributions include formal proofs of unresolved conjectures, novel taxonomy for emerging statistical paradigms (e.g., "interactive inference" frameworks), or meta-analyses exposing replication failures in high-impact domains.'
    }
}

# -------------- Ranking Evaluation Prompts --------------

OUTLINE_RANKING_PROMPT = """
You are given a list of outlines for academic surveys about the topic "{topic}". Each outline is identified by an index number.

Here are the outlines:
{outlines}

Please rank these outlines based on their quality, considering:
1. Logical organization and hierarchy
2. Coverage of key aspects of the topic
3. Clarity and informativeness of section titles
4. Balance and progression of topics
5. Overall structural coherence

Return your ranking as a JSON object where:
- Keys are the index numbers
- Values are their ranks (1 being the best, higher numbers indicating lower ranks)
- All ranks must be unique integers from 1 to n (where n is the number of outlines)

Example format:
{{
    "1": 2,
    "2": 1,
    "3": 3
}}

Return only the JSON object without any explanation.
"""

CONTENT_RANKING_PROMPT = """
You are given a list of academic survey contents about the topic "{topic}". Each content is identified by an index number.

Here are the contents:
{contents}

Please rank these contents based on their quality, considering:
1. Coverage and comprehensiveness
2. Logical structure and flow
3. Relevance to the topic
4. Language quality and academic tone
5. Critical analysis and insights
6. Overall coherence and readability

Return your ranking as a JSON object where:
- Keys are the index numbers
- Values are their ranks (1 being the best, higher numbers indicating lower ranks)
- All ranks must be unique integers from 1 to n (where n is the number of contents)

Example format:
{{
    "1": 2,
    "2": 1,
    "3": 3
}}

Return only the JSON object without any explanation.
"""

REFERENCE_RANKING_PROMPT = """
You are given a list of reference sections from academic surveys about the topic "{topic}". Each reference section is identified by an index number.

Here are the reference sections:
{references}

Please rank these reference sections based on their quality, considering:
1. Relevance of references to the topic
2. Coverage of key works in the field
3. Recency and comprehensiveness
4. Citation format consistency
5. Overall quality and appropriateness

Return your ranking as a JSON object where:
- Keys are the index numbers
- Values are their ranks (1 being the best, higher numbers indicating lower ranks)
- All ranks must be unique integers from 1 to n (where n is the number of reference sections)

Example format:
{{
    "1": 2,
    "2": 1,
    "3": 3
}}

Return only the JSON object without any explanation.
"""

# -------------- Comparison Prompts --------------

OUTLINE_COMPARISON_PROMPT = """
You are given two outlines for academic surveys about the topic "{topic}". Please compare these outlines and determine which one is better.

Outline 1:
{outline_1}

Outline 2:
{outline_2}

Please compare these outlines and determine if Outline 1 is better than Outline 2, considering:
1. Logical organization and hierarchy
2. Coverage of key aspects of the topic
3. Clarity and informativeness of section titles
4. Balance and progression of topics
5. Overall structural coherence

Return your answer as a JSON object:
{{
    "is_better": true/false,  // whether Outline 1 is better than Outline 2
    "reason": "brief explanation of your decision"
}}

Return only the JSON object without any explanation.
"""

CONTENT_COMPARISON_PROMPT = """
You are given two academic survey contents about the topic "{topic}". Please compare these contents and determine which one is better.

Content 1:
{content_1}

Content 2:
{content_2}

Please compare these contents and determine if Content 1 is better than Content 2, considering:
1. Coverage and comprehensiveness of the topic
2. Logical structure and flow
3. Relevance and accuracy of information
4. Quality of language and readability
5. Depth of critical analysis
6. Overall effectiveness as a survey

Return your answer as a JSON object:
{{
    "is_better": true/false,  // whether Content 1 is better than Content 2
    "reason": "brief explanation of your decision"
}}

Return only the JSON object without any explanation.
"""

REFERENCE_COMPARISON_PROMPT = """
You are given two reference sections from academic surveys about the topic "{topic}". Please compare these references and determine which one is better.

References 1:
{references_1}

References 2:
{references_2}

Please compare these references and determine if References 1 is better than References 2, considering:
1. Relevance to the topic
2. Coverage of key works in the field
3. Recency and timeliness
4. Consistency in citation format
5. Overall quality and comprehensiveness

Return your answer as a JSON object:
{{
    "is_better": true/false,  // whether References 1 is better than References 2
    "reason": "brief explanation of your decision"
}}

Return only the JSON object without any explanation.
"""