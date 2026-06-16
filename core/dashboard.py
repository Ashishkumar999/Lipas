from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_manager import (
    load_assets
)

console = Console()


def dashboard():

    assets = load_assets()

    total_assets = len(
        assets
    )

    total_ports = 0
    total_services = 0
    total_tech = 0
    total_findings = 0

    high = 0
    medium = 0
    low = 0

    for asset in assets:

        total_ports += len(
            asset["ports"]
        )

        total_services += len(
            asset["services"]
        )

        total_tech += len(
            asset["technologies"]
        )

        total_findings += len(
            asset["findings"]
        )

        risk = asset.get(
            "risk_score",
            0
        )

        if risk >= 70:

            high += 1

        elif risk >= 40:

            medium += 1

        else:

            low += 1

    console.print()

    console.print(

        Panel.fit(

            "[bold cyan]LIPAS ENTERPRISE DASHBOARD[/bold cyan]",

            border_style="bright_blue",

            padding=(1, 5)

        )

    )

    table = Table(

        show_header=True,

        header_style="bold white",

        border_style="bright_blue"

    )

    table.add_column(
        "Metric",
        style="cyan"
    )

    table.add_column(
        "Value",
        justify="center"
    )

    table.add_row(
        "Assets",
        str(total_assets)
    )

    table.add_row(
        "Ports",
        str(total_ports)
    )

    table.add_row(
        "Services",
        str(total_services)
    )

    table.add_row(
        "Technologies",
        str(total_tech)
    )

    table.add_row(
        "Findings",
        str(total_findings)
    )

    console.print(
        table
    )

    risk_table = Table(

        title="Risk Distribution",

        border_style="bright_blue"

    )

    risk_table.add_column(
        "Severity"
    )

    risk_table.add_column(
        "Count",
        justify="center"
    )

    risk_table.add_row(
        "🔴 High",
        str(high)
    )

    risk_table.add_row(
        "🟠 Medium",
        str(medium)
    )

    risk_table.add_row(
        "🟢 Low",
        str(low)
    )

    console.print()

    console.print(
        risk_table
    )
