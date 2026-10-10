import streamlit as st
import requests

st.set_page_config(page_title="Local AI Code Reviewer", page_icon="🛡️", layout="wide")

st.title("🛡️ Local AI Static Code Review Engine")
st.caption("100% Offline Application Security Testing via Ollama")

with st.sidebar:
    st.header("Engine Configuration")
    model_name = st.text_input("Model", value="qwen2.5-coder:1.5b-instruct")
    ollama_url = st.text_input("Ollama Endpoint", value="http://localhost:11434/api/generate")

code_input = st.text_area("Paste Source Code for Analysis:", height=250, value='''import sqlite3
import os

def login(user_input_username, user_input_password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input_username}' AND password = '{user_input_password}'"
    cursor.execute(query)
    return cursor.fetchone()

def execute_command(command):
    os.system("ping " + command)
''')

if st.button("🔍 Run Security Audit", type="primary"):
    if not code_input.strip():
        st.warning("Please provide source code to analyze.")
    else:
        lines = code_input.splitlines()
        indexed_code = "\n".join([f"{idx+1}: {line}" for idx, line in enumerate(lines)])

        prompt = f"""You are an expert SAST security engine. Analyze the following code for CWE vulnerabilities.
Respond strictly in JSON format as an array of objects with keys: "line_number", "cwe_id", "issue_name", "severity", "explanation".

Code:
{indexed_code}
"""

        payload = {
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 512}
        }

        with st.spinner("Analyzing code on local CPU model..."):
            try:
                response = requests.post(ollama_url, json=payload, timeout=60)
                if response.status_code == 200:
                    result_json = response.json().get("response", "{}")
                    st.subheader("Audit Results")
                    st.code(result_json, language="json")
                else:
                    st.error(f"Error from Ollama API: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to Ollama: {str(e)}")
