import os
import re
import json
import logging
from typing import Dict, List, Tuple, Optional, Any, Union
from pathlib import Path
from dataclasses import dataclass, asdict, field
from datetime import datetime

from utils.markdown_to_json import (
    MarkdownToJsonConverter,
    split_survey_into_parts,
    extract_outline,
    parse_markdown_references
)

# LLM相关导入
try:
    from openai import OpenAI
    from dotenv import load_dotenv
    load_dotenv()
    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False
    logging.warning("OpenAI library not available. LLM features will be disabled.")


# ==================== 数据结构定义 ====================

@dataclass
class OutlineItem:
    """
    大纲项数据结构
    
    Attributes:
        level: 标题级别 (1, 2, 3...)
        title: 标题文本
    """
    level: int
    title: str
    
    def to_list(self) -> List[Union[int, str]]:
        """转换为 [level, title] 格式"""
        return [self.level, self.title]
    
    @classmethod
    def from_list(cls, item: List) -> 'OutlineItem':
        """从 [level, title] 格式创建"""
        if len(item) != 2:
            raise ValueError(f"Invalid outline item format: {item}")
        return cls(level=item[0], title=item[1])

@dataclass
class Outline:
    """
    大纲数据结构
    
    Attributes:
        items: 大纲项列表
    """
    items: List[OutlineItem]

    def to_list(self) -> List[List]:
        """转换为 [level, title] 格式"""
        return [item.to_list() for item in self.items]
    
    @classmethod
    def from_list(cls, items: List[List]) -> 'Outline':
        """从 [level, title] 格式创建"""
        return cls(items=[OutlineItem.from_list(item) for item in items])

@dataclass
class ContentSection:
    """
    内容章节数据结构
    
    Attributes:
        heading: 章节标题
        level: 章节级别
        content: 章节内容文本
        stats: 统计信息 (可选)
    """
    heading: str
    level: int
    content: str
    stats: Optional[Dict[str, int]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        result = {
            'heading': self.heading,
            'level': self.level,
            'content': self.content
        }
        if self.stats:
            result['stats'] = self.stats
        return result
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ContentSection':
        """从字典格式创建"""
        return cls(
            heading=data.get('heading', ''),
            level=data.get('level', 0),
            content=data.get('content', ''),
            stats=data.get('stats')
        )

@dataclass
class Content:
    """
    Content数据结构
    
    Attributes:
        sections: 内容章节列表
    """
    sections: List[ContentSection]

    def to_list(self) -> List[Dict]:
        """转换为字典格式"""
        return [section.to_dict() for section in self.sections]
    
    @classmethod
    def from_list(cls, sections: List[Dict]) -> 'Content':
        """从字典格式创建"""
        return cls(sections=[ContentSection.from_dict(section) for section in sections])

@dataclass
class ReferenceEntry:
    """
    ReferenceEntry数据结构
    
    Attributes:
        number: 引用编号
        title: 引用标题
    """
    text: str
    number: int | None
    title: str
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'text': self.text,
            'number': self.number,
            'title': self.title
        }
    @classmethod
    def from_dict(cls, data: Union[Dict, str]) -> 'ReferenceEntry':
        """从字典格式或字符串创建"""
        if isinstance(data, str):
            # 如果是字符串，解析出编号和标题
            return cls(text=data, number=None, title=data)
        else:
            # 如果是字典，从字典中提取
            return cls(
                text=data.get('text', ''),
                number=data.get('number'),
                title=data.get('title', '')
            )

@dataclass
class References:
    """
    References数据结构
    
    Attributes:
        entries: 引用条目列表
    """
    entries: List[ReferenceEntry]

    def to_list(self) -> List[Dict]:
        """转换为字典格式"""
        return [entry.to_dict() for entry in self.entries]
    
    @classmethod
    def from_list(cls, entries: List[Union[Dict, str]]) -> 'References':
        """从字典列表或字符串列表格式创建"""
        return cls(entries=[ReferenceEntry.from_dict(entry) for entry in entries])

@dataclass
class SurveyData:
    """
    综述数据完整结构
    
    Attributes:
        outline: 大纲列表
        content: 内容章节列表
        references: 引用列表
        metadata: 元数据 (可选)
    """
    outline: Outline = field(default_factory=Outline)
    content: Content = field(default_factory=Content)
    references: References = field(default_factory=References)
    metadata: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式（用于JSON序列化）"""
        result = {
            'outline': self.outline.to_list(),
            'content': self.content.to_list(),
            'references': self.references.to_list()
        }
        if self.metadata:
            result['metadata'] = self.metadata
        return result
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SurveyData':
        """从字典格式创建"""
        return cls(
            outline=Outline.from_list(data.get('outline', [])),
            content=Content.from_list(data.get('content', [])),
            references=References.from_list(data.get('references', [])),
            metadata=data.get('metadata')
        )
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取数据统计信息"""
        total_content = ' '.join([section.content for section in self.content.sections])
        return {
            'outline_count': len(self.outline.items),
            'section_count': len(self.content.sections),
            'reference_count': len(self.references.entries),
            'total_chars': len(total_content),
            'total_words': len(total_content.split()),
            'sections_with_content': sum(1 for s in self.content.sections if s.content.strip())
        }


# ==================== 配置类 ====================

