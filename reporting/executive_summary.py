from core.asset_manager import (
    load_assets
)


def executive_summary():

    assets = load_assets()

    print()

    print(

        "LIPAS EXECUTIVE SUMMARY"

    )

    print()

    print(

        "Assets :",

        len(
            assets
        )

    )

    findings = 0

    for asset in assets:

        findings += len(

            asset.get(
                "findings",
                []
            )

        )

    print(

        "Findings :",

        findings

    )
