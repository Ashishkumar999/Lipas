from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "SSRF DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Look for:"
    )

    print(
        "?url="
    )

    print(
        "?redirect="
    )

    print(
        "?callback="
    )

    print(
        "?next="
    )
