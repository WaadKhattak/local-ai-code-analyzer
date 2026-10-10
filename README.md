# 🛡️ Local AI Static Code Review Engine

A 100% private, offline Application Security Testing (SAST) engine designed for secure code reviews without data leaks. Powered locally by **Ollama** (`qwen2.5-coder:1.5b-instruct`) and presented via an interactive **Streamlit** web user interface.

## 🚀 Features
- **100% Offline & Private:** Runs entirely on local CPU/GPU with zero external API calls.
- **AI-Powered SAST:** Detects vulnerabilities like SQL Injection, Command Injection, and CWE flaws.
- **Dual Interface:** Accessible via a clean Streamlit Web UI or a command-line interface.

## 🛠️ Quickstart
1. Clone the repository and navigate into the folder.
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
