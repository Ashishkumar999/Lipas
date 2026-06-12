from scanner.port_scanner import scan_ports
from scanner.security_headers import security_headers_check
from scanner.ssl_inspector import ssl_inspector


def multi_target_scan():

    print("\nLIPAS MULTI TARGET MODE\n")

    try:

        with open(
            "targets.txt",
            "r"
        ) as file:

            targets = [
                line.strip()
                for line in file
                if line.strip()
            ]

        for target in targets:

            print(
                "\n" + "=" * 50
            )

            print(
                f"Scanning: {target}"
            )

            print(
                "=" * 50
            )

            try:

                scan_ports(target)

                security_headers_check(
                    target
                )

                ssl_inspector(target)

                print(
                    f"\n[✓] {target} completed"
                )

            except Exception as e:

                print(
                    f"[!] Error: {e}"
                )

    except FileNotFoundError:

        print(
            "targets.txt not found"
        )
