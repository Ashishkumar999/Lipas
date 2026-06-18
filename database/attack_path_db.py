import json

DB_FILE = "database/attack_paths.json"


def load_attack_paths():

    try:

        with open(
            DB_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    except:

        return []


def save_attack_paths(
    paths
):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            paths,
            file,
            indent=4
        )


def add_attack_path(
    attack_path
):

    paths = load_attack_paths()

    paths.append(
        attack_path
    )

    save_attack_paths(
        paths
    )
