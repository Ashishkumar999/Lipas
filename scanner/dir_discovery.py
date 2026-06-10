FOUND_DIRS = []

import requests


WORDLIST = [
    "admin",
    "login",
    "dashboard",
    "api",
    "backup",
    "uploads",
    "config",
    "test",
    "dev",
    "robots.txt",
    "sitemap.xml"
]


def dir_discovery(target):

    print("\n" + "=" * 50)
    print("LIPAS DIRECTORY DISCOVERY")
    print("=" * 50 + "\n")

    if not target.startswith("http"):
        target = "https://" + target

    found = 0

    for item in WORDLIST:

        try:

            url = f"{target}/{item}"

            response = requests.get(
                url,
                timeout=5,
                allow_redirects=False
            )

            if response.status_code in [200, 301, 302, 403]:

               result = f"[{response.status_code}] {url}"

               print(result)

               FOUND_DIRS.append(result)

               found += 1

        except:

            pass

    print(f"\nTotal Found: {found}")
