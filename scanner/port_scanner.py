OPEN_PORTS = []

import socket
import threading

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MYSQL",
    3389: "RDP",
    8080: "HTTP-ALT"
}


def check_port(host, port):

    try:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(1)

        result = sock.connect_ex(
            (host, port)
        )

        if result == 0:

            service = COMMON_PORTS.get(
                port,
                "UNKNOWN"
            )

            result = f"{port}/tcp OPEN - {service}"

            print(result)

            OPEN_PORTS.append(result)

        sock.close()

    except:
        pass


def scan_ports(host):

    print("\n" + "=" * 50)
    print("LIPAS PORT SCANNER")
    print("=" * 50 + "\n")

    threads = []

    for port in COMMON_PORTS:

        t = threading.Thread(
            target=check_port,
            args=(host, port)
        )

        t.start()

        threads.append(t)

    for t in threads:
        t.join()
