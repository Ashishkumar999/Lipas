from recon.dns_lookup import dns_lookup
from recon.ip_lookup import ip_lookup
from recon.reverse_dns import reverse_dns
from recon.whois_lookup import whois_lookup
from recon.subdomain_enum import subdomain_enum

from scanner.port_scanner import scan_ports
from scanner.header_analyzer import analyze_headers
from scanner.tech_detector import detect_technology
from scanner.banner_grabber import banner_grab
from scanner.http_checker import http_checker
from scanner.dir_discovery import dir_discovery
from scanner.screenshot import take_screenshot
from scanner.ssl_inspector import ssl_inspector
from scanner.dns_security import dns_security_check
from scanner.security_headers import security_headers_check
from scanner.security_score import security_score
from scanner.custom_port_scan import custom_port_scan
from scanner.full_port_scan import full_port_scan
from scanner.threaded_port_scan import threaded_port_scan
from scanner.service_detector import detect_service

from reports.report_generator import generate_report
from reports.html_report import generate_html_report

from config.version import VERSION


def banner():

   print(f"""
==================================================
                LIPAS v{VERSION}
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

    print("\n[+] Starting Full Scan")

    print("[+] Report will be generated automatically\n")

    recon_scan(target)

    scan_ports(target)

    analyze_headers(target)

    detect_technology(target)

    subdomain_enum(target)

    generate_report(target)

def menu():

    banner()

    target = input("Enter Target Domain: ").strip()

    while True:

        print("\n========== MENU ==========")
        print("1. Reconnaissance")
        print("2. Port Scanner")
        print("3. Header Analysis")
        print("4. Full Scan")
        print("5. Technology Detection")
        print("6. Generate Report")
        print("7. Subdomain Enumeration")
        print("8. Banner Grabbing")
        print("9. HTTP Status Checker")
        print("10. Directory Discovery")
        print("11. Export HTML Report")
        print("12. Website Screenshot")
        print("13. SSL Inspector")
        print("14. DNS Security Check")
        print("15. Security Headers Audit")
        print("16. Security Scorecard")
        print("17. Custom Port Scan")
        print("18. Full Port Scan")
        print("19. Fast Port Scanner")
        print("20. Service Detection")
        print("0. Exit")

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

            detect_technology(target)

        elif choice == "6":

            generate_report(target)

        elif choice == "7":

            subdomain_enum(target)

        elif choice == "8":

            banner_grab(target)

        elif choice == "9":

            http_checker(target)

        elif choice == "10":

            dir_discovery(target)

        elif choice == "11":

            generate_html_report(target)

        elif choice == "12":

           take_screenshot(target)

        elif choice == "13":

           ssl_inspector(target)

        elif choice == "14":

           dns_security_check(target)

        elif choice == "15":

           security_headers_check(target)

        elif choice == "16":

           security_score()

        elif choice == "17":

           custom_port_scan(target)

        elif choice == "18":

            confirm = input(
               "\nFull scan may take a long time. Continue? (y/n): "
            )

            if confirm.lower() == "y":

              full_port_scan(target)

        elif choice == "19":

           threaded_port_scan(
              target
           )

        elif choice == "20":

           detect_service(target)

        elif choice == "0":

             print("\nExiting LIPAS...")
             break

        else:

            print("\nInvalid Option")


if __name__ == "__main__":
    menu()
