import sys

from scanner.header_analyzer import analyze_headers
from scanner.port_scanner import scan_ports
from recon.dns_lookup import dns_lookup
from recon.ip_lookup import ip_lookup
from recon.reverse_dns import reverse_dns
from recon.whois_lookup import whois_lookup

from scanner.port_scanner import scan_ports


def banner():

    print("""
=========================================
              LIPAS v1.0
=========================================
Lightweight Intelligent Penetration
Assessment Suite
=========================================
""")


def main():

    banner()

    if len(sys.argv) != 3:

        print("Usage:")
        print("python lipas.py recon domain.com")
        print("python lipas.py ports domain.com")
        print("python lipas.py headers domain.com")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "recon":

        dns_lookup(target)

        whois_lookup(target)

        ip = ip_lookup(target)

        if ip:
            reverse_dns(ip)

    elif command == "ports":

        scan_ports(target)

    elif command == "headers":

       analyze_headers(target)

    else:

        print("Unknown command")


if __name__ == "__main__":
    main()
