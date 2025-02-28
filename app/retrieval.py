import json
import os
from typing import List

EMBEDDINGS_FILE = os.path.join(os.path.dirname(__file__), "embeddings.json")
DOCS_FOLDER = os.path.join(os.path.dirname(__file__), "docs")

def load_embeddings() -> List[str]:
    """Load document names from the embeddings file."""
    with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:
        docs = json.load(f)  # embeddings.json should be like: ["doc1.txt", "doc2.txt", "doc3.txt"]
    return docs

def retrieve_relevant_docs(query: str, top_n=2) -> List[str]:
    """Retrieve the most relevant documents based on simple keyword matching."""
    docs = load_embeddings()

    query_lower = query.lower()
    doc_scores = []

    for doc in docs:
        score = sum(1 for word in query_lower.split() if word in doc.lower())
        doc_scores.append((doc, score))

    # Sort by score (descending) and take top_n docs
    top_docs = [doc for doc, _ in sorted(doc_scores, key=lambda x: x[1], reverse=True)[:top_n]]
    return top_docs

def load_document(doc_name: str, max_length=1000) -> str:
    """Load doc content and truncate if too long."""
    doc_path = os.path.join(DOCS_FOLDER, doc_name)
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content) > max_length:
        content = content[:max_length] + "\n...[truncated]..."

    return content
