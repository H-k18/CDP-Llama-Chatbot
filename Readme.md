# 🤖 CDP Support Chatbot

CDP Support Chatbot is a conversational assistant designed to help users find "how-to" information from the documentation of four major Customer Data Platforms (CDPs): **Segment, mParticle, Lytics, and Zeotap**. This chatbot leverages **web scraping, semantic search, and an LLM (Language Model)** to provide accurate answers directly from the official documentation.

---

## 📚 Overview

The chatbot works in the following steps:
1. **Scrape Documentation:** Text from official documentation pages is extracted and stored.
2. **Create Embeddings:** Text embeddings are generated using **`all-MiniLM-L6-v2`** from Sentence Transformers.
3. **Retrieve Relevant Documents:** When a question is asked, relevant documents are retrieved using **simple keyword matching**.
4. **Generate Answer:** The final answer is generated using **`google/flan-t5-small`** LLM.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```sh
git clone <repository-url>
cd CDP-Llama-Chatbot

----

# Create Virtual Environment

## For Windows

```sh
python -m venv .venv
source .venv/Scripts/activate

##Install Dependencies
pip install -r requirements.txt


##  Scrape Documentation
python app/scrape_docs.py

##  Generate Embeddings
python app/embed_docs.py

## Run Backend (FastAPI)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Run Frontend (Streamlit)

streamlit run streamlit_app.py

##  Usage Flow
Open the Streamlit app.
Type a question related to Segment, mParticle, Lytics, or Zeotap.
Press Ask.
The chatbot will:
Retrieve relevant sections from the documentation.
Feed them into the LLM along with your question.
Return a human-like response with the required information.

##Tech Stack 
Component         : Technology
Language Model    : Llama
Embedding Model   : all-MiniLM-L6-v2
Backend API       : FastAPI
Frontend UI       : Streamlit
Web Scraping      : BeautifulSoup
Doc Storage       : Plain Text Files
Search Logic      : Simple Keyword Matching

## requirements.txt 
streamlit
fastapi
uvicorn
requests
beautifulsoup4
transformers
sentence-transformers
torch

##License
This project is licensed under the MIT License.
##Contributing
Contributions are welcome!
Feel free to fork, modify, and create pull requests to improve this project.



