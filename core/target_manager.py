from core.asset_manager import (
    create_asset
)

TARGET_FILE = (
    "config/current_target.txt"
)


def set_target(
    target
):

    create_asset(
        target
    )

    with open(

        TARGET_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(
            target
        )


def get_target():

    try:

        with open(

            TARGET_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            target = (

                file.read()

                .strip()

            )

            if target:

                return target

            return None

    except:

        return None


def clear_target():

    with open(

        TARGET_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(
            ""
        )


def show_target():

    target = get_target()

    print(

        f"\nCurrent Target: "

        f"{target}"

    )
