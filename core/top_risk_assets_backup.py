from core.asset_manager import (
    load_assets
)


def top_risk_assets():

    assets = sorted(

        load_assets(),

        key=lambda x:

        x.get(
            "risk_score",
            0
        ),

        reverse=True

    )

    print()

    print(

        "Top Risk Assets"

    )

    print()

    for asset in assets[:5]:

        print(

            asset.get(
                "target"
            ),

            "-",

            asset.get(
                "risk_score",
                0
            )

        )
