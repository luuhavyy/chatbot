# Chatbot

A lightweight article ingestion pipeline and semantic search assistant.

## Overview

This project scrapes support articles from a Zendesk-based help center, converts them to Markdown, chunks the text, generates vector embeddings using Vertex AI, and stores the results in a Qdrant vector store. It is containerized via Docker and set to run daily as a scheduled job on a virtual machine.

## Project Structure

* `main.py` — Used in production to run daily. Handles fetching, hashing, updating local markdown files, and uploading text chunks as vector embeddings to Qdrant.
* `fetch_articles.py` — Scrapes structured article data from the help center API and converts it into markdown files. Used initially to populate the articles/ folder.
* `embed.py` — Processes markdown articles into overlapping chunks and generates vector embeddings using Vertex AI. Meant for first-time embedding.
* `chat.py` — Demo chatbot script that loads vector data and responds to user queries using a defined assistant prompt.
* `dockerfile` — Builds the app into a container. Used for scheduled runs on remote servers like DigitalOcean.
* `articles/` — Stores article markdown files organized by category.
* `logs/` — Contains timestamped logs of each run (e.g., 2025-07-25.txt).


## Run Locally

```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
cp .env.sample .env  # Fill in your keys

# Run locally
python main.py
```

## Docker Usage

Build and run:

```bash
docker build -t chatbot .
docker run --rm --env-file .env chatbot
```

## Scheduled Deployment

A Docker image was pushed to Docker Hub and scheduled on a cloud VM using `crontab`:

```cron
0 8 * * * docker run --rm luuhavyy/chatbot >> /root/chatbot.log 2>&1
```

## Log Example

```txt
Running daily update job...
Done.
New: 3, Updated: 2, Skipped: 28, Chunks: 125
```

## Secrets

* Environment variables defined in `.env.sample`
* Actual credentials excluded via `.gitignore`

## Embedding Strategy

* Token chunk size: 500 tokens
* Overlap: 100 tokens
* Model: `text-embedding-005` (Google Vertex AI)
* Each chunk stores title, URL, and raw text for semantic search use
