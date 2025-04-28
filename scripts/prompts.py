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