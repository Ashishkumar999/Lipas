from network.asset_discovery import (
    DISCOVERED_ASSETS
)


def network_dashboard():

    print("\n" + "=" * 60)
    print("LIPAS NETWORK DASHBOARD")
    print("=" * 60 + "\n")

    if not DISCOVERED_ASSETS:

        print(
            "No assets discovered."
        )

        return

    for asset in DISCOVERED_ASSETS:

        print(
            asset
        )

    print(
        f"\nTotal Assets: "
        f"{len(DISCOVERED_ASSETS)}"
    )
