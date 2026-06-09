import sys

from recon.dns_lookup import dns_lookup
from recon.ip_lookup import ip_lookup
from recon.reverse_dns import reverse_dns
from recon.whois_lookup import whois_lookup


def banner():

    GREEN = "\033[92m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    print(f"""{GREEN}

██╗     ██╗██████╗  █████╗ ███████╗
██║     ██║██╔══██╗██╔══██╗██╔════╝
██║     ██║██████╔╝███████║███████╗
██║     ██║██╔═══╝ ██╔══██║╚════██║
███████╗██║██║     ██║  ██║███████║
╚══════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝

{CYAN}LIPAS v1.0{RESET}
""")


def main():

    banner()

    if len(sys.argv) != 3:

        print("Usage:")
        print("python lipas.py recon domain.com")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "recon":

        dns_lookup(target)

        whois_lookup(target)

        ip = ip_lookup(target)

        if ip:
            reverse_dns(ip)

    else:

        print("Unknown command")


if __name__ == "__main__":
    main()
