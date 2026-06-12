from scanner.port_scanner import OPEN_PORTS
from scanner.service_detector import SERVICE_RESULTS
from reports.findings import FINDINGS


ASSET_RESULTS = []


def asset_correlation():

    ASSET_RESULTS.clear()

    print("\n" + "=" * 50)
    print("LIPAS ASSET CORRELATION")
    print("=" * 50 + "\n")

    web_ports = []

    for port in OPEN_PORTS:

        port_str = str(port)

        if (
            "80" in port_str
            or "443" in port_str
            or "8080" in port_str
        ):

            web_ports.append(
                port
            )

    if web_ports:

        asset = {

            "name": "Web Server",

            "ports": web_ports,

            "services": SERVICE_RESULTS,

            "findings": [
                finding["title"]
                for finding in FINDINGS
            ]
        }

        ASSET_RESULTS.append(
            asset
        )

        print(
            "Asset Type : Web Server"
        )

        print(
            f"Open Ports : {len(web_ports)}"
        )

        print(
            f"Services   : {len(SERVICE_RESULTS)}"
        )

        print(
            f"Findings   : {len(FINDINGS)}"
        )

    else:

        print(
            "No web assets identified."
        )
