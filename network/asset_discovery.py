import socket

from network.network_profile import (
    NETWORK_PROFILE
)


DISCOVERED_ASSETS = []


def asset_discovery():

    print("\n" + "=" * 60)
    print("LIPAS NETWORK ASSET DISCOVERY")
    print("=" * 60 + "\n")

    target = input(
        "Enter IP or Domain: "
    ).strip()

    DISCOVERED_ASSETS.clear()

    for port in NETWORK_PROFILE:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(
                1
            )

            result = sock.connect_ex(
                (
                    target,
                    port
                )
            )

            if result == 0:

                service = NETWORK_PROFILE[
                    port
                ]

                item = (
                    f"{port} -> {service}"
                )

                DISCOVERED_ASSETS.append(
                    item
                )

                print(
                    f"[OPEN] {item}"
                )

            sock.close()

        except:

            pass

    print(
        f"\nAssets Found: "
        f"{len(DISCOVERED_ASSETS)}"
    )
