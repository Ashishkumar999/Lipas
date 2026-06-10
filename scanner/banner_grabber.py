import socket


def banner_grab(target):

    print("\n" + "=" * 50)
    print("LIPAS BANNER GRABBER")
    print("=" * 50 + "\n")

    ports = [21, 22, 25, 80, 443]

    for port in ports:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(3)

            sock.connect(
                (target, port)
            )

            try:

                banner = sock.recv(
                    1024
                ).decode().strip()

                if banner:

                    print(
                        f"[{port}] {banner}"
                    )

            except:

                print(
                    f"[{port}] Connected"
                )

            sock.close()

        except:

            pass
