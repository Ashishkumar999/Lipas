import socket

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    add_port
)

from core.ui import (
    success,
    banner
)


from rich.console import Console
from rich.panel import Panel


OPEN_PORTS = []

console = Console()


def scan_ports():

    target = get_target()

    if not target:

        console.print(
            "[red]No target selected.[/red]"
        )

        return

    console.print()

    console.print(

        Panel.fit(

            "[bold cyan]LIPAS PORT SCANNER[/bold cyan]",

            border_style="bright_blue"

        )

    )

    console.print(
        f"[yellow]Target:[/yellow] {target}"
    )

    console.print()

    common_ports = [

        21,
        22,
        23,
        25,
        53,
        80,
        110,
        143,
        443,
        445,
        3306,
        3389

    ]

    for port in common_ports:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(
                1
            )

            result = sock.connect_ex(
                (
                    target,
                    port
                )
            )

            if result == 0:

                if port not in OPEN_PORTS:

                    OPEN_PORTS.append(
                        port
                    )

                success(
                    f"Port {port} Open"
                )

                add_port(
                    target,
                    port
                )

            sock.close()

        except Exception:

            pass
