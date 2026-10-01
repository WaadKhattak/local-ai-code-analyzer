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
