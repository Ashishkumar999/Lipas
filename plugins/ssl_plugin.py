import ssl
import socket

from core.target_manager import (
    get_target
)

from core.findings_manager import (
    add_finding
)

from core.ui import (
    banner,
    success,
    warning
)


def run():

    target = get_target()

    if not target:

        warning(
            "No target selected"
        )

        return

    banner(
        "LIPAS SSL ANALYZER"
    )

    try:

        context = ssl.create_default_context()

        with socket.create_connection(

            (
                target,
                443
            ),

            timeout=10

        ) as sock:

            with context.wrap_socket(

                sock,

                server_hostname=target

            ) as ssock:

                cert = ssock.getpeercert()

                success(
                    "SSL Certificate Found"
                )

                print()

                print(
                    "Issuer:"
                )

                print(
                    cert.get(
                        "issuer"
                    )
                )

                print()

                print(
                    "Expires:"
                )

                print(
                    cert.get(
                        "notAfter"
                    )
                )

                cipher = (

                    ssock.cipher()

                )

                print()

                print(
                    "Cipher:"
                )

                print(
                    cipher
                )

    except Exception as e:

        warning(
            str(e)
        )

        add_finding(

            target,

            "SSL Issue",

            "MEDIUM 🟠",

            "A02",

            5.0,

            "SSL/TLS problem",

            "Review TLS configuration"

        )
