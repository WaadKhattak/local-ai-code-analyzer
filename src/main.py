import json
import os
import sys
import requests
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

console = Console()

# Default to localhost for portability across all machines
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")
MODEL_NAME = "qwen2.5-coder:7b-instruct-q4_K_M"

PROMPT_TEMPLATE = """You are an expert security code reviewer.
Analyze the code below for security vulnerabilities, bugs and bad practices.
Each line of the code starts with its line number (like "3: code").

Reply with ONLY valid JSON in exactly this shape:
{
  "issues": [
    {
      "name": "short issue name",
      "cwe": "CWE-89",
      "severity": "HIGH or MEDIUM or LOW",
      "line": 12,
      "explanation": "1-2 simple sentences",
      "bad_code": "the vulnerable line, without the line number",
      "fixed_code": "the secure replacement code"
    }
  ]
}
If there are no problems, reply {"issues": []}.

CODE:
<<CODE>>
"""

def analyze_file(filepath):
    if not os.path.exists(filepath):
        console.print(f"[bold red]Error:[/bold red] File '{filepath}' not found.")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        code_content = f.read()

    console.print(Panel(f"Target File: {filepath}\nModel: {MODEL_NAME}\nEndpoint: {OLLAMA_BASE}", title="Local AI Code Analyzer", border_style="cyan"))
    syntax = Syntax(code_content, "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title="Source Code", border_style="blue"))

    # Line numbering for accurate AI vulnerability tagging
    numbered = "\n".join(f"{i}: {line}" for i, line in enumerate(code_content.splitlines(), start=1))
    formatted_prompt = PROMPT_TEMPLATE.replace("<<CODE>>", numbered)

    payload = {
        "model": MODEL_NAME,
        "prompt": formatted_prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1},
    }

    try:
        with console.status("[bold green]Analyzing code for security vulnerabilities..."):
            response = requests.post(f"{OLLAMA_BASE}/api/generate", json=payload, timeout=120)
            response.raise_for_status()
            raw_response = response.json().get("response", "{}")
            data = json.loads(raw_response)

        display_results(data)

    except Exception as e:
        console.print(f"[bold red]Analysis Failed:[/bold red] {e}")

def display_results(data):
    issues = data.get("issues", [])
    if not issues:
        console.print(Panel("[bold green]No security issues detected![/bold green]", title="Audit Summary", border_style="green"))
        return

    table = Table(title="Security Analysis Findings", show_header=True, header_style="bold magenta")
    table.add_column("Line", style="dim", width=6)
    table.add_column("Issue Name", style="bold")
    table.add_column("CWE", style="yellow")
    table.add_column("Severity", style="bold red")
    table.add_column("Explanation")

    for issue in issues:
        sev = issue.get("severity", "LOW")
        sev_color = "red" if sev == "HIGH" else "yellow" if sev == "MEDIUM" else "green"
        table.add_row(
            str(issue.get("line", "-")),
            issue.get("name", "Unknown"),
            issue.get("cwe", "N/A"),
            f"[{sev_color}]{sev}[/{sev_color}]",
            issue.get("explanation", "")
        )

    console.print(table)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "samples/demo.py"
    analyze_file(target)
