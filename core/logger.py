from datetime import datetime


def write_log(

    logfile,

    message

):

    with open(

        logfile,

        "a",

        encoding="utf-8"

    ) as file:

        timestamp = (

            datetime.now()

        )

        file.write(

            f"[{timestamp}] "

            f"{message}\n"

        )


def scanner_log(

    message

):

    write_log(

        "logs/scanner.log",

        message

    )


def error_log(

    message

):

    write_log(

        "logs/error.log",

        message

    )


def activity_log(

    message

):

    write_log(

        "logs/activity.log",

        message

    )


def log_event(

    message

):

    activity_log(

        message

    )
