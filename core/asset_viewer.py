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

            border_style="bright_blue"

        )

    )

    if not assets:

        console.print(

            "[red]No Assets Found[/red]"

        )

        return

    table = Table(

        border_style="bright_blue"

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
        "Subs",
        justify="center",
        style="bright_blue"
    )

    table.add_column(
        "Dirs",
        justify="center",
        style="bright_green"
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

    table.add_column(
        "Last Scan"
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

            asset.get(
                "target",
                ""
            ),

            str(
                len(
                    asset.get(
                        "ports",
                        []
                    )
                )
            ),

            str(
                len(
                    asset.get(
                        "services",
                        []
                    )
                )
            ),

            str(
                len(
                    asset.get(
                        "technologies",
                        []
                    )
                )
            ),

            str(
                len(
                    asset.get(
                        "subdomains",
                        []
                    )
                )
            ),

            str(
                len(
                    asset.get(
                        "directories",
                        []
                    )
                )
            ),

            str(
                len(
                    asset.get(
                        "findings",
                        []
                    )
                )
            ),

            risk_display,

            asset.get(
                "last_scan",
                ""
            )

        )

    console.print(
        table
    )
