import socket
import time

from concurrent.futures import ThreadPoolExecutor


OPEN_PORTS = set()


def check_port(target, port):

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

            OPEN_PORTS.add(port)

        sock.close()

    except:

        pass


def threaded_port_scan(target):

    print("\nLIPAS THREADED PORT SCANNER\n")

    start = time.time()

    start_port = int(
        input("Start Port: ")
    )

    end_port = int(
        input("End Port: ")
    )

    with ThreadPoolExecutor(
        max_workers=100
    ) as executor:

        for port in range(
            start_port,
            end_port + 1
        ):

            executor.submit(
                check_port,
                target,
                port
            )

    print(
        f"\nOpen Ports Found: {len(OPEN_PORTS)}"
    )

    end = time.time()

    print(
       f"Scan Time: {round(end-start, 2)} seconds"
    )
