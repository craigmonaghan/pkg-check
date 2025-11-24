import typer
from rich.console import Console
from rich.panel import Panel
from core.checkers.npm_checker import NPMChecker


app = typer.Typer()
console = Console()


@app.command()
def npm(package_name: str):
    