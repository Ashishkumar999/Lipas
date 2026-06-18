from core.asset_manager import (
    load_assets
)


def risk_assistant():

    print()

    print(

        "Risk Assistant"

    )

    print()

    assets = load_assets()

    for asset in assets:

        score = asset.get(

            "risk_score",

            0

        )

        print(

            asset.get(
                "target"
            ),

            "->",

            score

        )
