from reports.asset_correlation import (
    ASSET_RESULTS
)


def asset_inventory():

    print("\n" + "=" * 50)
    print("LIPAS ASSET INVENTORY")
    print("=" * 50 + "\n")

    if not ASSET_RESULTS:

        print(
            "No assets discovered."
        )

        return

    total = len(
        ASSET_RESULTS
    )

    print(
        f"Total Assets: {total}\n"
    )

    for i, asset in enumerate(
        ASSET_RESULTS,
        start=1
    ):

        print(
            f"Asset #{i}"
        )

        print(
            f"Type: "
            f"{asset['name']}"
        )

        print(
            f"Ports: "
            f"{len(asset['ports'])}"
        )

        print(
            f"Services: "
            f"{len(asset['services'])}"
        )

        print(
            f"Findings: "
            f"{len(asset['findings'])}"
        )

        print(
            "-" * 30
        )
