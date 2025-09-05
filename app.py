import streamlit as st
import requests

st.title("ECE AI Research Assistant 🤖")

# User query input
query = st.text_area("Ask me anything about ECE + AI:")

if st.button("Generate Answer"):
    if query.strip():
        # Call Ollama locally
        response = requests.post("http://localhost:11434/api/generate",
                                 json={"model": "llama3:latest", "prompt": query},
                                 stream=False)
        
        if response.status_code == 200:
            data = response.json()
            st.write(data["response"])
        else:
            st.error("Error: Could not connect to Ollama. Make sure it's running.")
