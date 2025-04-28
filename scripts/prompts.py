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