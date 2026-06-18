from core.ui import banner


def run():

    banner(
        "JWT ANALYZER"
    )

    print(
        "\nProvide JWT manually for analysis"
    )

    token = input(
        "JWT > "
    )

    if token.count(".") != 2:

        print(
            "Invalid JWT"
        )

        return

    print(
        "\nJWT Format Valid"
    )

    print(
        "Manual analysis phase"
    )
