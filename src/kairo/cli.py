import typer
from rich.console import Console
from .core import KairoBot
from .retriever import KairoRetriever
from .utils import print_logo

app = typer.Typer()
console = Console()

@app.command()
def chat(model: str = "gpt-3.5-turbo"):
    """Start chatting with Kairo"""
    kairo = KairoBot(model=model)
    print_logo(console)
    console.print("[bold cyan]Kairo is ready! Type 'exit' to quit.[/bold cyan]")

    while True:
        user_input = console.input("[green]You:[/green] ")
        if user_input.lower() in ["exit", "quit"]:
            console.print("[red]Goodbye from Kairo![/red]")
            break

        reply = kairo.ask(user_input)
        console.print(f"[blue]Kairo:[/blue] {reply}")

@app.command()
def load(file: str):
    """Load documents (PDF or TXT) into Kairo's knowledge base"""
    retriever = KairoRetriever()
    retriever.load_docs(file)
    console.print(f"[bold yellow]Document {file} loaded into Kairo's knowledge base![/bold yellow]")
