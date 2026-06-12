import socket


SERVICE_RESULTS = []


COMMON_SERVICES = {

    21: "FTP",

    22: "OpenSSH",

    25: "SMTP",

    53: "DNS",

    80: "HTTP",

    110: "POP3",

    143: "IMAP",

    443: "HTTPS",

    3306: "MySQL",

    5432: "PostgreSQL",

    6379: "Redis",

    8080: "HTTP Alternate"
}


def detect_service(target):

    print("\n" + "=" * 50)
    print("LIPAS SERVICE DETECTOR")
    print("=" * 50 + "\n")

    ports = [
        21,
        22,
        25,
        53,
        80,
        110,
        143,
        443,
        3306,
        5432,
        6379,
        8080
    ]

    for port in ports:

        try:

            service = COMMON_SERVICES.get(
                port,
                "Unknown"
            )

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:

                output = (
                    f"[OPEN] {port} -> {service}"
                )

                print(output)

                SERVICE_RESULTS.append(
                    output
                )

            sock.close()

        except Exception:

            pass

    print("\nService Detection Completed.")
