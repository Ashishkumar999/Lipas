FOUND_SUBDOMAINS = []

import socket


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


def subdomain_enum(domain):

    print("\n" + "=" * 50)
    print("LIPAS SUBDOMAIN ENUMERATION")
    print("=" * 50 + "\n")

    found = []

    for sub in COMMON_SUBDOMAINS:

        target = f"{sub}.{domain}"

        try:

            ip = socket.gethostbyname(target)

            print(f"[+] {target} -> {ip}")

            found.append(target)

            FOUND_SUBDOMAINS.append(target)

        except:

            pass

    print(f"\nTotal Found: {len(found)}")
