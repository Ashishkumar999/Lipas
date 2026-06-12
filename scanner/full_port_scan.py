import socket


def full_port_scan(target):

    print(
        "\nScanning All Ports (1-65535)..."
    )

    for port in range(1, 65536):

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:

                print(
                    f"[OPEN] {port}"
                )

            sock.close()

        except:

            pass
