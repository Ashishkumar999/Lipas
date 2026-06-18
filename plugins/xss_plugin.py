from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "XSS DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Check reflection points:"
    )

    print(
        "?q="
    )

    print(
        "?search="
    )

    print(
        "?message="
    )

    print(
        "?name="
    )
