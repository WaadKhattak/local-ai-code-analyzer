# Local AI Static Code Review Engine

An open-source static application security and quality analysis harness powered by local open-weight LLMs (`qwen2.5-coder`).

## Features
- **100% Local & Private:** Runs inference locally on hardware (NVIDIA RTX GPU) via Ollama.
- **Auto Model Selection:** Dynamically detects and utilizes available local models.
- **Rich Terminal UI:** Displays source code with syntax highlighting alongside structured analysis reports.

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) running locally with `qwen2.5-coder`

## Usage
```bash
pip install rich requests
python3 src/main.py samples/demo.py

## 🚀 Future Roadmap
- **Optional Web/Desktop GUI:** Introduce a user-friendly interface using **Streamlit** or **Gradio** for visual inspection and file uploading.
- **CI/CD Integration:** GitHub Actions / GitLab CI pipeline integration for automated pull-request scanning.
- **Custom Rule Engine:** Allow security teams to define custom YAML/JSON rule templates for specific vulnerability patterns.