@dataclass
class DataProcessingConfig:
    """数据处理配置"""
    # 路径配置
    input_dir: str = "results/original"  # 输入目录
    output_dir: str = "results/processed"  # 输出目录
    systems: Optional[List[str]] = None  # 要处理的系统列表（如 Autosurvey），None表示所有系统
    categories: Optional[List[str]] = None  # 要处理的类别列表（如 Biology, Computer Science），None表示所有类别
    auto_convert_markdown: bool = True  # 是否自动转换 Markdown 文件为 JSON
    overwrite_original_json: bool = False  # Markdown 转 JSON 时是否覆盖已存在的原始 JSON 文件

    # Outline配置
    normalize_outline: bool = True  # 是否标准化outline
    llm_calibration: bool = False  # 是否使用LLM进行大纲校准
    remove_empty_titles: bool = True  # 是否移除空标题

    # Content配置
    normalize_content: bool = True  # 是否标准化content
    remove_short_sections: bool = False  # 是否移除过短的章节
    min_section_words: int = 10  # 最少章节字数
    calculate_section_stats: bool = True  # 是否计算章节统计信息
    
    # Reference配置
    normalize_references: bool = True  # 是否标准化references
    keep_number: bool = False  # 是否保留引用编号
    llm_quality_check: bool = False  # 是否使用LLM进行质量检查
    remove_duplicate_refs: bool = True  # 是否移除重复引用
    
    # LLM配置
    llm_api_base: str = None  # OpenRouter API 基础URL
    llm_api_key: Optional[str] = None  # LLM API Key (从环境变量读取)
    llm_model: str = None  # LLM 模型名称
    llm_temperature: float = 0.0  # LLM 温度参数
    llm_enable_reasoning: bool = False  # 是否启用推理功能
    
    # 质量检查配置
    enable_quality_check: bool = False  # 是否启用质量检查
    min_outline_items: int = 3  # 最少大纲项数
    min_references: int = 5  # 最少引用数
    min_total_content_length: int = 1000  # 最少总内容长度（字符数）

    # 日志配置
    log_level: str = "INFO"
    log_file: str = "data_processing.log"
    
    def get_systems(self, base_dir: Optional[str] = None) -> List[str]:
        """
        获取要处理的系统列表
        
        Args:
            base_dir: 基础目录，默认使用input_dir
            
        Returns:
            List[str]: 系统列表（如 Autosurvey）
        """
        if self.systems:
            return self.systems
        
        base_dir = base_dir or self.input_dir
        if not os.path.exists(base_dir):
            return []
        
        # 返回所有子目录作为系统
        return [d for d in os.listdir(base_dir) 
                if os.path.isdir(os.path.join(base_dir, d))]
    
    def get_categories_in_system(self, system: str, base_dir: Optional[str] = None) -> List[str]:
        """
        获取指定系统下的类别列表
        
        Args:
            system: 系统名称（如 Autosurvey）
            base_dir: 基础目录，默认使用input_dir
            
        Returns:
            List[str]: 类别列表（如 Biology, Computer Science等）
        """
        base_dir = base_dir or self.input_dir
        system_path = os.path.join(base_dir, system)
        
        if not os.path.exists(system_path):
            return []
        
        if self.categories:
            # 过滤指定的类别
            available = [d for d in os.listdir(system_path) 
                        if os.path.isdir(os.path.join(system_path, d))]
            return [c for c in self.categories if c in available]
        
        # 返回所有类别
        return [d for d in os.listdir(system_path) 
                if os.path.isdir(os.path.join(system_path, d))]


# ==================== 辅助函数（无状态，定义在外部）====================

def setup_logging(config: DataProcessingConfig) -> logging.Logger:
    """
    配置日志系统
    
    Args:
        config: 数据处理配置
        
    Returns:
        logging.Logger: 配置好的logger
    """
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """
    标准化文本：去除多余空白、统一换行符等
    
    Args:
        text: 原始文本
        
    Returns:
        str: 标准化后的文本
    """
    # 统一换行符
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # 去除行尾空白
    text = re.sub(r'[ \t]+\n', '\n', text)
    
    # 合并多个空行为单个空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 去除首尾空白
    text = text.strip()
    
    return text


def remove_noise_patterns(text: str) -> str:
    """
    移除常见的噪声模式
    
    Args:
        text: 原始文本
        
    Returns:
        str: 清洗后的文本
    """
    # 移除图片路径中的噪声
    text = re.sub(r'!\[.*?\]\(images/[a-f0-9]+\.jpg\)', '[Image]', text)
    
    # 移除过长的数学公式（可能是OCR错误）
    text = re.sub(r'\$\$[^\$]{500,}\$\$', '[Formula]', text)
    
    # 移除重复的特殊字符
    text = re.sub(r'([^\w\s])\1{3,}', r'\1', text)

    # 移除URL
    text = re.sub(r'https?://[^\s]+', '', text)
    text = re.sub(r'www\.[^\s]+', '', text)
    text = re.sub(r'ftp://[^\s]+', '', text)
    text = re.sub(r'mailto://[^\s]+', '', text)
    text = re.sub(r'tel://[^\s]+', '', text)
    text = re.sub(r'file://[^\s]+', '', text)
    text = re.sub(r'magnet://[^\s]+', '', text)
    text = re.sub(r'irc://[^\s]+', '', text)
    text = re.sub(r'ircs://[^\s]+', '', text)
    return text
    
    
def clean_reference_text(ref: str) -> str:
    """
    清洗单条引用文本（简单版本，用于列表清理）
    
    Args:
        ref: 原始引用文本
        
    Returns:
        str: 清洗后的引用
    """
    # 标准化空白
    ref = ' '.join(ref.split())
    
    # 去除首尾空白
    ref = ref.strip()
    
    return ref


