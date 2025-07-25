import os
import re
import requests
import html2text

# Utility: Convert HTML content into clean Markdown
def html_to_markdown(html):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.bypass_tables = False
    return h.handle(html)

# Utility: Convert string to safe slug (for filenames and URLs)
def slugify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()

# Utility: Save markdown file into category folder and include real article URL and title
def save_article(title, body, category_name, article_id):
    folder_name = f"articles/{slugify(category_name)}"
    os.makedirs(folder_name, exist_ok=True)
    filename = f"{folder_name}/{slugify(title)}.md"

    slug = slugify(title)
    article_url = f"https://support.optisigns.com/hc/en-us/articles/{article_id}-{slug}"

    content = f"Article URL: {article_url}\n\n# {title}\n\n{body}"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Fetch articles using category > section > article structure
def fetch_articles_by_structure():
    base_url = "https://support.optisigns.com/api/v2/help_center/en-us"

    def get_json(url):
        res = requests.get(url)
        res.raise_for_status()
        return res.json()

    category_articles = {}

    categories = get_json(f"{base_url}/categories.json").get('categories', [])

    for category in categories:
        cat_id = category['id']
        cat_name = category['name']
        category_articles[cat_name] = []

        sections = get_json(f"{base_url}/categories/{cat_id}/sections.json").get('sections', [])

        for section in sections:
            sec_id = section['id']
            articles = get_json(f"{base_url}/sections/{sec_id}/articles.json").get('articles', [])

            for article in articles:
                category_articles[cat_name].append(article)

    return category_articles

# Run and print article count per category
if __name__ == "__main__":
    category_stats = fetch_articles_by_structure()
    print("\nArticle count by category:")
    for cat, count in category_stats.items():
        print(f"- {cat}: {count} articles")
