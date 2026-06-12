from datetime import datetime


def log_event(message):

    timestamp = datetime.now()

    with open(
        "lipas.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"[{timestamp}] "
            f"{message}\n"
        )
