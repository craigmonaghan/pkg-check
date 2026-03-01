import typer
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from core.npm_checker import NPMChecker
from core.pypi_checker import PyPiChecker
from core.aur_checker import AURChecker
from parsers.exporter import export


app = typer.Typer()
console = Console()


@app.command()
def npm(package_name: str):
    console.print(f"Checking [cyan]{package_name}[/cyan] on NPM..")
    try:
        checker = NPMChecker()
        pkg = checker.check_package(package_name)
        output = f"""[bold cyan]NPM Package Info[/bold cyan]
        
        Name: {pkg.name}
        Version: {pkg.version}
        Maintainer(s): {pkg.maintainer}
        Updated: {pkg.updated_display()}
        URL: {pkg.url}
        """
        
        console.print(Panel(output, border_style="green"))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def pypi(package_name: str):
    console.print(f"Checking [cyan]{package_name}[/cyan] on PyPi..")
    try:
        checker = PyPiChecker()
        pkg = checker.check_package(package_name)        
        output = f"""[bold cyan]PyPi Package Info[/bold cyan]
        
        Name: {pkg.name}
        Version: {pkg.version}
        Maintainer(s): {pkg.maintainer}
        Updated: {pkg.updated_display()}
        URL: {pkg.url}
        """
        
        console.print(Panel(output, border_style="green"))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        
@app.command()
def aur(package_name: str):
    console.print(f"Checking [cyan]{package_name}[/cyan] on the AUR..")
    try:
        checker = AURChecker()
        pkg = checker.check_package(package_name)        
        output = f"""[bold cyan]AUR Package Info[/bold cyan]
        
        Name: {pkg.name}
        Version: {pkg.version}
        Maintainer(s): {pkg.maintainer}
        Updated: {pkg.updated_display()}
        URL: {pkg.url}
        """
        
        console.print(Panel(output, border_style="green"))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


@app.command()
def fetch(checker, package_name: str, output_file: Optional[str] = None):
    console.print(f"writing response for [cyan]{package_name}[/cyan]")
    try:
        if checker == "pypi": 
            checker = PyPiChecker 
        elif checker == "npm":
            checker = NPMChecker
        else:
            checker = AURChecker
            
        if output_file is None:
            output_file = f"response_{package_name}.json"
        output = export(checker, package_name, output_file)
        console.print(f"[green] Exported to {output_file}[/green]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


if __name__ == "__main__":
    app()