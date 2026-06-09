import whois

def whois_lookup(domain):

    try:

        w = whois.whois(domain)

        print("\n[WHOIS INFORMATION]")

        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")

    except Exception as e:

        print(f"WHOIS Error: {e}")
