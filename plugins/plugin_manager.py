from rich.console import Console

from core.logger import (
    error_log,
    activity_log
)

console = Console()

PLUGINS = []


def register_plugin(
    plugin
):

    if plugin not in PLUGINS:

        PLUGINS.append(
            plugin
        )


def run_plugins():

    console.print()

    console.print(
        "[bold cyan]Running Plugins[/bold cyan]"
    )

    console.print()

    for plugin in PLUGINS:

        try:

            activity_log(

                f"Running plugin: "

                f"{plugin.__name__}"

            )

            plugin()

        except Exception as e:

            error_log(

                f"{plugin.__name__}: {e}"

            )

            console.print(

                f"[red]Plugin Error: "

                f"{plugin.__name__}[/red]"

            )

            continue

    console.print()

    console.print(

        "[green]Plugin Execution Finished[/green]"

    )
