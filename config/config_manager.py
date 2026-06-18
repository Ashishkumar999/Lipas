import json

CONFIG_FILE = "config/settings.json"


def load_config():

    try:

        with open(

            CONFIG_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(
                file
            )

    except:

        return {}
