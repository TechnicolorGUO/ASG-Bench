import json
import re
import csv
import os


def convert_round_to_square_brackets(text):
    """
    将圆括号内的作者-年份引用替换为中括号，支持2018a等格式。
    支持 (Smith et al., 2018a; Brown et al., 2017) 变成 [Smith et al., 2018a; Brown et al., 2017]
    """
    # 匹配 (Author et al., 2018a; AuthorB et al., 2017)
    pattern = re.compile(r'\(([A-Z][^()]+?, \d{4}[a-z]?([;，][^()]+?, \d{4}[a-z]?)*?)\)')
    return pattern.sub(r'[\1]', text)

def acl_ref_to_key(ref):
    """
    将 ACL 格式参考文献字符串转换为 [Author et al., 2018a] 格式
    支持单作者、两作者、三及以上作者情况
    """
    # 1. 找年份+可选字母后缀
    year_match = re.search(r'\b(20\d{2}[a-z]?|19\d{2}[a-z]?)\b', ref)
    year = year_match.group(1) if year_match else '????'

    # 2. 提取作者段
    # authors_part = ref.split('.')[0].strip()
    authors_part = ref[:year_match.start()].strip() if year_match else ref.split('.')[0].strip()
    # 替换 " and " 为逗号，方便统一处理
    authors_part = authors_part.replace(' and ', ', ')
    # 拆分作者
    author_names = [a.strip() for a in authors_part.split(',') if a.strip()]

    # 提取每个人的姓
    surnames = []
    for name in author_names:
        if ',' in name:
            surnames.append(name.split(',')[0].strip().strip('.'))
        else:
            surnames.append(name.split()[-1].strip().strip('.'))

    if len(surnames) == 1:
        key = f'[{surnames[0]}, {year}]'
    elif len(surnames) == 2:
        key = f'[{surnames[0]} and {surnames[1]}, {year}]'
    elif len(surnames) >= 3:
        key = f'[{surnames[0]} et al., {year}]'
    else:
        key = f'[Unknown, {year}]'
    return key

def extract_citation_spans(sentence):
    """
    提取所有中括号内的引用片段
    """
    return re.findall(r'\[[^\]]+\]', sentence)

def is_numeric_citation(citation):
    """
    判断是否为纯数字型引用（如[1,3,5-7]或[25]–[28]）
    """
    # 匹配 [1,3,5-7] 也匹配 [25]–[28]（区间可在 expand_citation 里处理）
    return re.match(r'^\[\d+([\s,\-–，]*\d+)*\]$', citation) or \
           re.match(r'^\[\d+\]\s*[\-–]\s*\[\d+\]$', citation)

def is_author_year_citation(citation):
    """
    判断是否为作者-年份型引用:
    - 长形式 [Chen et al., 2023c; Xie et al., 2023]
    - 简缩写形式 [Abé10], [AL18]
    """
    # 形式1: 作者+4位数字年份
    if re.search(r'[A-Za-z].*?\d{4}', citation):
        return True
    # 形式2: 作者+2位数字/字母 (如 [AL18], [Abé10])
    # 通常是大写字母+2位数字，或包含特殊字符
    if re.search(r'\[\s*[A-Za-z]{2,}[0-9]{2,}[a-z]?\s*\]', citation):
        return True
    # 可以扩展其他变体
    return False

def merge_all_numeric_citations(sentence):
    ids = []

    # 1. 提取所有区间 [num]–[num]
    pattern_range = re.compile(r'\[(\d+)\]\s*[\-–]\s*\[(\d+)\]')
    for m in pattern_range.finditer(sentence):
        start, end = int(m.group(1)), int(m.group(2))
        ids.extend(range(start, end + 1))
    # 2. 去掉区间，处理剩下的单中括号
    sentence_wo_ranges = pattern_range.sub('', sentence)
    singles = [int(m.group(1)) for m in re.finditer(r'\[(\d+)\]', sentence_wo_ranges)]
    ids.extend(singles)
    # 3. 去重排序
    ids = sorted(set(ids))
    if ids:
        # 4. 合成为一个中括号字符串
        merged = '[' + ','.join(str(i) for i in ids) + ']'
        return merged
    else:
        return None

