from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "SQLI DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Look for parameters:"
    )

    print(
        "?id="
    )

    print(
        "?user="
    )

    print(
        "?search="
    )

    print(
        "?category="
    )
