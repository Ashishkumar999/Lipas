from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "SSTI DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Interesting parameters:"
    )

    print("?name=")
    print("?template=")
    print("?view=")
    print("?message=")
