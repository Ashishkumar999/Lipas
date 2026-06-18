from core.asset_manager import load_assets


def risk_matrix():

    print()

    print("Risk Matrix")

    print()

    for asset in load_assets():

        score = asset.get(
            "risk_score",
            0
        )

        if score >= 90:

            risk = "CRITICAL 🔴"

        elif score >= 70:

            risk = "HIGH 🔴"

        elif score >= 40:

            risk = "MEDIUM 🟠"

        else:

            risk = "LOW 🟢"

        print(

            asset.get(
                "target"
            ),

            "->",

            risk

        )
