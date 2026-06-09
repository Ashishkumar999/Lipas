import sys

from recon.dns_lookup import dns_lookup

def banner():

    print("""
 _      _____ _____   ___   _____
| |    |_   _|  __ \\ / _ \\ / ____|
| |      | | | |__) | | | | (___
| |      | | |  ___/| | | |\\___ \\
| |____ _| |_| |    | |_| |____) |
|______|_____|_|     \\___/|_____/

Lipas v1.0
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

    else:

        print("Unknown command")

if __name__ == "__main__":
    main()
