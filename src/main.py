import sys
import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# Host bridge configuration for Ollama API
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://192.168.117.1:11434")

def auto_select_model():
    """Detect available local models and select the optimal coding model."""
    if "MODEL_NAME" in os.environ:
        return os.environ["MODEL_NAME"]
    
    try:
        res = requests.get(f"{OLLAMA_BASE}/api/tags", timeout=5)
        if res.status_code == 200:
            models = res.json().get("models", [])
            if models:
                for m in models:
                    name = m.get("name", "")
                    if "qwen2.5-coder:7b" in name:
                        return name
                return models[0]["name"]
    except Exception:
        pass
    
    return "qwen2.5-coder:7b"

MODEL_NAME = auto_select_model()
OLLAMA_URL = f"{OLLAMA_BASE}/api/generate"

PROMPT_TEMPLATE = """
You are an expert static analysis code reviewer engine. 
Analyze the following source code for bugs, quality issues, efficiency bottlenecks, structural anti-patterns, and best practices.

Provide a clear, structured response containing:
1. Identified Issues & Structural Anti-patterns
2. Severity Assessment (Low, Medium, High, Critical)
3. Refactored Code Recommendations

Source Code to Analyze:
```{code}```
"""

def analyze_file(file_path):
    if not os.path.exists(file_path):
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    console.print(
        Panel(
            f"[bold cyan]Target File:[/bold cyan] {file_path}\n"
            f"[bold yellow]Selected Model:[/bold yellow] {MODEL_NAME}\n"
            f"[bold green]Endpoint:[/bold green] {OLLAMA_URL}",
            title="Local AI Code Analysis Engine",
            border_style="cyan"
        )
    )

    formatted_prompt = PROMPT_TEMPLATE.format(code=code_content)

    payload = {
        "model": MODEL_NAME,
        "prompt": formatted_prompt,
        "stream": False
    }

    try:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description=f"Running inference via local GPU ({MODEL_NAME})...", total=None)
            response = requests.post(OLLAMA_URL, json=payload, timeout=120)

        if response.status_code == 200:
            result = response.json().get("response", "")
            
            # Render syntax-highlighted source code
            syntax = Syntax(code_content, "python", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title="Source Code"))

            # Render AI analysis report
            console.print(Panel(result, title="[bold green]AI Analysis Report[/bold green]", border_style="green"))
        else:
            console.print(f"[bold red]API Error {response.status_code}:[/bold red] {response.text}")

    except Exception as e:
        console.print(f"[bold red]Connection Failed:[/bold red] {str(e)}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "samples/demo.py"
    analyze_file(target)
