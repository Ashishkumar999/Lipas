import requests

from core.target_manager import get_target
from core.findings_manager import add_finding
from core.ui import banner, success, warning


def run():

    target = get_target()

    if not target:
        warning("No target selected")
        return

    url = target

    if not target.startswith("http"):
        url = "https://" + target

    banner("COOKIE ANALYZER")

    try:

        response = requests.get(url, timeout=10)

        cookies = response.cookies

        if not cookies:

            warning("No cookies detected")
            return

        for cookie in cookies:

            print(cookie.name)

            if not cookie.secure:

                add_finding(
                    target,
                    "Cookie Missing Secure Flag",
                    "MEDIUM 🟠",
                    "A02",
                    5.3,
                    "Cookie can be intercepted",
                    "Enable Secure flag"
                )

            success(cookie.name)

    except Exception as e:

        warning(str(e))
