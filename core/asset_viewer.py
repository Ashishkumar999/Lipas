from rich.console import Console
from rich.table import Table
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

            border_style="bright_blue",

            padding=(1, 5)

        )

    )

    console.print()

    if not assets:

        console.print(
            "[bold red]No Assets Found[/bold red]"
        )

        return

    table = Table(

        show_header=True,

        header_style="bold white",

        border_style="bright_blue"

    )

    table.add_column(
        "Target",
        style="cyan",
        no_wrap=True
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
        justify="center"
    )

    for asset in assets:

        risk = asset.get(
            "risk_score",
            0
        )

        if risk >= 70:

            risk_display = (
                f"🔴 {risk}"
            )

        elif risk >= 40:

            risk_display = (
                f"🟠 {risk}"
            )

        else:

            risk_display = (
                f"🟢 {risk}"
            )

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

            risk_display

        )

    console.print(
        table
    )
