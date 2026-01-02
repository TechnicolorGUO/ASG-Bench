import os
import re
import json


def split_markdown_content_and_refs(content: str) -> tuple:
    """
    Split markdown content into main content and reference block.
    
    Args:
        content: Full markdown content
        
    Returns:
        tuple: (main_content, reference_block)
    """
    # Common reference section patterns
    # Patterns now support optional numbering like "10. References" or "References"
    ref_patterns = [
        r'\n#+\s*(\d+\.?\s+)?References?\s*\n',
        r'\n#+\s*(\d+\.?\s+)?Bibliography\s*\n',
        r'\n#+\s*(\d+\.?\s+)?Works?\s+Cited\s*\n',
        r'\n#+\s*(\d+\.?\s+)?Literature\s+Cited\s*\n'
    ]
    
    for pattern in ref_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            split_pos = match.start()
            main_content = content[:split_pos]
            ref_block = content[split_pos:]
            return main_content, ref_block
    
    # No reference section found
    return content, ""


def parse_markdown_references(content: str) -> list:
    """
    Parse references from markdown content.
    
    Args:
        content: Markdown content string
        
    Returns:
        list: List of reference strings
    """
    _, ref_block = split_markdown_content_and_refs(content)
    
    if not ref_block:
        return []
    
    # Remove the reference header
    ref_block = re.sub(r'^#+\s*.*$', '', ref_block, count=1, flags=re.MULTILINE)
    
    # Remove "**Sources:**" section and everything after it (common in Gemini outputs)
    sources_match = re.search(r'\*\*Sources:\*\*', ref_block, re.IGNORECASE)
    if sources_match:
        ref_block = ref_block[:sources_match.start()]
    
    # Split by lines and filter empty lines
    references = [line.strip() for line in ref_block.split('\n') if line.strip()]
    
    # Try to parse numbered references
    numbered_refs = []
    for line in references:
        # Skip lines that are just URLs or markdown links without reference info
        if line.startswith('http') or re.match(r'^\d+\.\s*\[.*\]\(http', line):
            continue
        # Match patterns like "[1]", "1.", "[cite: 1]", etc.
        if re.match(r'^(\[?\d+[\]\.)\s]|\[cite:\s*\d+\])', line):
            numbered_refs.append(line)
    
    return numbered_refs if numbered_refs else references


