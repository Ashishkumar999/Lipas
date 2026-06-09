import dns.resolver

def dns_lookup(domain):

    print(f"\n[+] DNS Information for {domain}\n")

    records = ["A", "AAAA", "MX", "NS", "TXT"]

    for record in records:

        try:

            answers = dns.resolver.resolve(
                domain,
                record
            )

            print(f"[{record}]")

            for answer in answers:
                print(answer)

            print()

        except:
            pass
