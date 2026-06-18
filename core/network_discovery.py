from core.ui import banner

from scanner.port_scanner import (
    scan_ports
)

from scanner.service_detector import (
    detect_service
)

from scanner.banner_grabber import (
    banner_grab
)


def network_discovery():

    while True:

        banner(
            "LIPAS NETWORK DISCOVERY"
        )

        print(
            "1. Quick Port Scan"
        )

        print(
            "2. Service Detection"
        )

        print(
            "3. Banner Analysis"
        )

        print(
            "4. Return"
        )

        print()

        choice = input(
            "Select Option: "
        )

        if choice == "1":

            scan_ports()

        elif choice == "2":

            detect_service()

        elif choice == "3":

            banner_grab()

        elif choice == "4":

            break

        else:

            print(
                "\nInvalid Option\n"
            )