def expand_citation(raw_citation):
    """
    输入如 '[1,3,5-7]' 或 '[25]–[28]'，输出所有涉及的数字编号，去重排序
    """
    ref_ids = []
    # 1. 处理所有 [num] - [num]、[num]–[num]，如 [25]–[28]
    pattern = re.compile(r'\[(\d+)\]\s*[\-–]\s*\[(\d+)\]')
    # 复制一份，防止替换后影响 bracket_pattern
    temp_citation = raw_citation
    for match in pattern.finditer(temp_citation):
        start, end = int(match.group(1)), int(match.group(2))
        ref_ids.extend(range(start, end + 1))
        # 替换当前已处理的部分，避免后续重复处理
        raw_citation = raw_citation.replace(match.group(0), '')
    # 2. 处理单中括号内的区间/列表，如 [1,3,5-7]
    bracket_pattern = re.compile(r'\[(.*?)\]')
    for bracket in bracket_pattern.findall(raw_citation):
        for part in bracket.split(','):
            part = part.strip()
            if '-' in part or '–' in part:
                subpattern = re.compile(r'(\d+)[\-–](\d+)')
                submatch = subpattern.match(part)
                if submatch:
                    start, end = map(int, submatch.groups())
                    ref_ids.extend(range(start, end + 1))
            else:
                try:
                    ref_ids.append(int(part))
                except ValueError:
                    continue
    return sorted(set(ref_ids))

def get_continuous_refs(matches):
    """从编号1开始，拼接所有能承接的区间，允许重复编号或比最大编号小的编号出现"""
    refs = []
    next_idx = 1
    used = set()  # 已用过的区间下标
    while True:
        found = False
        for i, (start, end) in enumerate(matches):
            if i in used:
                continue
            if start == next_idx:
                refs.append((start, end))
                next_idx = end + 1
                used.add(i)
                found = True
                break  # 找到后立即拼接，继续查找下一个
        if not found:
            break  # 没有能承接的区间，停止
    return refs

def find_inline_references(para, initial_max=None):
    """
    返回para中的所有引用区间，按出现顺序。
    每次append后立即用end更新max，只保留end <= current_max + 1的区间。
    """
    matches = []
    # 先找区间
    for match in re.finditer(r'(?<!\d)(\d{1,3})\s*[–-]\s*(\d{1,3})\b', para):
        start, end = int(match.group(1)), int(match.group(2))
        if start < end:
            matches.append((start, end, match.start()))
    # 再找单个
    for match in re.finditer(r'(?<!\d)(\d{1,3})\b', para):
        idx = int(match.group(1))
        if not any(start <= idx <= end for start, end, _ in matches):
            matches.append((idx, idx, match.start()))
    matches.sort(key=lambda x: x[2])

    filtered = []
    current_max = initial_max if initial_max is not None else 0
    for start, end, _ in matches:
        if end <= current_max + 1:
            filtered.append((start, end))
            if end > current_max:
                current_max = end
    return filtered

def split_markdown_content_and_refs(content):
    """
    输入 Markdown 内容，返回 (正文内容, 参考文献块) 元组
    """
    # 1. 最严格：# References
    ref_header = re.compile(r'^(#{1,6})\s*References\s*$', re.IGNORECASE | re.MULTILINE)
    header_match = ref_header.search(content)

    if header_match:
        start = header_match.end()
        next_header = re.search(r'^#{1,6}\s+\S+', content[start:], re.MULTILINE)
        end = start + next_header.start() if next_header else len(content)
        main_content = content[:header_match.start()].strip() + "\n"
        main_content += content[start + (next_header.end() if next_header else 0):].strip() if next_header else ""
        ref_block = content[start:end].strip()
    else:
        # 2. 次严格：# ...reference...
        loose_header = re.compile(r'^#{1,6}.*reference', re.IGNORECASE | re.MULTILINE)
        loose_match = loose_header.search(content)
        if loose_match:
            start = loose_match.end()
            next_header = re.search(r'^#{1,6}\s+\S+', content[start:], re.MULTILINE)
            end = start + next_header.start() if next_header else len(content)
            main_content = content[:loose_match.start()].strip() + "\n"
            main_content += content[start + (next_header.end() if next_header else 0):].strip() if next_header else ""
            ref_block = content[start:end].strip()
        else:
            # 3. 检测 [1] 样式的参考文献编号
            numbered_ref = re.compile(r'^\[\d+\]', re.MULTILINE)
            numbered_match = numbered_ref.search(content)
            if numbered_match:
                start = numbered_match.start()
                main_content = content[:start].strip()
                ref_block = content[start:].strip()
            else:
                # 4. 最宽松：全文最后一个 reference(s) 或者bibliography
                ref_word = re.compile(r'\b(bibliography|references?)\b', re.IGNORECASE)
                matches = list(ref_word.finditer(content))
                if matches:
                    last_ref = matches[-1]
                    start = last_ref.end()
                    next_header = re.search(r'^#{1,6}\s+\S+', content[start:], re.MULTILINE)
                    end = start + next_header.start() if next_header else len(content)
                    main_content = content[:last_ref.start()].strip() + "\n"
                    main_content += content[start + (next_header.end() if next_header else 0):].strip() if next_header else ""
                    ref_block = content[start:end].strip()
                else:
                    # 5. 都没有
                    main_content = content.strip()
                    ref_block = ""
    return main_content, ref_block

