from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from core.target_manager import (
    get_target
)

from database.finding_db import (
    load_findings
)

console = Console()


def findings_viewer():

    target = get_target()

    if not target:

        console.print(

            "[red]No target selected[/red]"

        )

        return

    findings = load_findings()

    console.print()

    console.print(

        Panel.fit(

            "[bold red]LIPAS FINDINGS[/bold red]",

            border_style="red"

        )

    )

    table = Table(

        border_style="red"

    )

    table.add_column(
        "Severity"
    )

    table.add_column(
        "OWASP"
    )

    table.add_column(
        "CVSS"
    )

    table.add_column(
        "Title"
    )

    count = 0

    for finding in findings:

        if finding.get(
            "target"
        ) == target:

            table.add_row(

                finding.get(
                    "severity",
                    ""
                ),

                finding.get(
                    "owasp",
                    ""
                ),

                str(

                    finding.get(
                        "cvss",
                        ""
                    )

                ),

                finding.get(
                    "title",
                    ""
                )

            )

            count += 1

    if count == 0:

        table.add_row(

            "-",

            "-",

            "-",

            "No Findings"

        )

    console.print(
        table
    )
