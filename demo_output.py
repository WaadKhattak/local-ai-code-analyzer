from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Header Panel
console.print(Panel(
    "[bold cyan]Target File:[/bold cyan] samples/demo.py\n"
    "[bold cyan]Model:[/bold cyan] qwen2.5-coder:7b-instruct-q4_K_M (Offline Local LLM)\n"
    "[bold cyan]Endpoint:[/bold cyan] http://localhost:11434",
    title="[bold yellow]🛡️ Local AI Static Code Review Engine[/bold yellow]",
    expand=False
))

# Table setup
table = Table(title="[bold red]Vulnerability Audit Report[/bold red]", show_lines=True)

table.add_column("Line", style="bold white", justify="center")
table.add_column("Severity", justify="center")
table.add_column("CWE / CVE Standard", style="bold cyan")
table.add_column("Vulnerability Name", style="bold yellow")
table.add_column("Remediation / Explanation", style="white")

# Adding Findings
table.add_row(
    "7",
    "[bold white on red] HIGH [/bold white on red]",
    "CWE-89\n[dim](CVE-2023-XXXX class)[/dim]",
    "SQL Injection",
    "f-string concatenates raw user input into SQL query. Use parameterized queries: [green]`cursor.execute('SELECT... WHERE username=?', (user,))`[/green]"
)

table.add_row(
    "12",
    "[bold black on yellow] MEDIUM [/bold black on yellow]",
    "CWE-78\n[dim](CVE-2022-XXXX class)[/dim]",
    "OS Command Injection",
    "Unsanitized input passed directly to `os.system()`. Replace with `subprocess.run(['ping', command], shell=False)`."
)

console.print(table)
