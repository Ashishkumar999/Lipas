from scheduler.background_scan import (
    background_scan
)


def daily_scan():

    print()

    print(
        "Daily Scan Started"
    )

    background_scan()

    print()

    print(
        "Daily Scan Completed"
    )
