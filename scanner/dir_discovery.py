import requests

from core.target_manager import (
    get_target
)

from core.asset_manager import (
    add_directory
)

from core.ui import (
    banner,
    success
)

FOUND_DIRS = []


with open(

    "wordlists/common_dirs.txt"

) as file:

    WORDLIST = [

        line.strip()

        for line in file

        if line.strip()

    ]


def dir_discovery():

    target = get_target()

    if not target:

        return

    if not target.startswith(

        "http"

    ):

        target = (

            "https://" + target

        )

    banner(

        "LIPAS DIRECTORY DISCOVERY"

    )

    found = 0

    for item in WORDLIST:

        try:

            url = (

                f"{target}/{item}"

            )

            response = requests.get(

                url,

                timeout=5,

                allow_redirects=False

            )

            if response.status_code in [

                200,

                301,

                302,

                403

            ]:

                success(

                    f"[{response.status_code}] {url}"

                )

                FOUND_DIRS.append(

                    url

                )

                add_directory(

                    get_target(),

                    url

                )

                found += 1

        except:

            pass

    print()

    print(

        f"Total Found: {found}"

    )
