import requests

from core.target_manager import get_target
from core.findings_manager import add_finding
from core.ui import banner, warning, success


def run():

    target = get_target()

    if not target:

        warning(
            "No target selected"
        )

        return

    if not target.startswith("http"):

        url = "https://" + target

    else:

        url = target

    banner(
        "CORS ANALYZER"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        origin = response.headers.get(
            "Access-Control-Allow-Origin"
        )

        if origin == "*":

            warning(
                "Wildcard Origin Found"
            )

            add_finding(

                target,

                "Wildcard CORS",

                "MEDIUM 🟠",

                "A05",

                5.8,

                "Cross origin abuse",

                "Restrict origins"

            )

        else:

            success(
                "CORS Looks Good"
            )

    except Exception as e:

        warning(
            str(e)
        )
