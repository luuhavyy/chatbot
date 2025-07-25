import os
import hashlib
import datetime
import uuid
from dotenv import load_dotenv
from fetch_articles import fetch_articles_by_structure, html_to_markdown, slugify
from embed import chunk_text
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from qdrant_client.http.exceptions import UnexpectedResponse
from google.cloud import aiplatform
from vertexai.language_models import TextEmbeddingModel

load_dotenv()

# ENV
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")
GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_LOCATION = os.getenv("GCP_LOCATION")

# Init
aiplatform.init(project=GCP_PROJECT, location=GCP_LOCATION)
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Ensure collection exists
try:
    client.get_collection(QDRANT_COLLECTION)
except UnexpectedResponse:
    client.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        optimizers_config={"default_segment_number": 1},
        timeout=300,
        shard_number=1,
    )

def compute_hash(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def save_markdown(title, body, category_name, article_id):
    folder = f"articles/{slugify(category_name)}"
    os.makedirs(folder, exist_ok=True)
    slug = slugify(title)
    article_url = f"https://support.optisigns.com/hc/en-us/articles/{article_id}-{slug}"
    content = f"Article URL: {article_url}\n\n# {title}\n\n{body}"
    return content, f"{folder}/{slug}.md"

def main():
    print("Running daily update job...")
    today = datetime.date.today()
    log = {
        "new": 0,
        "updated": 0,
        "skipped": 0,
        "chunks": 0
    }
    to_embed = []

    # Fetch full structured articles
    all_articles = fetch_articles_by_structure()  # returns { category: [articles] }

    for category, articles in all_articles.items():
        for a in articles:
            title = a["title"]
            html_body = a["body"]
            md_body = html_to_markdown(html_body)
            article_id = a["id"]

            content, filepath = save_markdown(title, md_body, category, article_id)
            new_hash = compute_hash(content)

            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    old = f.read()
                    old_hash = compute_hash(old)
                if old_hash == new_hash:
                    log["skipped"] += 1
                    continue
                else:
                    log["updated"] += 1
                    url = content.splitlines()[0].replace("Article URL: ", "").strip()
                    client.delete(
                        collection_name=QDRANT_COLLECTION,
                        filter=Filter(
                            must=[FieldCondition(key="url", match=MatchValue(value=url))]
                        )
                    )
            else:
                log["new"] += 1

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            to_embed.append((filepath, content))

    # Embed and upload
    for path, content in to_embed:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            url = lines[0].strip().replace("Article URL: ", "")
            title = ""
            for line in lines[1:4]:
                if line.startswith("# "):
                    title = line.strip("# ").strip()
                    break
            raw_content = "".join(lines[1:])
            chunks = chunk_text(raw_content, max_tokens=500, overlap=100)
            vectors = embedding_model.get_embeddings(chunks)
            log["chunks"] += len(chunks)

            points = []
            for i, vec in enumerate(vectors):
                points.append(
                    PointStruct(
                        id=str(uuid.uuid4()),
                        vector=vec.values,
                        payload={
                            "url": url,
                            "title": title,
                            "chunk_index": i,
                            "text": chunks[i]
                        }
                    )
                )
            client.upsert(collection_name=QDRANT_COLLECTION, points=points)

    # Save log
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/{today}.txt", "w") as f:
        for k, v in log.items():
            f.write(f"{k}: {v}\n")

    print("Done.")
    print(f"New: {log['new']}, Updated: {log['updated']}, Skipped: {log['skipped']}, Chunks: {log['chunks']}")

if __name__ == "__main__":
    main()
