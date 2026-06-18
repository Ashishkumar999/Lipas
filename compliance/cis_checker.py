from core.asset_manager import load_assets


def cis_checker():

    assets = load_assets()

    print()

    print(

        "CIS Baseline"

    )

    print()

    for asset in assets:

        print(

            asset.get(

                "target"

            ),

            "Checked"

        )
