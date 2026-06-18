from core.asset_manager import (
    get_asset
)

from core.target_manager import (
    get_target
)


def attack_surface():

    target = get_target()

    asset = get_asset(
        target
    )

    if not asset:

        return

    ports = len(
        asset.get(
            "ports",
            []
        )
    )

    subs = len(
        asset.get(
            "subdomains",
            []
        )
    )

    dirs = len(
        asset.get(
            "directories",
            []
        )
    )

    print()

    print(
        "Attack Surface Summary"
    )

    print()

    print(
        f"Ports      : {ports}"
    )

    print(
        f"Subdomains : {subs}"
    )

    print(
        f"Directories: {dirs}"
    )
