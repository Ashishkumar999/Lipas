import requests

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    add_technology
)

from core.ui import (
    banner,
    success,
    warning
)

TECH_RESULTS = []


def detect_technology():

    target = get_target()

    if not target:

        warning(
            "No Target Selected"
        )

        return

    if not target.startswith(
        "http"
    ):

        target = (
            "https://" + target
        )

    banner(
        "LIPAS TECHNOLOGY DETECTOR"
    )

    try:

        response = requests.get(
            target,
            timeout=10
        )

        headers = response.headers

        html = response.text.lower()

        server = headers.get(
            "Server",
            "Unknown"
        )

        success(
            f"Server: {server}"
        )

        add_technology(
            get_target(),
            server
        )

        technologies = []

        signatures = {

            "wordpress": "WordPress",

            "react": "React",

            "angular": "Angular",

            "vue": "Vue.js",

            "bootstrap": "Bootstrap",

            "jquery": "jQuery"

        }

        for key, value in signatures.items():

            if key in html:

                technologies.append(
                    value
                )

        if "cloudflare" in str(
            headers
        ).lower():

            technologies.append(
                "Cloudflare"
            )

        if technologies:

            for tech in technologies:

                success(
                    f"Detected: {tech}"
                )

                TECH_RESULTS.append(
                    tech
                )

                add_technology(
                    get_target(),
                    tech
                )

        else:

            warning(
                "No Technologies Detected"
            )

    except Exception as e:

        warning(
            str(e)
        )
