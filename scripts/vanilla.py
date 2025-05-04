import json
import os
from prompts import CONTENT_GENERATE_BY_OUTLINE_PROMPT, CONTENT_GENERATE_WITHOUT_OUTLINE_PROMPT, OUTLINE_GENERATE_PROMPT
from utils import generateResponse, getClient, robust_json_parse, robust_list_parse

# -------------------- Generate with outline --------------------

def generate_outline(topic:str) -> list:
    client = getClient()
    prompt = OUTLINE_GENERATE_PROMPT.format(topic=topic)
    raw_response = generateResponse(client, prompt, max_tokens=768, temperature=0.5)
    outline = robust_list_parse(raw_response)
    if outline is None:
        print(f"Failed to parse outline for topic: {topic}")
        return []
    print(f"Generated outline for topic: {topic}")
    print(outline)
    return outline

def generate_content_by_outline(topic: str, outline: list, max_tokens=4096):
    client = getClient()
    result = {}
    n = len(outline)
    i = 0

    while i < n:
        # 找到下一个一级标题
        if outline[i][0] == 1:
            section = [outline[i]]
            section_title = outline[i][1]
            # 收集所有下属二级及三级标题
            j = i + 1
            while j < n and outline[j][0] > 1:
                section.append(outline[j])
                j += 1

            # 构造 prompt
            prompt = CONTENT_GENERATE_BY_OUTLINE_PROMPT.format(
                topic=topic,
                outline = outline,
                section_group = section,
            )
            # 调用 LLM
            raw_response = generateResponse(client, prompt, max_tokens=max_tokens, temperature=0.5)
            content_obj = robust_json_parse(raw_response)
            if not content_obj or "content" not in content_obj:
                print(f"Failed to get content for section: {section_title}")
                result[section_title] = ""
            else:
                print(f"Generated content for section: {section_title}")
                result[section_title] = content_obj["content"]

            i = j  # 跳到下一个一级section
        else:
            i += 1

    return result

def save_outline_content(topic: str, output_dir: str):
    outline = generate_outline(topic)
    if not outline:
        print("Failed to generate outline.")
        return

    content = generate_content_by_outline(topic, outline)
    if not content:
        print("Failed to generate content.")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    outline_path = os.path.join(output_dir, "outline.json")
    content_path = os.path.join(output_dir, f"{topic}.md")

    # Save outline to outline.json
    with open(outline_path, "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)
    print(f"Saved outline to {outline_path}")


    # Save markdown content to {topic}.md
    with open(content_path, "w", encoding="utf-8") as f:
        # content是{section_title: md_text}，拼接所有内容
        for section_title, md_text in content.items():
            # 保证所有 \n 都是实际换行
            md_text = md_text.replace('\\n', '\n')
            f.write(md_text.strip())
            f.write('\n\n')

    
    print(f"Saved content to {content_path}")

def generate_outline_content_all_topics(root_dir="surveys"):
    for category in os.listdir(root_dir):
        category_path = os.path.join(root_dir, category)
        if not os.path.isdir(category_path):
            continue
        for topic in os.listdir(category_path):
            topic_path = os.path.join(category_path, topic)
            if not os.path.isdir(topic_path):
                continue

            vanilla_dir = os.path.join(topic_path, "vanilla_outline")
            os.makedirs(vanilla_dir, exist_ok=True)
            md_path = os.path.join(vanilla_dir, f"{topic}.md")
            if os.path.exists(md_path):
                print(f"Skipped '{topic}' in '{category}' (already exists).")
                continue

            print(f"Processing topic '{topic}' in category '{category}'...")

            try:
                save_outline_content(topic, vanilla_dir)
            except Exception as e:
                print(f"Failed to process {topic}: {e}")

# -------------------- Generate without outline --------------------
def generate_content(topic: str, max_tokens=4096):
    client = getClient()
    prompt = CONTENT_GENERATE_WITHOUT_OUTLINE_PROMPT.format(topic=topic)
    raw_response = generateResponse(client, prompt, max_tokens=max_tokens, temperature=0.5)
    content_obj = robust_json_parse(raw_response)
    if not content_obj or "content" not in content_obj:
        print(f"Failed to get content for topic: {topic}")
        return ""
    return content_obj["content"]

def save_content(topic: str, output_dir: str):
    """
    自动生成并保存指定topic的vanilla markdown内容到 output_dir/<topic>.md
    """
    content = generate_content(topic)
    if not content:
        print(f"Failed to generate content for topic: {topic}")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    content_path = os.path.join(output_dir, f"{topic}.md")
    with open(content_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
        f.write("\n")
    print(f"Saved content to {content_path}")

def generate_content_all_topics(root_dir="surveys"):
    for category in os.listdir(root_dir):
        category_path = os.path.join(root_dir, category)
        if not os.path.isdir(category_path):
            continue
        for topic in os.listdir(category_path):
            topic_path = os.path.join(category_path, topic)
            if not os.path.isdir(topic_path):
                continue

            vanilla_dir = os.path.join(topic_path, "vanilla")
            os.makedirs(vanilla_dir, exist_ok=True)
            md_path = os.path.join(vanilla_dir, f"{topic}.md")
            if os.path.exists(md_path):
                print(f"Skipped '{topic}' in '{category}' (already exists).")
                continue

            print(f"Processing topic '{topic}' in category '{category}'...")

            try:
                save_content(topic, vanilla_dir)
            except Exception as e:
                print(f"Failed to process {topic}: {e}")

if __name__ == "__main__":
    # output_dir = "surveys/cs/3D Gaussian Splatting Techniques/vanilla"
    # topic = "3D Gaussian Splatting Techniques"
    # save_outline_content(topic, output_dir)
    # save_content(topic, output_dir)
    generate_content_all_topics()