def extract_outline(content: str) -> list:
    """
    Extract outline (headers) from markdown content.
    
    Args:
        content: Markdown content string
        
    Returns:
        list: List of [level, title] pairs
    """
    lines = content.split('\n')
    pattern_hash = r'^(#{1,6})\s+(.+)'
    hash_headers = []
    
    for i, line in enumerate(lines):
        match = re.match(pattern_hash, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            hash_headers.append((i, level, title))
    
    if not hash_headers:
        return []
    
    # Check if all headers are at the same level
    levels = {lvl for _, lvl, _ in hash_headers}
    single_level = (len(levels) == 1)
    
    outline = []
    if single_level:
        # Normalize to level 1 if all headers are at the same level
        for _, _, title in hash_headers:
            outline.append([1, title])
    else:
        for _, level, title in hash_headers:
            outline.append([level, title])
    
    return outline


def remove_headers(content: str) -> str:
    """
    Remove all markdown headers from content.
    
    Args:
        content: Markdown content string
        
    Returns:
        str: Content without headers
    """
    # Remove header lines
    content_no_headers = re.sub(r'^#+\s+.*$', '', content, flags=re.MULTILINE)
    # Merge multiple empty lines into one
    content_no_headers = re.sub(r'\n{2,}', '\n', content_no_headers)
    return content_no_headers.strip()


def split_content_by_headers(content: str, outline: list) -> list:
    """
    Split content by headers and associate each section with its heading.
    
    Args:
        content: Markdown content string
        outline: List of [level, title] pairs from extract_outline
        
    Returns:
        list: List of dicts with 'heading', 'level', and 'content' keys
    """
    if not outline:
        # No headers found, return all content as a single section
        return [{
            "heading": "",
            "level": 0,
            "content": content.strip()
        }]
    
    lines = content.split('\n')
    pattern_hash = r'^(#{1,6})\s+(.+)'
    
    # Find all header positions
    header_positions = []
    for i, line in enumerate(lines):
        match = re.match(pattern_hash, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            header_positions.append((i, level, title))
    
    # Build sections
    sections = []
    for idx, (line_num, level, title) in enumerate(header_positions):
        # Determine the end of this section
        if idx + 1 < len(header_positions):
            end_line = header_positions[idx + 1][0]
        else:
            end_line = len(lines)
        
        # Extract content for this section (excluding the header line itself)
        section_lines = lines[line_num + 1:end_line]
        section_content = '\n'.join(section_lines).strip()
        
        # Only add sections with content
        if section_content or idx == 0:  # Always include first section even if empty
            sections.append({
                "heading": title,
                "level": level,
                "content": section_content
            })
    
    return sections


def split_survey_into_parts(content: str) -> tuple:
    """
    Split markdown content into three parts: outline, content, and reference.
    
    Args:
        content: Markdown content string
        
    Returns:
        tuple: (outline, content_sections, references)
            - outline: list of [level, title] pairs
            - content_sections: list of dicts with heading, level, and content
            - references: list of reference strings
    """
    # Extract outline
    outline = extract_outline(content)
    
    # Split main content and references
    main_content, ref_block = split_markdown_content_and_refs(content)
    
    # Split content by headers
    content_sections = split_content_by_headers(main_content, outline)
    
    # Parse references
    references = parse_markdown_references(content)
    
    return outline, content_sections, references


class MarkdownToJsonConverter:
    """Convert markdown survey files to structured JSON format."""
    
    def __init__(self, markdown_path: str):
        """
        Initialize converter with markdown file path.
        
        Args:
            markdown_path: Path to the markdown file
        """
        self.markdown_path = markdown_path
        self.markdown_content = self._read_markdown()
        self.outline = []
        self.content = []  # Changed to list of dicts
        self.references = []
        
    def _read_markdown(self) -> str:
        """Read markdown file content."""
        with open(self.markdown_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse(self):
        """Parse markdown content into structured components."""
        self.outline, self.content, self.references = split_survey_into_parts(
            self.markdown_content
        )
        return self
    
    def to_dict(self) -> dict:
        """
        Convert parsed content to dictionary.
        
        Returns:
            dict: Structured data with outline, content, and references
        """
        return {
            "outline": self.outline,
            "content": self.content,
            "references": self.references
        }
    
    def save_json(self, output_path: str = None):
        """
        Save parsed content to JSON file.
        
        Args:
            output_path: Path to save JSON file. If None, saves to same directory
                        as markdown file with '_split.json' suffix
        """
        if output_path is None:
            # Generate output path based on markdown file path
            md_dir = os.path.dirname(self.markdown_path)
            md_basename = os.path.basename(self.markdown_path)
            json_filename = md_basename.replace('.md', '_split.json')
            output_path = os.path.join(md_dir, json_filename)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        # Save to JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
        
        print(f"[OK] JSON saved to: {output_path}")
        return output_path
    
    def get_outline_formatted(self) -> str:
        """Get formatted outline as a readable string."""
        formatted_lines = []
        for level, title in self.outline:
            indent = "  " * (level - 1)
            formatted_lines.append(f"{indent}{'#' * level} {title}")
        return "\n".join(formatted_lines)
    
    def get_content_plain_text(self) -> str:
        """Get all content as plain text without headers."""
        return "\n\n".join(section["content"] for section in self.content)
    
    def get_stats(self) -> dict:
        """Get statistics about the parsed content."""
        total_content_length = sum(len(section["content"]) for section in self.content)
        total_content_lines = sum(len(section["content"].split('\n')) for section in self.content)
        
        return {
            "outline_items": len(self.outline),
            "content_sections": len(self.content),
            "total_content_length": total_content_length,
            "total_content_lines": total_content_lines,
            "references_count": len(self.references)
        }


def convert_markdown_to_json(markdown_path: str, output_path: str = None) -> dict:
    """
    Convert a markdown file to JSON format.
    
    Args:
        markdown_path: Path to input markdown file
        output_path: Path to output JSON file (optional)
        
    Returns:
        dict: Parsed content as dictionary
    """
    converter = MarkdownToJsonConverter(markdown_path)
    converter.parse()
    converter.save_json(output_path)
    return converter.to_dict()


def batch_convert_directory(input_dir: str, output_dir: str = None):
    """
    Convert all markdown files in a directory to JSON.
    
    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save JSON files (optional, defaults to input_dir)
    """
    if output_dir is None:
        output_dir = input_dir
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all markdown files
    markdown_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    
    if not markdown_files:
        print(f"No markdown files found in {input_dir}")
        return
    
    print(f"Found {len(markdown_files)} markdown file(s)")
    print("=" * 80)
    
    results = []
    for md_file in markdown_files:
        print(f"\nProcessing: {md_file}")
        md_path = os.path.join(input_dir, md_file)
        
        # Generate output path
        json_filename = md_file.replace('.md', '_split.json')
        json_path = os.path.join(output_dir, json_filename)
        
        try:
            result = convert_markdown_to_json(md_path, json_path)
            
            # Show stats
            converter = MarkdownToJsonConverter(md_path)
            converter.parse()
            stats = converter.get_stats()
            print(f"  - Outline items: {stats['outline_items']}")
            print(f"  - Content sections: {stats['content_sections']}")
            print(f"  - Total content lines: {stats['total_content_lines']}")
            print(f"  - References: {stats['references_count']}")
            
            results.append({
                "file": md_file,
                "status": "success",
                "output": json_path
            })
        except Exception as e:
            print(f"[X] Error processing {md_file}: {e}")
            results.append({
                "file": md_file,
                "status": "error",
                "error": str(e)
            })
    
    print("\n" + "=" * 80)
    print(f"Conversion complete: {len(results)} file(s) processed")
    successful = sum(1 for r in results if r['status'] == 'success')
    print(f"[OK] Successful: {successful}")
    print(f"[X] Failed: {len(results) - successful}")


if __name__ == "__main__":
    import sys
    
    # Command line usage
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python markdown_to_json.py <markdown_file> [output_file]")
        print("  Directory:   python markdown_to_json.py <input_dir> --batch [output_dir]")
        print("\nExamples:")
        print("  python markdown_to_json.py survey.md")
        print("  python markdown_to_json.py survey.md output.json")
        print("  python markdown_to_json.py ./surveys --batch ./outputs")
        sys.exit(1)
    
    if "--batch" in sys.argv:
        # Batch conversion mode
        input_dir = sys.argv[1]
        output_dir = sys.argv[3] if len(sys.argv) > 3 else input_dir
        batch_convert_directory(input_dir, output_dir)
    else:
        # Single file conversion mode
        markdown_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        
        if not os.path.exists(markdown_path):
            print(f"Error: File not found: {markdown_path}")
            sys.exit(1)
        
        print(f"Converting: {markdown_path}")
        result = convert_markdown_to_json(markdown_path, output_path)
        
        # Show preview
        print("\n" + "=" * 80)
        print("Preview:")
        print("-" * 80)
        converter = MarkdownToJsonConverter(markdown_path)
        converter.parse()
        stats = converter.get_stats()
        print(f"Outline items: {stats['outline_items']}")
        print(f"Content sections: {stats['content_sections']}")
        print(f"Total content length: {stats['total_content_length']} characters")
        print(f"Total content lines: {stats['total_content_lines']}")
        print(f"References: {stats['references_count']}")
        print("=" * 80)

