from core.asset_manager import (
    load_assets
)


def risk_matrix():

    assets = load_assets()

    print()

    print(
        "Risk Matrix"
    )

    print()

    for asset in assets:

        score = asset.get(
            "risk_score",
            0
        )

        if score >= 90:

            level = "CRITICAL 🔴"

        elif score >= 70:

            level = "HIGH 🔴"

        elif score >= 40:

            level = "MEDIUM 🟠"

        else:

            level = "LOW 🟢"

        print(

            asset["target"],

            "->",

            level

        )
