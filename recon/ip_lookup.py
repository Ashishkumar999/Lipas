import socket

def ip_lookup(domain):

    try:

        ip = socket.gethostbyname(domain)

        print("\n[IP ADDRESS]")
        print(ip)

        return ip

    except Exception as e:

        print(f"Error: {e}")

        return None
