import os
from transformers import pipeline

# Use Hugging Face pipeline (replace with your actual LLM if needed)
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "google/flan-t5-small")

llm_pipeline = pipeline("text2text-generation", model=LLM_MODEL_NAME)

MAX_CONTEXT_TOKENS = 512

def count_tokens(text: str) -> int:
    return len(text.split())

def query_llm(context: str, question: str) -> str:
    combined = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer:"
    token_count = count_tokens(combined)

    if token_count > MAX_CONTEXT_TOKENS:
        raise ValueError(f"Input too long ({token_count} tokens). Please refine the retrieval or shorten docs.")

    response = llm_pipeline(combined, max_length=200)[0]["generated_text"]
    return response.strip()
