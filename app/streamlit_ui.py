import streamlit as st
import requests

st.set_page_config(page_title="CDP Support Chatbot")
st.title("CDP Support Chatbot")

question = st.text_input("Ask a question about Segment, mParticle, Lytics, or Zeotap")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        try:
            response = requests.get("http://localhost:8000/ask", params={"question": question})
            if response.status_code == 200:
                st.write(response.json().get("response"))
            else:
                st.error(f"Failed to get response from backend. Status code: {response.status_code}")
        except requests.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
