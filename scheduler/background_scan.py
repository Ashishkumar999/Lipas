from core.target_manager import (
    get_target
)

from scanner.port_scanner import (
    scan_ports
)

from scanner.tech_detector import (
    detect_technology
)


def background_scan():

    target = get_target()

    if not target:

        print(
            "No Target Selected"
        )

        return

    print()

    print(
        "Starting Background Scan"
    )

    print()

    scan_ports()

    detect_technology()

    print()

    print(
        "Background Scan Completed"
    )
