from fastapi import FastAPI, Query
from .retrieval import retrieve_relevant_docs, load_document
from .llm_handler import query_llm

app = FastAPI()

@app.get("/ask")
def ask(question: str = Query(...)):
    docs = retrieve_relevant_docs(question, top_n=2)

    contexts = [load_document(doc) for doc in docs]
    combined_context = "\n\n".join(contexts)

    response = query_llm(combined_context, question)
    return {"response": response}
