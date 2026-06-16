from rich.console import Console
from rich.panel import Panel

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    get_asset
)

console = Console()


def asset_details():

    target = get_target()

    asset = get_asset(
        target
    )

    if not asset:

        console.print(
            "[red]Asset Not Found[/red]"
        )

        return

    console.print()

    console.print(

        Panel.fit(

            f"[bold cyan]{target}[/bold cyan]",

            border_style="bright_blue"

        )

    )

    console.print()

    console.print(
        "[green]OPEN PORTS[/green]"
    )

    print(
        "-" * 30
    )

    for port in asset["ports"]:

        console.print(
            f"[green]{port}[/green]"
        )

    console.print()

    console.print(
        "[yellow]SERVICES[/yellow]"
    )

    print(
        "-" * 30
    )

    for service in asset["services"]:

        console.print(
            f"[yellow]{service}[/yellow]"
        )

    console.print()

    console.print(
        "[cyan]TECHNOLOGIES[/cyan]"
    )

    print(
        "-" * 30
    )

    for tech in asset["technologies"]:

        console.print(
            f"[cyan]{tech}[/cyan]"
        )

    console.print()

    console.print(
        "[red]FINDINGS[/red]"
    )

    print(
        "-" * 30
    )

    for finding in asset["findings"]:

        console.print(
            finding
        )
