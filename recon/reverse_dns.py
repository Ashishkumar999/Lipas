import socket

def reverse_dns(ip):

    try:

        hostname = socket.gethostbyaddr(ip)

        print("\n[REVERSE DNS]")
        print(hostname[0])

    except Exception:

        print("\n[REVERSE DNS]")
        print("No PTR record found")
