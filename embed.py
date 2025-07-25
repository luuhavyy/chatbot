import os
import glob
import uuid
from tqdm import tqdm
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from google.cloud import aiplatform
from vertexai.language_models import TextEmbeddingModel

# Load .env
load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")
GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_LOCATION = os.getenv("GCP_LOCATION")

# Init Gemini embedding model
aiplatform.init(project=GCP_PROJECT, location=GCP_LOCATION)
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")

# Init Qdrant
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Create collection
client.recreate_collection(
    collection_name=QDRANT_COLLECTION,
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE
    )
)

# Chunking strategy
def chunk_text(text, max_tokens=500, overlap=100):
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        window = words[start:start + max_tokens]
        chunk = " ".join(window)
        chunks.append(chunk)
        start += max_tokens - overlap

    return chunks

# Load markdown files and skip "Article URL" line
def load_markdown_files():
    paths = glob.glob("articles/**/*.md", recursive=True)
    data = []

    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines or not lines[0].startswith("Article URL:"):
                continue
            url = lines[0].strip().replace("Article URL: ", "")
            title = ""
            for line in lines[1:4]:  # Try to find first H1
                if line.startswith("# "):
                    title = line.strip("# ").strip()
                    break
            content = "".join(lines[1:])  # Remove Article URL line
            data.append((path, url, title, content))
    return data

# Embed and upload
def embed_and_upload():
    files = load_markdown_files()
    total_chunks = 0

    for path, url, title, content in tqdm(files, desc="Embedding & Uploading"):
        chunks = chunk_text(content)
        vectors = embedding_model.get_embeddings(chunks)
        qdrant_points = []

        for i, vec in enumerate(vectors):
            qdrant_points.append(
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

        client.upsert(
            collection_name=QDRANT_COLLECTION,
            points=qdrant_points
        )
        total_chunks += len(chunks)

    print(f"\nUploaded {len(files)} files with {total_chunks} chunks to Qdrant.")

if __name__ == "__main__":
    embed_and_upload()
