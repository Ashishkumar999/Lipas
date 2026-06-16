from rich.console import (
    Console
)

from rich.panel import (
    Panel
)

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
        f"[green]Ports:[/green]"
    )

    console.print(
        asset["ports"]
    )

    console.print()

    console.print(
        f"[yellow]Services:[/yellow]"
    )

    console.print(
        asset["services"]
    )

    console.print()

    console.print(
        f"[red]Findings:[/red]"
    )

    console.print(
        asset["findings"]
    )