def parse_markdown(content):
    """
    解析 Markdown 内容，提取完整句子和引用信息
    :param content: 输入的 Markdown 内容
    :return: 
        results: dict，key为带引用的完整句子，value为该句子用到的参考文献内容列表
        references: list，所有参考文献（顺序保存）
    """
    # 1. 抽refs
    main_content, ref_block = split_markdown_content_and_refs(content)

    # 2. 提取参考文献条目（兼容各种编号和无编号，条目间可空行分隔）
    # 检测以[xxx]开头的条目（如 [1] 或 [Agashe et al., 2023]），否则用空行分割

    # 标准化数字型引用格式
    def standardize_numeric_refs(block):
        def repl(match):
            num = match.group(1)
            return f'[{num}] '
        # 支持 1.  1)  1 A.  1 Pleiss 等等
        return re.sub(r'^\s*(\d+)(?:[\.\)]\s+|\s+(?=[A-Z]))', repl, block, flags=re.MULTILINE)

    ref_block = standardize_numeric_refs(ref_block)
    lines = [line for line in ref_block.splitlines() if line.strip()]
    bracket_lines = sum(1 for line in lines if line.strip().startswith("["))
    if ref_block and bracket_lines >= len(lines) // 2:
        # 用正则以[xxx]开头分割
        entries = re.split(r'(?=^\[.*?\])', ref_block, flags=re.MULTILINE)
        entries = [entry.strip() for entry in entries if entry.strip()]
    else:
        # 用空行分割
        # entries = re.split(r"\n\s*\n", ref_block)
        # entries = [entry.strip() for entry in entries if entry.strip()]
        entries = [line.strip() for line in ref_block.splitlines() if line.strip()]
    
    # 3. 建立参考文献编号到内容的映射
    # 对于[编号]，编号可为数字或文本，为字符串；无编号则用顺序号
    references = []
    ref_id_map = {}  # key: 编号(str) 或作者-年份key，value: 条目内容
    auto_id = 1      # 自动编号从1开始

    for idx, entry in enumerate(entries):
        m = re.match(r'^\[(.+?)\]\s*(.*)', entry, re.DOTALL)
        if m:
            ref_id = m.group(1).strip()
            ref_text = m.group(2).strip()
            ref_id_map[ref_id] = ref_text
            references.append(entry.strip())
        else:
            # 检查是否ACL风格，如果是就调用acl_ref_to_key
            key = acl_ref_to_key(entry)
            if key and key.startswith('[') and key.endswith(']') and ',' in key:
                # key 形如 [Smith et al., 2018a]，存map时去掉方括号和空格
                ref_id = key.strip('[]').strip()
                ref_id_map[ref_id] = entry.strip()
                references.append(entry.strip())
            else:
                # 都不是，就用自动编号
                ref_id = str(auto_id)
                ref_text = entry.strip()
                ref_id_map[ref_id] = ref_text
                references.append(f'[{ref_id}] {ref_text}')
                auto_id += 1

    # 4. 预处理正文内容（去除图片/公式/html）
    main_content = re.sub(r'!\[.*?\]\(.*?\)', '', main_content)
    main_content = re.sub(r'<html>.*?</html>', '', main_content, flags=re.DOTALL)
    # main_content = re.sub(r'\$.*?\$', '', main_content, flags=re.DOTALL)
    # main_content = re.sub(r'^\s*\$\$[\s\S]*?\$\$\s*$', '', main_content, flags=re.MULTILINE)
    main_content_wo_section = re.sub(r'^#+\s+.*$', '', main_content, flags=re.MULTILINE)
    main_content_wo_section = re.sub(r'\n{2,}', '\n', main_content_wo_section)  # 合并空行

    # 5. 用正则分割句子（适合英文）
    pattern = r'\.(?=\s+[A-Z]|\n|[A-Z])'
    paragraphs = re.split(pattern, main_content_wo_section)
    paragraphs = [sentence.strip() for sentence in paragraphs if sentence.strip()]


    results = {}

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        para = convert_round_to_square_brackets(para)
        ref_list = []
        already_handled = set()

        # 先合并所有数字型引用（区间和单独编号），直接展开
        merged_citation = merge_all_numeric_citations(para)
        if merged_citation:
            ids = expand_citation(merged_citation)
            for rid in ids:
                if rid not in already_handled:
                    ref_text = ref_id_map.get(str(rid))
                    if ref_text:
                        ref_list.append(f"[{rid}] {ref_text}")
                        already_handled.add(rid)

        # 再处理作者-年份型引用
        # 提取所有中括号引用
        author_year_citations = re.findall(r'([A-Z][A-Za-z\-]+(?: et al\.)?)\s*\((20\d{2}[a-z]?|19\d{2}[a-z]?)\)', para)
        for surname, year in author_year_citations:
            surname = surname.strip()
            key = f"[{surname}, {year}]"
            alt_key = f"[{surname.replace('et al.', 'et al')}, {year}]"  # 去掉句点试试
            for k in (key, alt_key):
                if k not in already_handled:
                    ref_text = ref_id_map.get(k)
                    if ref_text:
                        ref_list.append(f"{k} {ref_text}")
                        already_handled.add(k)
                        break
        citations = extract_citation_spans(para)
        for citation in citations:
            if is_author_year_citation(citation):
                # 去掉头尾中括号，按分号分割
                refs = [r.strip() for r in citation.strip("[]").split(';')]
                for ref in refs:
                    if ref and ref not in already_handled:
                        ref_text = ref_id_map.get(ref)
                        if ref_text:
                            ref_list.append(f"[{ref}] {ref_text}")
                            already_handled.add(ref)

        if ref_list:
            results[para] = ref_list
    # 只对 Introduction 到结尾做兜底引用识别
    intro_match = re.search(r'^.*#.*introduction.*$', main_content, re.IGNORECASE | re.MULTILINE)
    if intro_match:
        main_content_for_fallback = main_content[intro_match.start():].strip()
    else:
        main_content_for_fallback = main_content

    pattern = r'\.(?=\s+[A-Z]|\n|[A-Z])'
    fallback_paragraphs = re.split(pattern, main_content_for_fallback)
    fallback_paragraphs = [p.strip() for p in fallback_paragraphs if p.strip()]

    if not results:
        current_max = 0  # 或你希望的初始值
        for para in fallback_paragraphs:
            para = para.strip()
            if not para:
                continue
            # 传入当前max
            matches = find_inline_references(para, initial_max=current_max)
            ref_list = []
            already_handled = set()
            if matches:
                for start, end in matches:
                    for rid in range(start, end + 1):
                        if rid not in already_handled:
                            ref_text = ref_id_map.get(str(rid))
                            if ref_text:
                                ref_list.append(f"[{rid}] {ref_text}")
                                already_handled.add(rid)
                    # 每append一次更新current_max
                    if end > current_max:
                        current_max = end
            if ref_list:
                results[para] = ref_list
    if not results:
        for para in fallback_paragraphs:
            para = para.strip()
            if not para:
                continue
            ref_list = []
            already_handled = set()
            # 遍历ref_id_map，提取key的第一个单词（作者姓）
            for k in ref_id_map:
                # 提取第一个单词（字母+可选连字符）
                m = re.match(r'\[?([A-Z][A-Za-z\-]*)', k)
                if m:
                    surname = m.group(1)
                    # 如果段落里出现这个姓氏且还没处理过
                    if surname in para and k not in already_handled:
                        ref_text = ref_id_map[k]
                        ref_list.append(f"{k} {ref_text}")
                        already_handled.add(k)
            if ref_list:
                results[para] = ref_list
    return results, references

