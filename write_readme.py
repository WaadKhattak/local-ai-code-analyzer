content = """# 🛡️ Local AI Static Code Review Engine

An open-source, 100% offline static application security testing (SAST) tool powered by a local open-weight LLM (`qwen2.5-coder:7b-instruct-q4_K_M`) via Ollama.

---

## 🎬 Project Demo

[![Watch the Demo Video](https://img.youtube.com/vi/_iTRRWey6pM/maxresdefault.jpg)](https://youtu.be/_iTRRWey6pM)

> 👆 **Click the thumbnail above to watch the full walkthrough on YouTube.**

---

## 🎯 Key Features

- **100% Offline & Private:** Code never leaves your local environment; all LLM inference runs locally via Ollama.
- **Deterministic Prompting:** Enforces strict JSON output schemas to eliminate conversational fluff and hallucinations.
- **Vulnerability Mapping:** Automatically assigns **CWE IDs** (e.g., CWE-89, CWE-78) and severity levels (**HIGH**, **MEDIUM**, **LOW**).
- **Rich Terminal UI:** Displays clear line-numbered source code alongside structured security report tables.
- **Portability:** Defaults to standard `http://localhost:11434` with support for environment overrides via `OLLAMA_BASE`.

---

## ⚙️ How It Works (Step-by-Step Architecture)

The analyzer processes source code through a deterministic local pipeline to ensure data privacy and consistent structured output:
