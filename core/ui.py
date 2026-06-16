from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def banner(title):

    console.print()

    console.print(

        Panel.fit(

            f"[bold cyan]{title}[/bold cyan]",

            border_style="bright_blue",

            padding=(1, 10)

        )

    )

    console.print()


def success(msg):

    console.print(
        f"[bold green][+] {msg}[/bold green]"
    )


def warning(msg):

    console.print(
        f"[bold yellow][!] {msg}[/bold yellow]"
    )


def error(msg):

    console.print(
        f"[bold red][-] {msg}[/bold red]"
    )


def info(msg):

    console.print(
        f"[bold cyan][*] {msg}[/bold cyan]"
    )


def section(title):

    console.print()

    console.print(
        f"[bold magenta]=== {title} ===[/bold magenta]"
    )

    console.print()