def extract_refs(input_file, output_folder):
    """
    处理单个 Markdown 文件，将句子与引用对应关系保存到 CSV 和 JSON 文件，
    并保存全部参考文献的列表（按编号顺序）。
    """
    if not os.path.isfile(input_file):
        print(f"错误：输入文件 {input_file} 不存在，跳过该文件。")
        return

    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as e:
            print(f"错误：无法创建输出文件夹 {output_folder}，错误信息：{e}，跳过该文件。")
            return

    output_file_name = os.path.basename(input_file).replace('.md', '')
    output_csv = os.path.join(output_folder, output_file_name + '.csv')
    output_ref_list_json = os.path.join(output_folder, 'references.json')

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        data, references = parse_markdown(content)
    except FileNotFoundError:
        print(f"错误：未找到文件 {input_file}，跳过该文件。")
        return
    except Exception as e:
        print(f"处理文件 {input_file} 时发生未知错误：{e}，跳过该文件。")
        return

    # data: {sentence: [refs]}
    unique_data = {}
    for sentence, refs in data.items():
        unique_data[sentence] = list(dict.fromkeys(refs))  # 去重但保顺序

    # 写 CSV
    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            # 使用转义字符和引号
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
            writer.writerow(["sentence", "references"])
            for sentence, refs in unique_data.items():
                # 使用 "；" 拼接引用列表
                refs_str = ";".join(refs)
                writer.writerow([sentence, refs_str])  # 写入一行
    except PermissionError:
        print(f"错误：没有权限写入文件 {output_csv}，跳过该文件。")
    except Exception as e:
        print(f"写入文件 {output_csv} 时发生未知错误：{e}，跳过该文件。")

    try:
        # references: {编号: 内容}，要按编号从小到大排序
        ref_list = references
        with open(output_ref_list_json, 'w', encoding='utf-8') as f:
            json.dump(ref_list, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"写入文件 {output_ref_list_json} 时发生未知错误：{e}，跳过该文件。")

