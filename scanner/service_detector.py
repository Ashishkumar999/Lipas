import socket

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    add_service
)

from core.ui import (
    banner,
    success
)

SERVICE_RESULTS = []


def detect_service():

    target = get_target()

    if not target:

        return

    banner(
        "LIPAS SERVICE DETECTOR"
    )

    services = {

        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP"

    }

    for port, service in services.items():

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex(
                (
                    target,
                    port
                )
            )

            if result == 0:

                if service not in SERVICE_RESULTS:

                    SERVICE_RESULTS.append(
                        service
                    )

                success(
                    f"{service} Detected on Port {port}"
                )

                add_service(
                    target,
                    service
                )

            sock.close()

        except Exception:

            pass
