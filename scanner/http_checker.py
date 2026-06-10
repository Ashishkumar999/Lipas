import requests


COMMON_PATHS = [
    "/",
    "/admin",
    "/login",
    "/dashboard",
    "/api",
    "/robots.txt",
    "/sitemap.xml",
    "/upload",
    "/register"
]


def http_checker(target):

    print("\n" + "=" * 50)
    print("LIPAS HTTP STATUS CHECKER")
    print("=" * 50 + "\n")

    if not target.startswith("http"):
        target = "https://" + target

    for path in COMMON_PATHS:

        try:

            url = target + path

            response = requests.get(
                url,
                timeout=5,
                allow_redirects=False
            )

            print(
                f"[{response.status_code}] {path}"
            )

        except Exception:

            pass
