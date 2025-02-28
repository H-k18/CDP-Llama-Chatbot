from sentence_transformers import SentenceTransformer
import os
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_docs():
    embeddings = {}
    for filename in os.listdir("docs"):
        if filename.endswith(".txt"):
            with open(f"docs/{filename}", encoding="utf-8") as f:
                content = f.read()
                embeddings[filename] = model.encode(content).tolist()
    with open("embeddings.json", "w") as f:
        json.dump(embeddings, f)

if __name__ == "__main__":
    embed_docs()
