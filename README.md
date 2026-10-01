# Local AI Static Code Review Engine

An open-source static application security and quality analysis harness powered by local open-weight LLMs (`qwen2.5-coder`).

## 🌟 Features
- **100% Local & Private:** Runs inference locally via Ollama (`http://localhost:11434`).
- **Structured JSON Audits:** Outputs precise CWE codes, line numbers, severity levels, and refactored code fixes.
- **Rich Terminal UI:** Displays source code syntax highlighting alongside structured vulnerability tables.

## 📋 Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai/) running locally with `qwen2.5-coder` loaded.

## ⚙️ Usage
```bash
pip install rich requests
python3 src/main.py samples/demo.py
