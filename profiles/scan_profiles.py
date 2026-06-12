from scanner.port_scanner import (
    scan_ports
)

from scanner.security_headers import (
    security_headers_check
)

from scanner.service_detector import (
    detect_service
)

from scanner.banner_fingerprint import (
    banner_fingerprint
)


def quick_scan(target):

    print(
        "\nRunning Quick Scan...\n"
    )

    scan_ports(target)


def web_audit(target):

    print(
        "\nRunning Web Audit...\n"
    )

    security_headers_check(
        target
    )

    banner_fingerprint(
        target
    )


def full_assessment(target):

    print(
        "\nRunning Full Assessment...\n"
    )

    scan_ports(target)

    detect_service(target)

    security_headers_check(
        target
    )

    banner_fingerprint(
        target
    )
