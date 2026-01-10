import typer
from rich.console import Console
from rich.panel import Panel
from core.npm_checker import NPMChecker
from core.pypi_checker import PyPiChecker


app = typer.Typer()
console = Console()


@app.command()
def npm(package_name: str):
    console.print(f"🔍 Checking [cyan]{package_name}[/cyan] on NPM..")
    try:
        checker = NPMChecker()
        pkg =checker.check_package(package_name)
        
        output = f"""[bold cyan]NPM Package Info[/bold cyan]
        
        🔍 Name: {pkg.name}
        📦 Version: {pkg.version}
        👤 Maintainer(s): {pkg.maintainer}
        📅 Updated: {pkg.last_updated}
        """
        
        console.print(Panel(output, border_style="green"))
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

@app.command()
def pypi(package_name: str):
    console.print(f"🔍 Checking [cyan]{package_name}[/cyan] on PyPi..")
    try:
        checker = PyPiChecker()
        pkg =checker.check_package(package_name)
        
        output = f"""[bold cyan]PyPi Package Info[/bold cyan]
        
        🔍 Name: {pkg.name}
        📦 Version: {pkg.version}
        👤 Maintainer(s): {pkg.maintainer}
        📅 Updated: {pkg.last_updated}
        """
        
        console.print(Panel(output, border_style="green"))
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        
if __name__ == "__main__":
    app()
        
    
    
        