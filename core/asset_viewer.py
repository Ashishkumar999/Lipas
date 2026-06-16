from rich.table import Table
from rich.console import Console
from rich.panel import Panel

from core.asset_manager import (
    load_assets
)

console = Console()


def asset_viewer():

    assets = load_assets()

    console.print()

    console.print(

        Panel.fit(

            "[bold cyan]LIPAS ENTERPRISE ASSET DATABASE[/bold cyan]",

            border_style="bright_blue"
        )

    )

    if not assets:

        console.print(
            "[red]No Assets Found[/red]"
        )

        return

    table = Table(

        show_header=True,

        header_style="bold white"

    )

    table.add_column(
        "Target",
        style="cyan"
    )

    table.add_column(
        "Ports",
        justify="center",
        style="green"
    )

    table.add_column(
        "Services",
        justify="center",
        style="yellow"
    )

    table.add_column(
        "Findings",
        justify="center",
        style="red"
    )

    for asset in assets:

        table.add_row(

            asset["target"],

            str(
                len(asset["ports"])
            ),

            str(
                len(asset["services"])
            ),

            str(
                len(asset["findings"])
            )
        )

    console.print(
        table
    )
