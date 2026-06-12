import socket


def custom_port_scan(target):

    print("\nLIPAS CUSTOM PORT SCANNER\n")

    ports = input(
        "Enter Ports (80,443) or Range (1-1000): "
    )

    port_list = []

    if "-" in ports:

        start, end = ports.split("-")

        port_list = range(
            int(start),
            int(end) + 1
        )

    else:

        port_list = [
            int(x.strip())
            for x in ports.split(",")
        ]

    for port in port_list:

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

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
