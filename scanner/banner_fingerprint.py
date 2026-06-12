import socket


FINGERPRINT_RESULTS = []


def banner_fingerprint(target):

    print("\n" + "=" * 50)
    print("LIPAS BANNER FINGERPRINTING")
    print("=" * 50 + "\n")

    ports = [
        21,
        22,
        25,
        80,
        110,
        143,
        443,
        3306,
        8080
    ]

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

            if port in [80, 443, 8080]:

                request = (
                    b"HEAD / HTTP/1.0\r\n\r\n"
                )

                sock.send(
                    request
                )

            banner = sock.recv(
                1024
            ).decode(
                errors="ignore"
            )

            if banner:

                result = (
                    f"[{port}] "
                    f"{banner[:100]}"
                )

                print(result)

                FINGERPRINT_RESULTS.append(
                    result
                )

            sock.close()

        except:

            pass
