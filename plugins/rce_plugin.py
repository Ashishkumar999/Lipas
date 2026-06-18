from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "RCE DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Interesting parameters:"
    )

    print("?cmd=")
    print("?exec=")
    print("?ping=")
    print("?host=")
