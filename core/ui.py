from rich.console import Console
from rich.panel import Panel


console = Console()


def banner(title):

    console.print()

    console.print(

        Panel.fit(

            f"[bold cyan]{title}[/bold cyan]",

            border_style="bright_blue",

            padding=(1, 8)

        )

    )

    console.print()


def success(msg):

    console.print(
        f"[green][+] {msg}[/green]"
    )


def warning(msg):

    console.print(
        f"[yellow][!] {msg}[/yellow]"
    )


def error(msg):

    console.print(
        f"[red][-] {msg}[/red]"
    )


def info(msg):

    console.print(
        f"[cyan][*] {msg}[/cyan]"
    )
