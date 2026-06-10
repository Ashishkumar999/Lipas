from recon.dns_lookup import dns_lookup
from recon.ip_lookup import ip_lookup
from recon.reverse_dns import reverse_dns
from recon.whois_lookup import whois_lookup

from scanner.port_scanner import scan_ports
from scanner.header_analyzer import analyze_headers


def banner():

    print("""
==================================================
                    LIPAS v1.0
==================================================

Lightweight Intelligent Penetration
Assessment Suite

==================================================
""")


def recon_scan(target):

    dns_lookup(target)

    whois_lookup(target)

    ip = ip_lookup(target)

    if ip:
        reverse_dns(ip)


def full_scan(target):

    print("\n[+] Starting Full Scan\n")

    recon_scan(target)

    scan_ports(target)

    analyze_headers(target)


def menu():

    banner()

    target = input("Enter Target Domain: ").strip()

    while True:

        print("\n========== MENU ==========")
        print("1. Reconnaissance")
        print("2. Port Scanner")
        print("3. Header Analysis")
        print("4. Full Scan")
        print("5. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":

            recon_scan(target)

        elif choice == "2":

            scan_ports(target)

        elif choice == "3":

            analyze_headers(target)

        elif choice == "4":

            full_scan(target)

        elif choice == "5":

            print("\nExiting LIPAS...")
            break

        else:

            print("\nInvalid Option")


if __name__ == "__main__":
    menu()
