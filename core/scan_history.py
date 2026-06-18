from datetime import datetime

SCAN_HISTORY = []


def add_scan_history(

    target

):

    SCAN_HISTORY.append(

        {

            "target": target,

            "time": str(

                datetime.now()

            )

        }

    )


def show_scan_history():

    print()

    print(

        "Scan History"

    )

    print()

    for item in SCAN_HISTORY:

        print(

            item

        )
