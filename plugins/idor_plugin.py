from core.ui import banner
from core.target_manager import get_target


def run():

    target = get_target()

    banner(
        "IDOR DISCOVERY"
    )

    print()

    print(
        f"Target : {target}"
    )

    print()

    print(
        "Interesting parameters:"
    )

    print(
        "?id="
    )

    print(
        "?user_id="
    )

    print(
        "?account="
    )

    print(
        "?profile="
    )
