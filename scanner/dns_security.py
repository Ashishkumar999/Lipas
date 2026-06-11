import dns.resolver


def dns_security_check(target):

    print("\n" + "=" * 50)
    print("LIPAS DNS SECURITY CHECK")
    print("=" * 50 + "\n")

    try:

        print("[+] MX Records")

        mx_records = dns.resolver.resolve(
            target,
            "MX"
        )

        for mx in mx_records:

            print(f"  {mx}")

    except:

        print("  No MX records found")

    print()

    try:

        print("[+] SPF Record")

        txt_records = dns.resolver.resolve(
            target,
            "TXT"
        )

        found = False

        for record in txt_records:

            value = str(record)

            if "spf1" in value.lower():

                print(f"  {value}")

                found = True

        if not found:

            print("  SPF not found")

    except:

        print("  SPF lookup failed")

    print()

    try:

        print("[+] DMARC Record")

        dmarc = dns.resolver.resolve(
            "_dmarc." + target,
            "TXT"
        )

        for record in dmarc:

            print(f"  {record}")

    except:

        print("  DMARC not found")
