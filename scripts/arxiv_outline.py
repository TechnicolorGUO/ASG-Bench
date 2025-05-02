import os
import requests
import argparse
from bs4 import BeautifulSoup
import json
import urllib3

urllib3.disable_warnings()

def download_arxiv_html(arxiv_id, save_dir):
    """
    下载arxiv论文html到本地
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    filename = arxiv_id.replace("/", "ovo") + ".txt"
    save_path = os.path.join(save_dir, filename)
    url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    try:
        resp = requests.get(url, verify=False, timeout=30)
        resp.raise_for_status()
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"Downloaded HTML to {save_path}")
        return save_path
    except Exception as e:
        print(f"Error downloading {arxiv_id}: {e}")
        return None

def extract_outline_from_html(html_path, output_json):
    """
    解析html，提取大纲
    """
    try:
        with open(html_path, encoding='utf-8') as f:
            text = f.read()
        soup = BeautifulSoup(text, 'html.parser')

        # 获取论文标题
        title_tag = soup.find('title')
        if title_tag:
            paper_title = title_tag.get_text().strip()
        else:
            paper_title = "Unknown Title"

        outline = []
        # 第一项是论文名
        outline.append([1, paper_title])

        # 逐级解析 section, subsection, ...
        for section in soup.find_all('section'):
            # 查找section下的第一个标题
            h = section.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if h:
                title = h.get_text().strip()
            else:
                # 兼容部分section没有h标签
                title = section.text.split('\n')[0].strip()
            if title:
                # 判断级别
                prefix = title.split(' ')[0]
                if '.' in prefix:
                    level = prefix.count('.') + 2  # "1." -> 2, "1.1." -> 3 等
                    # 但有些是"1.1"，没有最后一个点
                    if prefix[-1] != '.':
                        level = prefix.count('.') + 2
                    if level > 5:
                        level = 5
                else:
                    level = 2
                outline.append([level, title])

        # 如果没找到section，直接找h1/h2/h3...
        if len(outline) == 1:
            for i, htag in enumerate(['h1', 'h2', 'h3', 'h4']):
                for h in soup.find_all(htag):
                    title = h.get_text().strip()
                    if title:
                        outline.append([i+2, title])

        # 保存json
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(outline, f, indent=2, ensure_ascii=False)
        print(f"Saved outline to {output_json}")
    except Exception as e:
        print(f"Error extracting outline: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arxiv_id", type=str, required=True, help="arxiv论文id,如2312.00001")
    parser.add_argument("--output_json", type=str, default="outline.json", help="输出的json文件路径")
    parser.add_argument("--tmp_html_dir", type=str, default="./tmp_html", help="临时HTML存放路径")
    args = parser.parse_args()

    html_path = download_arxiv_html(args.arxiv_id, args.tmp_html_dir)
    if html_path:
        extract_outline_from_html(html_path, args.output_json)