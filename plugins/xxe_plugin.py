from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "XXE DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Interesting attack surfaces:"
    )

    print("SOAP")
    print("XML Upload")
    print("POST XML")