def extract_reference_title(reference: str) -> Tuple[Optional[int], str]:
    """
    从引用文本中提取编号和标题
    
    合并的Pattern分类：
    - Pattern A (1, 2, 4, 5, 6, 8): 标准格式 [num] 或 num. 开头，直接提取标题
    - Pattern B (3): [cite: num] 格式，包含期刊信息，需要清理
    - Pattern C (7, 9): 标题后跟作者名列表，需要分离
    
    Args:
        reference: 原始引用文本
        
    Returns:
        Tuple[Optional[int], str]: (编号, 标题)
    """
    if not reference or not reference.strip():
        return (None, "")
    
    # ===== 预处理 =====
    # 去除换行符
    text = reference.replace('\n', ' ').replace('\r', ' ')
    
    # 转小写
    text = text.lower()
    
    # 去除多余空格
    text = ' '.join(text.split())
    
    if not text:
        return (None, "")
    
    # ===== 提取编号 =====
    num = None
    
    # Pattern: [cite: 1] 或 [1] 或 1. 或 1) 
    num_pattern = r'^\[?(?:cite:\s*)?(\d+)[\]\.)\s]+'
    num_match = re.match(num_pattern, text)
    
    if num_match:
        num = int(num_match.group(1))
        # 移除编号部分
        text = text[num_match.end():].strip()
    
    # ===== 清理文本 =====
    
    # 移除 URL (包括 URL: 前缀)
    text = re.sub(r'\burl:\s*https?://\S+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'www\.\S+', '', text)
    
    # 移除 DOI
    text = re.sub(r'\bdoi:\s*\S+', '', text, flags=re.IGNORECASE)
    
    # 移除期刊信息: *journal name*, vol(issue), pages
    # 例如: *Revista de Psicología*, 19(38), 41-62
    text = re.sub(r'\*[^*]+\*,?\s*\d+\(\d+\),\s*\d+-\d+', '', text)
    
    # 移除尾部的 [cite: num]
    text = re.sub(r'\[cite:\s*\d+\]\s*$', '', text)
    
    # 移除年份: (1936–2024) 或 (2023) 或年份在末尾
    text = re.sub(r'\(\d{4}(?:[-–—]\d{4})?\)', '', text)
    text = re.sub(r',?\s*\d{4}(?:[-–—]\d{4})?\s*\.?\s*$', '', text)  # 移除末尾年份
    
    # ===== 提取标题（去除作者名和期刊名） =====
    
    # 策略1: 查找常见的期刊名模式 "Journal Name. (Year). Title"
    # 如果匹配到这个模式，提取第一个句号前的内容作为期刊名
    journal_pattern = r'^([^.]+)\.\s*\(\d{4}\)\.\s*(.+)$'
    journal_match = re.match(journal_pattern, text)
    if journal_match:
        # 这种情况下，第一部分是期刊名，第二部分是标题
        # 但根据你的需求，可能是要保留期刊名
        # 让我们保留第一个句号前的内容
        text = journal_match.group(1).strip()
    else:
        # 策略2: 如果文本中有句号，分析句号前后的内容
        # 通常：Title. Author1, Author2, Author3
        # 或者：Journal. Title
        parts = text.split('.')
        if len(parts) >= 2:
            # 检查第二部分是否像作者名列表（多个逗号分隔的名字）
            second_part = parts[1].strip()
            # 如果第二部分有多个逗号，很可能是作者列表
            if second_part.count(',') >= 2:
                # 第一部分是标题
                text = parts[0].strip()
            # 如果第一部分很短（<30个字符），第二部分较长，可能第一部分是期刊名
            elif len(parts[0]) < 30 and len(second_part) > len(parts[0]):
                # 第二部分可能是标题
                # 但需要清理作者名
                title_candidate = second_part
                # 移除可能的作者名（逗号分隔的人名）
                author_removal = re.sub(r'[,;]\s*[a-z]+\s+[a-z]+.*$', '', title_candidate)
                if author_removal:
                    text = author_removal.strip()
                else:
                    text = parts[0].strip()
            else:
                # 默认使用第一部分
                text = parts[0].strip()
    
    # 策略3: 移除末尾的作者名模式
    # 例如: ", Author1, Author2" 或 ". Author1, Author2"
    text = re.sub(r'[.,]\s+[a-z]+\s+[a-z]+(?:,\s+[a-z]+\s+[a-z]+)+.*$', '', text)
    
    # 移除 "and Author" 这样的模式（只在有逗号的情况下，避免误删标题中的 "and"）
    text = re.sub(r',\s+and\s+[a-z]+\s+[a-z]+.*$', '', text)
    
    # ===== 最终清理 =====
    
    # 去除多余的标点和空格
    text = text.strip(' .,;:')
    
    # 合并多余空格
    text = ' '.join(text.split())
    
    # 移除连续的句号
    text = re.sub(r'\.{2,}', '.', text)
    text = text.strip('.')
    
    return (num, text) 
    

def calculate_text_stats(text: str) -> Dict[str, int]:
    """
    计算文本统计信息
    
    Args:
        text: 文本内容
        
    Returns:
        Dict: 统计信息
    """
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    
    return {
        'char_count': len(text),
        'word_count': len(words),
        'sentence_count': len([s for s in sentences if s.strip()]),
        'line_count': len(text.split('\n'))
    }


def robust_json_parse(response_text: str, max_retries: int = 3) -> Optional[Dict]:
    """
    稳健的 JSON 解析函数，处理解析失败的情况，带有限次重试。
    
    使用正则提取第一个 { 和最后一个 } 之间的内容（包含括号），
    可以处理 LLM 在 JSON 外添加额外文本的情况。支持最多 `max_retries`
    次尝试，每次都会做一次简单清理后再解析。
    
    Args:
        response_text: JSON 响应文本
        max_retries: 最大重试次数（默认 3）
        
    Returns:
        Optional[Dict]: 解析后的字典，失败时返回 None
    """
    cleaned = response_text
    for attempt in range(1, max_retries + 1):
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # 尝试提取 JSON 片段
            match = re.search(r'\{.*\}', cleaned, re.DOTALL)
            if match:
                json_str = match.group(0)
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    pass
            
            if attempt < max_retries:
                # 基础清理后再重试：去掉包裹的代码块、首尾空白
                cleaned = cleaned.strip()
                cleaned = re.sub(r'^```(?:json)?\s*', '', cleaned)
                cleaned = re.sub(r'```$', '', cleaned)
                logging.warning(
                    f"JSON parse failed (attempt {attempt}/{max_retries-1}), retrying..."
                )
            else:
                logging.warning("Failed to parse JSON response after retries")
                logging.warning(f"Response: {cleaned[:500]}...")
                return None

# ==================== 核心清洗类 ====================

class ContentCleaner:
    """内容清洗器 - 负责清洗outline和content"""
    
    def __init__(self, config: DataProcessingConfig):
        """
        初始化清洗器
        
        Args:
            config: 数据处理配置
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def clean_outline(self, outline: List[List]) -> List[OutlineItem]:
        """
        清洗outline数据
        
        Args:
            outline: 原始outline [[level, title], ...]
            
        Returns:
            List[OutlineItem]: 清洗后的outline
        """
        cleaned_outline = []
        
        for item in outline:
            try:
                outline_item = OutlineItem.from_list(item)
                
                # 清洗标题
                if self.config.normalize_outline:
                    outline_item.title = normalize_text(outline_item.title)
                    outline_item.title = remove_noise_patterns(outline_item.title)
                
                # 移除空标题
                if self.config.remove_empty_titles:
                    if not outline_item.title or len(outline_item.title.strip()) < 2:
                        self.logger.debug(f"Skipping empty title at level {outline_item.level}")
                        continue
                
                cleaned_outline.append(outline_item)
                
            except Exception as e:
                self.logger.warning(f"Invalid outline item: {item}, error: {e}")
                continue
        
        self.logger.info(f"Cleaned outline: {len(outline)} -> {len(cleaned_outline)} items")
        return cleaned_outline
    
    def clean_content_sections(self, content_sections: List[Dict]) -> List[ContentSection]:
        """
        清洗content sections数据
        
        Args:
            content_sections: 原始content sections
            
        Returns:
            List[ContentSection]: 清洗后的sections
        """
        cleaned_sections = []
        
        for section_data in content_sections:
            try:
                section = ContentSection.from_dict(section_data)
                
                # 清洗内容
                if self.config.normalize_content:
                    section.content = normalize_text(section.content)
                    section.content = remove_noise_patterns(section.content)
                    section.heading = normalize_text(section.heading)
                
                # 检查内容长度
                if self.config.remove_short_sections:
                    word_count = len(section.content.split())
                    if word_count < self.config.min_section_words:
                        self.logger.debug(
                            f"Skipping short section '{section.heading}' ({word_count} words)"
                        )
                        continue
                
                # 计算统计信息
                if self.config.calculate_section_stats:
                    section.stats = calculate_text_stats(section.content)
                
                cleaned_sections.append(section)
                
            except Exception as e:
                self.logger.warning(f"Error cleaning section: {e}")
                continue
        
        self.logger.info(
            f"Cleaned sections: {len(content_sections)} -> {len(cleaned_sections)} sections"
        )
        return cleaned_sections


class ReferenceCleaner:
    """引用清洗器 - 负责清洗和标准化references"""
    
    def __init__(self, config: DataProcessingConfig):
        """
        初始化引用清洗器
        
        Args:
            config: 数据处理配置
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # 初始化LLM客户端
        self.llm_client = None
        if self.config.llm_quality_check and LLM_AVAILABLE:
            # 从 .env 文件读取配置（优先级高于 config）
            api_key = os.environ.get("API_KEY") or self.config.llm_api_key
            base_url = os.environ.get("BASE_URL") or self.config.llm_api_base
            
            if api_key:
                self.llm_client = OpenAI(
                    api_key=api_key,
                    base_url=base_url
                )
                self.logger.info(f"LLM client initialized with model: {self.config.llm_model}")
                self.logger.info(f"Using base URL: {base_url}")
            else:
                self.logger.warning("LLM quality check enabled but no API key found (set API_KEY in .env)")
        elif self.config.llm_quality_check and not LLM_AVAILABLE:
            self.logger.warning("LLM quality check enabled but OpenAI library not available")
    
    def extract_reference_with_llm(self, reference_text: str) -> Tuple[int, str]:
        """
        使用LLM提取引用的编号和标题
        
        Args:
            reference_text: 原始引用文本
            
        Returns:
            Tuple[int, str]: (编号, 标题)，如果没有编号则返回0
        """
        if not self.llm_client:
            self.logger.warning("LLM client not available, falling back to regex extraction")
            return extract_reference_title(reference_text)
        
        try:
            prompt = f"""You are a reference parser. Extract the reference number and title from the following reference text.

Reference text:
{reference_text}

Please extract:
1. The reference number (if present, otherwise return 0)
2. The title of the paper/article

Return your answer in the following JSON format:
{{
    "number": <number as integer, 0 if not present>,
    "title": "<title as string>"
}}

Guidelines:
- Remove URLs, DOIs, author names, journal names, publication years, and other metadata
- Extract only the core title of the work
- If there's no explicit number, use 0
- Keep the title concise and clean
"""

            # 构建请求参数
            request_params = {
                "model": self.config.llm_model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": self.config.llm_temperature,
                "response_format": {"type": "json_object"}
            }
            
            # 如果启用推理功能，添加 extra_body
            if self.config.llm_enable_reasoning:
                request_params["extra_body"] = {"reasoning": {"enabled": False}}
            
            completion = self.llm_client.chat.completions.create(**request_params)
            
            # 解析LLM响应
            response_text = completion.choices[0].message.content
            response_data = robust_json_parse(response_text)
            
            # 如果解析失败，降级到正则表达式
            if response_data is None:
                self.logger.warning("JSON parsing failed, falling back to regex")
                return extract_reference_title(reference_text)
            
            number = response_data.get("number", 0)
            title = response_data.get("title", "").strip()
            
            # 确保 number 是整数
            if number is None or number == "":
                number = 0
            else:
                try:
                    number = int(number)
                except (ValueError, TypeError):
                    number = 0
            
            if not title:
                self.logger.warning(f"LLM returned empty title for reference: {reference_text[:100]}...")
                # 降级到正则表达式
                return extract_reference_title(reference_text)
            
            return (number, title)
            
        except Exception as e:
            self.logger.warning(f"LLM extraction failed: {e}, falling back to regex")
            return extract_reference_title(reference_text)
    
    def clean_references(self, reference_entries: List[ReferenceEntry]) -> List[ReferenceEntry]:
        """
        清洗引用列表，提取标题并移除多余信息
        
        Args:
            reference_entries: 原始引用条目列表
            
        Returns:
            List[ReferenceEntry]: 清洗后的引用条目列表
        """
        cleaned_refs = []
        seen_refs = set()  # 用于去重
        
        for entry in reference_entries:
            # 如果需要标准化，重新提取标题
            if self.config.normalize_references:
                # 根据配置选择提取方法
                if self.config.llm_quality_check and self.llm_client:
                    # 使用 LLM 提取编号和标题
                    num, title = self.extract_reference_with_llm(entry.text)
                else:
                    # 使用正则表达式提取编号和标题
                    num, title = extract_reference_title(entry.text)
                
                # 构建清洗后的引用文本
                if num is not None and num != 0 and self.config.keep_number:
                    cleaned_text = f"[{num}] {title}"
                else:
                    cleaned_text = title
                
                # 创建新的 ReferenceEntry
                cleaned_entry = ReferenceEntry(
                    text=cleaned_text,
                    number=num if self.config.keep_number else None,
                    title=title
                )
            else:
                # 不标准化，保持原样（但去除首尾空白）
                cleaned_entry = ReferenceEntry(
                    text=entry.text.strip(),
                    number=entry.number,
                    title=entry.title
                )
            
            # 移除空引用
            if not cleaned_entry.title or cleaned_entry.text == "[]":
                self.logger.debug("Skipping empty reference")
                continue
            
            # 去重
            if self.config.remove_duplicate_refs:
                # 使用小写标题进行去重比较
                ref_key = cleaned_entry.title.lower().strip()
                
                if not ref_key:
                    continue
                    
                if ref_key in seen_refs:
                    self.logger.debug(f"Skipping duplicate reference: {ref_key[:50]}...")
                    continue
                seen_refs.add(ref_key)
            
            cleaned_refs.append(cleaned_entry)
        
        self.logger.info(f"Cleaned references: {len(reference_entries)} -> {len(cleaned_refs)} items")
        return cleaned_refs


class QualityChecker:
    """质量检查器 - 验证处理后数据的质量"""
    
    def __init__(self, config: DataProcessingConfig):
        """
        初始化质量检查器
        
        Args:
            config: 数据处理配置
        """
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def check_data_quality(self, survey_data: SurveyData) -> Tuple[bool, List[str]]:
        """
        检查数据质量
        
        Args:
            survey_data: 综述数据对象
            
        Returns:
            Tuple[bool, List[str]]: (是否通过, 问题列表)
        """
        issues = []
        
        # 检查outline
        if len(survey_data.outline.items) < self.config.min_outline_items:
            issues.append(
                f"Outline too short: {len(survey_data.outline.items)} items "
                f"(min: {self.config.min_outline_items})"
            )
        
        # 检查content
        if not survey_data.content.sections:
            issues.append("No content sections found")
        
        # 检查references
        if len(survey_data.references.entries) < self.config.min_references:
            issues.append(
                f"Too few references: {len(survey_data.references.entries)} "
                f"(min: {self.config.min_references})"
            )
        
        # 检查内容长度
        total_content = ' '.join([section.content for section in survey_data.content.sections])
        if len(total_content) < self.config.min_total_content_length:
            issues.append(
                f"Content too short: {len(total_content)} chars "
                f"(min: {self.config.min_total_content_length})"
            )
        
        # 检查空内容章节
        empty_sections = sum(1 for section in survey_data.content.sections if not section.content.strip())
        if empty_sections > 0:
            issues.append(f"Found {empty_sections} empty content sections")
        
        passed = len(issues) == 0
        
        if not passed:
            self.logger.warning(f"Quality check failed: {len(issues)} issues found")
            for issue in issues:
                self.logger.warning(f"  - {issue}")
        else:
            self.logger.info("Quality check passed")
        
        return passed, issues
    
    def generate_quality_report(self, survey_data: SurveyData) -> Dict[str, Any]:
        """
        生成详细的质量报告
        
        Args:
            survey_data: 综述数据对象
            
        Returns:
            Dict: 质量报告
        """
        passed, issues = self.check_data_quality(survey_data)
        stats = survey_data.get_statistics()
        
        # 计算额外指标
        avg_section_length = (
            stats['total_chars'] / stats['section_count'] 
            if stats['section_count'] > 0 else 0
        )
        
        level_distribution = {}
        for item in survey_data.outline.items:
            level_distribution[item.level] = level_distribution.get(item.level, 0) + 1
        
        return {
            'passed': passed,
            'issues': issues,
            'statistics': stats,
            'metrics': {
                'avg_section_length': round(avg_section_length, 2),
                'outline_depth': max([item.level for item in survey_data.outline.items]) if survey_data.outline.items else 0,
                'level_distribution': level_distribution,
                'empty_sections': stats['section_count'] - stats['sections_with_content']
            }
        }


# ==================== 主流水线类 ====================

class DataProcessingPipeline:
    """
    数据处理流水线主类
    
    负责协调整个数据处理流程
    """
    
    def __init__(self, config: Optional[DataProcessingConfig] = None):
        """
        初始化流水线
        
        Args:
            config: 数据处理配置，如果为None则使用默认配置
        """
        self.config = config or DataProcessingConfig()
        self.logger = setup_logging(self.config)
        
        # 初始化各个组件
        self.content_cleaner = ContentCleaner(self.config)
        self.reference_cleaner = ReferenceCleaner(self.config)
        self.quality_checker = QualityChecker(self.config)
        
        self.logger.info("Data Processing Pipeline initialized")
    
    def process_single_file(self, json_path: str, output_path: Optional[str] = None) -> SurveyData:
        """
        处理单个JSON文件
        
        Args:
            json_path: 输入JSON文件路径
            output_path: 输出JSON文件路径（可选）
            
        Returns:
            SurveyData: 处理后的数据对象
        """
        self.logger.info(f"Processing: {json_path}")
        
        try:
            # Step 1: 读取原始JSON数据
            self.logger.info("Step 1: Loading JSON data...")
            with open(json_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # Step 2: 转换为数据对象
            self.logger.info("Step 2: Parsing data structure...")
            survey_data = SurveyData.from_dict(raw_data)
            
            # Step 3: 清洗outline
            self.logger.info("Step 3: Cleaning outline...")
            cleaned_outline_items = self.content_cleaner.clean_outline(
                survey_data.outline.to_list()
            )
            survey_data.outline = Outline(items=cleaned_outline_items)
            
            # Step 4: 清洗content
            self.logger.info("Step 4: Cleaning content...")
            cleaned_content_sections = self.content_cleaner.clean_content_sections(
                survey_data.content.to_list()
            )
            survey_data.content = Content(sections=cleaned_content_sections)
            
            # Step 5: 清洗references
            self.logger.info("Step 5: Cleaning references...")
            cleaned_ref_entries = self.reference_cleaner.clean_references(
                survey_data.references.entries
            )
            survey_data.references = References(entries=cleaned_ref_entries)
            
            # Step 6: 添加/更新元数据
            self.logger.info("Step 6: Adding metadata...")
            survey_data.metadata = {
                'source_file': json_path,
                'processed_date': datetime.now().isoformat(),
                'config': {
                    'normalize_outline': self.config.normalize_outline,
                    'normalize_content': self.config.normalize_content,
                    'normalize_references': self.config.normalize_references
                }
            }
            
            # Step 7: 质量检查
            if self.config.enable_quality_check:
                self.logger.info("Step 7: Quality check...")
                quality_report = self.quality_checker.generate_quality_report(survey_data)
                survey_data.metadata['quality_check'] = quality_report
            
            # Step 8: 保存结果
            if output_path:
                self._save_json(survey_data, output_path)
            
            self.logger.info(f"Successfully processed: {json_path}")
            return survey_data
            
        except Exception as e:
            self.logger.error(f"Error processing {json_path}: {e}", exc_info=True)
            raise
    
    def convert_markdown_files(self, directory: str) -> Dict[str, Any]:
        """
        检查目录中的 Markdown 文件，如果没有对应的 JSON，则转换
        
        Args:
            directory: 要检查的目录路径
            
        Returns:
            Dict: 转换结果统计
        """
        self.logger.info(f"Checking for markdown files in: {directory}")
        
        dir_path = Path(directory)
        if not dir_path.exists():
            self.logger.warning(f"Directory does not exist: {directory}")
            return {'total': 0, 'converted': 0, 'skipped': 0, 'failed': 0}
        
        # 查找所有 .md 文件
        md_files = list(dir_path.rglob("*.md"))
        
        results = {
            'total': len(md_files),
            'converted': 0,
            'skipped': 0,
            'failed': 0,
            'details': []
        }
        
        for md_file in md_files:
            try:
                # 检查是否已有对应的 JSON 文件
                json_file = md_file.with_suffix('').with_suffix('.json')
                if json_file.name.endswith('_split.json'):
                    json_file = md_file.with_name(md_file.stem + '_split.json')
                else:
                    json_file = md_file.with_name(md_file.stem + '_split.json')
                
                if json_file.exists() and not self.config.overwrite_original_json:
                    self.logger.debug(f"JSON already exists for: {md_file.name} (skipping, overwrite=False)")
                    results['skipped'] += 1
                    results['details'].append({
                        'file': str(md_file),
                        'status': 'skipped',
                        'reason': 'json_exists'
                    })
                    continue
                
                if json_file.exists() and self.config.overwrite_original_json:
                    self.logger.info(f"Overwriting existing JSON for: {md_file.name}")
                
                # 转换 MD 到 JSON
                self.logger.info(f"Converting markdown to JSON: {md_file.name}")
                converter = MarkdownToJsonConverter(str(md_file))
                converter.parse()
                output_path = converter.save_json()
                
                results['converted'] += 1
                results['details'].append({
                    'file': str(md_file),
                    'status': 'converted',
                    'output': output_path
                })
                
            except Exception as e:
                self.logger.error(f"Failed to convert {md_file}: {e}")
                results['failed'] += 1
                results['details'].append({
                    'file': str(md_file),
                    'status': 'failed',
                    'error': str(e)
                })
        
        self.logger.info(
            f"Markdown conversion complete: {results['converted']} converted, "
            f"{results['skipped']} skipped, {results['failed']} failed"
        )
        
        return results
    
    def process_directory(self, 
                         input_dir: Optional[str] = None,
                         output_dir: Optional[str] = None,
                         pattern: str = "*_split.json",
                         auto_convert_markdown: Optional[bool] = None) -> Dict[str, Any]:
        """
        批量处理目录中的JSON文件
        
        Args:
            input_dir: 输入目录（可选，使用配置中的默认值）
            output_dir: 输出目录（可选，使用配置中的默认值）
            pattern: 文件匹配模式
            auto_convert_markdown: 是否自动转换 Markdown 文件（None 使用配置默认值）
            
        Returns:
            Dict: 处理结果统计
        """
        input_dir = input_dir or self.config.input_dir
        output_dir = output_dir or self.config.output_dir
        
        # 使用配置中的默认值（如果未指定）
        if auto_convert_markdown is None:
            auto_convert_markdown = self.config.auto_convert_markdown
        
        self.logger.info(f"Batch processing directory: {input_dir}")
        
        # Step 0: 自动转换 Markdown 文件（如果启用）
        markdown_results = None
        if auto_convert_markdown:
            self.logger.info("Step 0: Checking and converting markdown files...")
            markdown_results = self.convert_markdown_files(input_dir)
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 查找所有JSON文件
        input_path = Path(input_dir)
        json_files = list(input_path.rglob(pattern))
        
        self.logger.info(f"Found {len(json_files)} JSON files matching '{pattern}'")
        
        results = {
            'total': len(json_files),
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'details': []
        }
        
        for json_file in json_files:
            try:
                # 构建输出路径（保持目录结构）
                relative_path = json_file.relative_to(input_path)
                output_path = Path(output_dir) / relative_path
                
                # 如果输出文件已存在且较新，则跳过
                if output_path.exists():
                    if output_path.stat().st_mtime > json_file.stat().st_mtime:
                        self.logger.info(f"Skipping (up-to-date): {json_file}")
                        results['skipped'] += 1
                        continue
                
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # 处理文件
                survey_data = self.process_single_file(str(json_file), str(output_path))
                
                # 获取统计信息
                stats = survey_data.get_statistics()
                quality_passed = survey_data.metadata.get('quality_check', {}).get('passed', True)
                
                results['success'] += 1
                results['details'].append({
                    'file': str(json_file),
                    'status': 'success',
                    'output': str(output_path),
                    'quality_passed': quality_passed,
                    'statistics': stats
                })
                
            except Exception as e:
                self.logger.error(f"Failed to process {json_file}: {e}")
                results['failed'] += 1
                results['details'].append({
                    'file': str(json_file),
                    'status': 'failed',
                    'error': str(e)
                })
        
        # 保存批处理结果
        summary_path = Path(output_dir) / 'processing_summary.json'
        summary_data = {
            'markdown_conversion': markdown_results,
            'json_processing': results
        }
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)
        
        self.logger.info(
            f"Batch processing complete: "
            f"{results['success']}/{results['total']} succeeded, "
            f"{results['failed']} failed, "
            f"{results['skipped']} skipped"
        )
        
        if markdown_results:
            self.logger.info(
                f"Markdown conversion: "
                f"{markdown_results['converted']} converted, "
                f"{markdown_results['skipped']} skipped, "
                f"{markdown_results['failed']} failed"
            )
        
        return summary_data
    
    def process_by_category(self, 
                           category: Optional[str] = None,
                           system: Optional[str] = None) -> Dict[str, Any]:
        """
        按系统和类别处理数据
        
        Args:
            category: 类别名称（可选，None表示所有类别，如 Biology, Computer Science）
            system: 系统名称（可选，None表示所有系统，如 Autosurvey）
            
        Returns:
            Dict: 处理结果统计
        """
        systems = [system] if system else self.config.get_systems()
        
        all_results = {
            'systems_processed': 0,
            'categories_processed': 0,
            'total_files': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'by_system': {}
        }
        
        for sys in systems:
            self.logger.info(f"Processing system: {sys}")
            
            # 获取该系统下的类别
            categories = [category] if category else self.config.get_categories_in_system(sys)
            
            system_results = {
                'categories_processed': 0,
                'total_files': 0,
                'success': 0,
                'failed': 0,
                'skipped': 0,
                'by_category': {}
            }
            
            for cat in categories:
                self.logger.info(f"  Processing category: {cat}")
                
                # 确定输入输出目录（System/Category结构）
                cat_input_dir = os.path.join(self.config.input_dir, sys, cat)
                cat_output_dir = os.path.join(self.config.output_dir, sys, cat)
                
                if not os.path.exists(cat_input_dir):
                    self.logger.warning(f"Category directory not found: {cat_input_dir}")
                    continue
                
                # 处理该类别
                cat_results = self.process_directory(cat_input_dir, cat_output_dir)
                
                # 提取 JSON 处理结果
                json_results = cat_results.get('json_processing', cat_results)
                
                system_results['categories_processed'] += 1
                system_results['total_files'] += json_results.get('total', 0)
                system_results['success'] += json_results.get('success', 0)
                system_results['failed'] += json_results.get('failed', 0)
                system_results['skipped'] += json_results.get('skipped', 0)
                system_results['by_category'][cat] = cat_results
            
            all_results['systems_processed'] += 1
            all_results['categories_processed'] += system_results['categories_processed']
            all_results['total_files'] += system_results['total_files']
            all_results['success'] += system_results['success']
            all_results['failed'] += system_results['failed']
            all_results['skipped'] += system_results['skipped']
            all_results['by_system'][sys] = system_results
        
        return all_results
    
    def _save_json(self, survey_data: SurveyData, output_path: str):
        """
        保存SurveyData为JSON文件
        
        Args:
            survey_data: 综述数据对象
            output_path: 输出路径
        """
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(survey_data.to_dict(), f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Saved to: {output_path}")


# ==================== 命令行接口 ====================

def main():
    """命令行入口函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Survey Data Processing Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single file
  python data_processing_pipeline.py input.json -o output.json
  
  # Process directory
  python data_processing_pipeline.py input_dir --batch -o output_dir
  
  # Process by category
  python data_processing_pipeline.py --category Biology -o output_dir
  
  # Process all with custom config
  python data_processing_pipeline.py --batch --config config.json
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input JSON file or directory')
    parser.add_argument('-o', '--output', help='Output JSON file or directory')
    parser.add_argument('--batch', action='store_true', help='Batch process directory')
    parser.add_argument('--category', help='Process specific category')
    parser.add_argument('--system', help='Process specific system')
    parser.add_argument('--config', help='Path to config JSON file')
    parser.add_argument('--overwrite-original-json', action='store_true',
                       help='Overwrite existing original JSON files when converting from Markdown')
    
    # Processing options
    parser.add_argument('--no-normalize-outline', action='store_true',
                       help='Disable outline normalization')
    parser.add_argument('--no-normalize-content', action='store_true',
                       help='Disable content normalization')
    parser.add_argument('--no-normalize-refs', action='store_true',
                       help='Disable reference normalization')
    parser.add_argument('--no-quality-check', action='store_true',
                       help='Disable quality check')
    
    # Threshold options
    parser.add_argument('--min-section-words', type=int, default=5,
                       help='Minimum section word count (default: 5)')
    parser.add_argument('--min-outline-items', type=int, default=2,
                       help='Minimum outline items (default: 2)')
    parser.add_argument('--min-references', type=int, default=1,
                       help='Minimum references (default: 1)')
    
    args = parser.parse_args()
    
    # 加载或创建配置
    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
            config = DataProcessingConfig(**config_dict)
    else:
        config = DataProcessingConfig()
    
    # 应用命令行参数覆盖配置
    if args.no_normalize_outline:
        config.normalize_outline = False
    if args.no_normalize_content:
        config.normalize_content = False
    if args.no_normalize_refs:
        config.normalize_references = False
    if args.no_quality_check:
        config.enable_quality_check = False
    if args.overwrite_original_json:
        config.overwrite_original_json = True
    
    config.min_section_words = args.min_section_words
    config.min_outline_items = args.min_outline_items
    config.min_references = args.min_references
    
    if args.output:
        config.output_dir = args.output
    
    # 创建流水线
    pipeline = DataProcessingPipeline(config)
    
    # 执行处理
    try:
        if args.category or args.system:
            # 按类别处理（如果只指定system，会处理该system下的所有category）
            results = pipeline.process_by_category(
                category=args.category,
                system=args.system
            )
            print(f"\n{'='*60}")
            print(f"Category Processing Summary")
            print(f"{'='*60}")
            print(f"Categories processed: {results['categories_processed']}")
            print(f"Total files: {results['total_files']}")
            print(f"Success: {results['success']}")
            print(f"Failed: {results['failed']}")
            print(f"Skipped: {results['skipped']}")
            
        elif args.batch:
            # 批量处理
            if not args.input:
                args.input = config.input_dir
            
            results = pipeline.process_directory(args.input, args.output)
            print(f"\n{'='*60}")
            print(f"Batch Processing Summary")
            print(f"{'='*60}")
            
            # 从嵌套结构中提取 JSON 处理结果
            json_results = results.get('json_processing', {})
            print(f"Total files: {json_results.get('total', 0)}")
            print(f"Success: {json_results.get('success', 0)}")
            print(f"Failed: {json_results.get('failed', 0)}")
            print(f"Skipped: {json_results.get('skipped', 0)}")
            
            # 显示 Markdown 转换结果（如果有）
            md_results = results.get('markdown_conversion')
            if md_results:
                print(f"\nMarkdown Conversion:")
                print(f"Converted: {md_results.get('converted', 0)}")
                print(f"Skipped: {md_results.get('skipped', 0)}")
                print(f"Failed: {md_results.get('failed', 0)}")
            
        else:
            # 单文件处理
            if not args.input:
                parser.error("Input file is required for single file processing")
            
            survey_data = pipeline.process_single_file(args.input, args.output)
            
            print(f"\n{'='*60}")
            print(f"Processing Complete")
            print(f"{'='*60}")
            print(f"Source: {args.input}")
            if args.output:
                print(f"Output: {args.output}")
            
            stats = survey_data.get_statistics()
            print(f"\nStatistics:")
            print(f"  Outline items: {stats['outline_count']}")
            print(f"  Content sections: {stats['section_count']}")
            print(f"  References: {stats['reference_count']}")
            print(f"  Total words: {stats['total_words']}")
            
            if config.enable_quality_check and survey_data.metadata:
                qc = survey_data.metadata.get('quality_check', {})
                print(f"\nQuality Check: {'PASSED' if qc.get('passed') else 'FAILED'}")
                if not qc.get('passed'):
                    print("Issues:")
                    for issue in qc.get('issues', []):
                        print(f"  - {issue}")
        
        print(f"\n{'='*60}")
        print("Processing completed successfully!")
        
    except Exception as e:
        print(f"\n{'='*60}")
        print(f"ERROR: {e}")
        print(f"{'='*60}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()
