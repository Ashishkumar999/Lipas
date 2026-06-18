from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "LFI DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Interesting parameters:"
    )

    print("?file=")
    print("?path=")
    print("?page=")
    print("?include=")
