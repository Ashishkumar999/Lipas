import socket

from core.target_manager import (
    get_target
)

from core.ui import (
    banner,
    success,
    warning
)


def banner_grab():

    target = get_target()

    if not target:

        warning(
            "No Target Selected"
        )

        return

    banner(
        "LIPAS BANNER ANALYZER"
    )

    common_ports = [

        21,
        22,
        25,
        80,
        110,
        143,
        443

    ]

    found = False

    for port in common_ports:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(3)

            sock.connect(
                (
                    target,
                    port
                )
            )

            banner_data = sock.recv(
                1024
            )

            success(
                f"Port {port}"
            )

            print(
                banner_data.decode(
                    errors="ignore"
                )
            )

            found = True

            sock.close()

        except:

            pass

    if not found:

        warning(
            "No Banner Information Found"
        )
