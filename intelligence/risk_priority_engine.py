from core.asset_manager import (
    get_asset
)

from core.target_manager import (
    get_target
)


def risk_priority():

    target = get_target()

    asset = get_asset(
        target
    )

    if not asset:

        return

    score = asset.get(

        "risk_score",

        0

    )

    print()

    print(

        "Risk Priority"

    )

    print()

    if score >= 90:

        print(

            "CRITICAL 🔴"

        )

    elif score >= 70:

        print(

            "HIGH 🔴"

        )

    elif score >= 40:

        print(

            "MEDIUM 🟠"

        )

    else:

        print(

            "LOW 🟢"

        )
