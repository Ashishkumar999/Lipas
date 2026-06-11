import socket

from config.settings import (
    COMMON_PORTS,
    DEFAULT_TIMEOUT
)

OPEN_PORTS = []


def scan_ports(target):

    print("\n" + "=" * 50)
    print("LIPAS PORT SCANNER")
    print("=" * 50 + "\n")

    ports = COMMON_PORTS

    for port in ports:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(
                DEFAULT_TIMEOUT
            )

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:

                try:

                    service = socket.getservbyport(
                        port
                    )

                except:

                    service = "unknown"

                output = (
                    f"{port}/tcp OPEN - "
                    f"{service}"
                )

                print(output)

                OPEN_PORTS.append(
                    output
                )

            sock.close()

        except Exception:

            pass

    print("\nScan Completed.")
