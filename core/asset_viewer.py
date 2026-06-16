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

    console.print()

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
        "Tech",
        justify="center",
        style="magenta"
    )

    table.add_column(
        "Findings",
        justify="center",
        style="red"
    )

    table.add_column(
        "Risk",
        justify="center",
        style="bright_red"
    )

    for asset in assets:

        table.add_row(

            asset["target"],

            str(
                len(
                    asset["ports"]
                )
            ),

            str(
                len(
                    asset["services"]
                )
            ),

            str(
                len(
                    asset["technologies"]
                )
            ),

            str(
                len(
                    asset["findings"]
                )
            ),

            str(
                asset.get(
                    "risk_score",
                    0
                )
            )

        )

    console.print(
        table
    )
