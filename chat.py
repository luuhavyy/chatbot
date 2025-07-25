import os
import re
from dotenv import load_dotenv
from vertexai import init
from vertexai.preview.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel
from qdrant_client import QdrantClient
from qdrant_client.http.models import SearchRequest

load_dotenv()

# Load ENV
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")
GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_LOCATION = os.getenv("GCP_LOCATION")

# Init Vertex + Qdrant
init(project=GCP_PROJECT, location=GCP_LOCATION)
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
chat_model = GenerativeModel("gemini-2.0-flash-lite-001")
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# System prompt
SYSTEM_PROMPT = """
You are OptiBot, the customer-support bot for OptiSigns.com.
• Tone: helpful, factual, concise.
• Only answer using the uploaded docs.
• Max 5 bullet points; else link to the doc.
• Cite up to 3 "Article URL:" lines per reply.
"""

# Search context from Qdrant
def search_context(question, top_k=5):
    query_vec = embedding_model.get_embeddings([question])[0].values
    results = qdrant.search(
        collection_name=QDRANT_COLLECTION,
        query_vector=query_vec,
        limit=top_k
    )
    return results

# Build prompt with sources
def build_prompt(question, contexts):
    chunks = []
    for i, point in enumerate(contexts):
        url = point.payload.get("url", "")
        title = point.payload.get("title", "")
        text = point.payload.get("text", "").strip().replace("\n", " ")
        chunks.append(f"[{i+1}] {text} (Article URL: {url})")
    context_block = "\n\n".join(chunks)
    return f"{SYSTEM_PROMPT.strip()}\n\n{context_block}\n\nQuestion: {question}\nAnswer:"

# Replace [1], [2]... with actual URLs
def inject_urls(answer, contexts):
    for i, point in enumerate(contexts):
        url = point.payload.get("url", "")
        answer = re.sub(rf"\[{i+1}\]", url, answer)
    return answer

# CLI loop
def main():
    print("Hi, I’m OptiBot. Ask me anything about OptiSigns.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("Goodbye.")
            break

        results = search_context(question)
        if not results:
            print("OptiBot: Sorry, I couldn’t find anything relevant.")
            continue

        prompt = build_prompt(question, results)
        response = chat_model.generate_content(prompt)
        answer = inject_urls(response.text, results)
        print("\nOptiBot:", answer.strip())

if __name__ == "__main__":
    main()
