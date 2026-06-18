import time

from scheduler.background_scan import (
    background_scan
)


def scheduler():

    print()

    print(
        "Scheduler Started"
    )

    while True:

        background_scan()

        print()

        print(
            "Sleeping 1 Hour..."
        )

        time.sleep(

            3600

        )
