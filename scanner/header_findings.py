import requests

from core.target_manager import (
    get_target
)

from core.findings_manager import (
    add_finding
)

from core.ui import (
    banner,
    success,
    warning
)


def header_findings():

    target = get_target()

    if not target:

        warning(
            "No target selected"
        )

        return

    if not target.startswith(
        "http"
    ):

        url = (
            "https://" + target
        )

    else:

        url = target

    banner(
        "LIPAS HEADER FINDINGS"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        headers = response.headers

        if "Content-Security-Policy" not in headers:

            warning(
                "Missing CSP"
            )

            add_finding(

                target,

                "Missing Content Security Policy",

                "HIGH 🔴",

                "A05",

                8.2,

                "Clickjacking and XSS risk",

                "Implement CSP"

            )

        else:

            success(
                "CSP Present"
            )

        if "Strict-Transport-Security" not in headers:

            warning(
                "Missing HSTS"
            )

            add_finding(

                target,

                "Missing HSTS",

                "MEDIUM 🟠",

                "A02",

                6.5,

                "MITM attacks possible",

                "Enable HSTS"

            )

        else:

            success(
                "HSTS Present"
            )

        if "X-Frame-Options" not in headers:

            warning(
                "Missing X-Frame-Options"
            )

            add_finding(

                target,

                "Missing X-Frame-Options",

                "MEDIUM 🟠",

                "A05",

                5.5,

                "Clickjacking risk",

                "Add X-Frame-Options"

            )

        else:

            success(
                "XFO Present"
            )

    except Exception as e:

        warning(
            str(e)
        )