if __name__ == "__main__":
    # # 输入文件目录
    # dir_path = "md_file/md_file/my_file"
    # # 输出文件夹名称
    # output_folder = "output_new_csv_files"

    # # 验证输入目录是否有效
    # if not os.path.isdir(dir_path):
    #     print(f"错误：输入目录 {dir_path} 不存在，请检查路径。")
    # else:
    #     for root, _, files in os.walk(dir_path):
    #         for file in files:
    #             file_path = os.path.join(root, file)
    #             main(input_file=file_path, output_folder=output_folder)
    #     print("所有文件处理完毕")
    # main(input_file="surveys\cs/3D Gaussian Splatting Techniques\pdfs/2401.03890.md", output_folder="surveys\cs/3D Gaussian Splatting Techniques\pdfs")
    # extract_refs(input_file="surveys/cs/3D Gaussian Splatting Techniques/pdfs/2401.03890.md", output_folder="surveys/cs/3D Gaussian Splatting Techniques/pdfs")
    # surveys\cs\Large Language Model Based Multi-Agent Systems\pdfs\2402.01680.md
    # extract_refs(input_file="surveys/cs/Large Language Model Based Multi-Agent Systems/pdfs/2402.01680.md", output_folder="surveys/cs/Large Language Model Based Multi-Agent Systems/pdfs")
    # surveys\cs\Natural Language to Code Generation with Large Language Models\pdfs\2212.09420.md
    # extract_refs(input_file="surveys/cs/Natural Language to Code Generation with Large Language Models/pdfs/2212.09420.md", output_folder="surveys/cs/Natural Language to Code Generation with Large Language Models/pdfs")

    # surveys\<category>\<topic>\pdfs\<filename>.md 进行extract_refs
    # for cat in os.listdir("surveys"):
    #     cat_path = os.path.join("surveys", cat)
    #     if not os.path.isdir(cat_path):
    #         continue
    #     for topic in os.listdir(cat_path):
    #         topic_path = os.path.join(cat_path, topic)
    #         if not os.path.isdir(topic_path):
    #             continue
    #         md_path = os.path.join(topic_path, "pdfs")
    #         if not os.path.isdir(md_path):
    #             continue
    #         for file in os.listdir(md_path):
    #             if not file.lower().endswith(".md"):
    #                 continue
    #             file_path = os.path.join(md_path, file)
    #             extract_refs(input_file=file_path, output_folder=md_path)
    # extract_refs(input_file="surveys\cs/3D Gaussian Splatting Techniques\AutoSurvey/3D Gaussian Splatting Techniques.md", output_folder="surveys\cs/3D Gaussian Splatting Techniques\AutoSurvey")
    # surveys\cs\3D Gaussian Splatting Techniques\InteractiveSurvey\survey_3D Gaussian Splatting Techniques.md
    extract_refs(input_file="surveys/cs/3D Gaussian Splatting Techniques/InteractiveSurvey/survey_3D Gaussian Splatting Techniques.md", output_folder="surveys/cs/3D Gaussian Splatting Techniques/InteractiveSurvey")