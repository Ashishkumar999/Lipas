from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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
            "[bold red]Asset Not Found[/bold red]"
        )

        return

    console.print()

    console.print(

        Panel.fit(

            f"[bold cyan]{target}[/bold cyan]",

            border_style="bright_blue",

            padding=(1, 5)

        )

    )

    console.print()

    risk = asset.get(
        "risk_score",
        0
    )

    if risk >= 70:

        risk_text = (
            "[bold red]CRITICAL[/bold red]"
        )

    elif risk >= 40:

        risk_text = (
            "[bold yellow]MEDIUM[/bold yellow]"
        )

    else:

        risk_text = (
            "[bold green]LOW[/bold green]"
        )

    summary = Table(

        show_header=True,

        header_style="bold white",

        border_style="bright_blue"

    )

    summary.add_column(
        "Category",
        style="cyan"
    )

    summary.add_column(
        "Count",
        justify="center"
    )

    summary.add_row(
        "Ports",
        str(
            len(
                asset["ports"]
            )
        )
    )

    summary.add_row(
        "Services",
        str(
            len(
                asset["services"]
            )
        )
    )

    summary.add_row(
        "Technologies",
        str(
            len(
                asset["technologies"]
            )
        )
    )

    summary.add_row(
        "Findings",
        str(
            len(
                asset["findings"]
            )
        )
    )

    summary.add_row(
        "Risk Score",
        str(risk)
    )

    console.print(
        summary
    )

    console.print()

    console.print(
        f"Risk Level: {risk_text}"
    )

    console.print()

    ports_table = Table(

        title="Open Ports",

        border_style="green"

    )

    ports_table.add_column(
        "Port",
        justify="center"
    )

    for port in asset["ports"]:

        ports_table.add_row(
            str(port)
        )

    console.print(
        ports_table
    )

    console.print()

    services_table = Table(

        title="Services",

        border_style="yellow"

    )

    services_table.add_column(
        "Service",
        justify="center"
    )

    for service in asset["services"]:

        services_table.add_row(
            service
        )

    console.print(
        services_table
    )

    console.print()

    tech_table = Table(

        title="Technologies",

        border_style="magenta"

    )

    tech_table.add_column(
        "Technology",
        justify="center"
    )

    for tech in asset["technologies"]:

        tech_table.add_row(
            tech
        )

    console.print(
        tech_table
    )

    console.print()

    findings_table = Table(

        title="Findings",

        border_style="red"

    )

    findings_table.add_column(
        "Finding"
    )

    if not asset["findings"]:

        findings_table.add_row(
            "No Findings"
        )

    else:

        for finding in asset["findings"]:

            findings_table.add_row(
                str(finding)
            )

    console.print(
        findings_table
    )
