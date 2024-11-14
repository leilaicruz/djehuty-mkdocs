# src/markdown_generator.py
from markdownify import markdownify as md

def convert_to_markdown(soup):
    """Convert HTML content to Markdown format."""
    content_md = ""
    for element in soup.find_all(['h1', 'h2', 'p', 'ul', 'ol', 'code']):
        content_md += md(str(element)) + "\n\n"
    return content_md
