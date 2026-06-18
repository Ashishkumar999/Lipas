from core.asset_manager import (
    get_asset
)

from core.target_manager import (
    get_target
)


def correlate():

    target = get_target()

    asset = get_asset(
        target
    )

    if not asset:

        print(
            "\nAsset not found"
        )

        return

    findings = asset.get(
        "findings",
        []
    )

    ports = asset.get(
        "ports",
        []
    )

    technologies = asset.get(
        "technologies",
        []
    )

    correlations = []

    if 22 in ports:

        correlations.append(

            "SSH Attack Surface"

        )

    if 80 in ports:

        if any(

            "Content Security Policy"

            in x

            for x in findings

        ):

            correlations.append(

                "Security Misconfiguration"

            )

    if any(

        "PHP"

        in x

        for x in technologies

    ):

        correlations.append(

            "PHP Attack Surface"

        )

    print()

    print(

        "Correlation Results"

    )

    print()

    if correlations:

        for item in correlations:

            print(

                "[+]",

                item

            )

    else:

        print(

            "No correlations"

        )
