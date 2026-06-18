from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_manager import load_assets
from database.finding_db import load_findings
from database.attack_path_db import load_attack_paths

console = Console()


def dashboard_v3():

    assets = load_assets()

    findings = load_findings()

    attack_paths = load_attack_paths()

    console.print()

    console.print(

        Panel.fit(

            "[bold cyan]LIPAS ENTERPRISE DASHBOARD V3[/bold cyan]",

            border_style="bright_blue"

        )

    )

    table = Table(

        title="Summary",

        border_style="bright_blue"

    )

    table.add_column(
        "Metric",
        style="cyan"
    )

    table.add_column(
        "Count",
        justify="center"
    )

    table.add_row(
        "Assets",
        str(
            len(assets)
        )
    )

    table.add_row(
        "Findings",
        str(
            len(findings)
        )
    )

    table.add_row(
        "Attack Paths",
        str(
            len(attack_paths)
        )
    )

    console.print(
        table
    )
