import streamlit as st
import requests

st.title("Enterprise AI Knowledge Assistant")

query = st.text_input("Ask a question")

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"query": query}
    )

    result = response.json()

    st.subheader("AI Response")

    st.write(result["answer"])