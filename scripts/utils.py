import json
import os
import re
from openai import OpenAI

from dotenv import load_dotenv
import requests
load_dotenv()

def getClient(): 
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    openai_api_base = os.environ.get("OPENAI_API_BASE")

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )
    return client

def generateResponse(client, prompt, max_tokens=768, temerature=0.5):
    chat_response = client.chat.completions.create(
        model=os.environ.get("MODEL"),
        max_tokens=max_tokens,
        temperature=temerature,
        stop="<|im_end|>",
        stream=True,
        messages=[{"role": "user", "content": prompt}]
    )

    text = ""
    for chunk in chat_response:
        if chunk.choices[0].delta.content:
            text += chunk.choices[0].delta.content
    return text

def robust_json_parse(raw_response):
    try:
        return json.loads(raw_response)
    except Exception:
        match = re.search(r'(\{.*\})', raw_response, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except Exception:
                pass
        raise ValueError("Failed to parse LLM response as JSON:\n" + raw_response)
    
def download_arxiv_pdf(arxiv_id: str, save_dir: str) -> str:
    """
    下载 arXiv 论文 PDF 到指定目录
    :param arxiv_id: arXiv 主ID（如 '2301.00001'）
    :param save_dir: 目标文件夹路径（如 './pdfs'）
    :return: 保存后的PDF文件路径
    :raises: Exception 如果下载失败
    """
    # 构造PDF下载URL
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    # 确保文件夹存在
    os.makedirs(save_dir, exist_ok=True)
    # 文件名
    file_path = os.path.join(save_dir, f"{arxiv_id}.pdf")

    # 如果已经存在，则跳过下载
    if os.path.exists(file_path):
        print(f"PDF already exists: {file_path}")
        return file_path

    print(f"Downloading {pdf_url} ...")
    try:
        resp = requests.get(pdf_url, stream=True, timeout=20)
        resp.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Saved: {file_path}")
        return file_path
    except Exception as e:
        # 如果下载失败，尝试删除未完成的文件
        if os.path.exists(file_path):
            os.remove(file_path)
        print(f"Failed to download {arxiv_id}: {e}")
        raise