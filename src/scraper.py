# src/scraper.py
import requests
from bs4 import BeautifulSoup
import config
from markdown_generator import convert_to_markdown

def fetch_and_convert(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content_md = convert_to_markdown(soup)
        with open(f"{config.OUTPUT_DIR}/{filename}.md", "w") as f:
            f.write(content_md)
    else:
        print(f"Failed to retrieve content from {url}")

def main():
    for section, url in config.SECTION_URLS.items():
        fetch_and_convert(url, section)

if __name__ == "__main__":
    main()
