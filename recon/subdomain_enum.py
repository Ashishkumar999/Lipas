import socket

from core.asset_manager import (
    add_subdomain
)

from core.target_manager import (
    get_target
)

from core.ui import (
    banner,
    success
)

FOUND_SUBDOMAINS = []


COMMON_SUBDOMAINS = [

    "www",

    "mail",

    "webmail",

    "ftp",

    "api",

    "dev",

    "test",

    "staging",

    "admin",

    "portal",

    "vpn",

    "blog",

    "m",

    "mobile",

    "shop"

]


def subdomain_enum():

    domain = get_target()

    if not domain:

        return

    banner(
        "LIPAS SUBDOMAIN ENUMERATION"
    )

    found = 0

    for sub in COMMON_SUBDOMAINS:

        target = (
            f"{sub}.{domain}"
        )

        try:

            ip = socket.gethostbyname(
                target
            )

            success(
                f"{target} -> {ip}"
            )

            FOUND_SUBDOMAINS.append(
                target
            )

            add_subdomain(
                domain,
                target
            )

            found += 1

        except:

            pass

    print()

    print(
        f"Total Found: {found}"
    )
