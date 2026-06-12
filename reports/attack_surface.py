from scanner.port_scanner import OPEN_PORTS
from scanner.service_detector import SERVICE_RESULTS
from scanner.security_headers import HEADER_RESULTS
from reports.findings import FINDINGS


def attack_surface():

    print("\n" + "=" * 50)
    print("LIPAS ATTACK SURFACE MAP")
    print("=" * 50 + "\n")

    print("TARGET")
    print("│")

    print("├── Open Ports")

    if OPEN_PORTS:

        for port in OPEN_PORTS:

            print(
                f"│   ├── {port}"
            )

    else:

        print(
            "│   └── None"
        )

    print("│")

    print("├── Services")

    if SERVICE_RESULTS:

        for service in SERVICE_RESULTS:

            print(
                f"│   ├── {service}"
            )

    else:

        print(
            "│   └── None"
        )

    print("│")

    print("├── Security Headers")

    if HEADER_RESULTS:

        for header in HEADER_RESULTS:

            print(
                f"│   ├── {header}"
            )

    else:

        print(
            "│   └── None"
        )

    print("│")

    print("└── Findings")

    if FINDINGS:

        for finding in FINDINGS:

            print(
                f"    ├── "
                f"{finding['title']}"
            )

    else:

        print(
            "    └── None"
        )
