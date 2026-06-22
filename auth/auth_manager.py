import json


USER_DB = "auth/users.json"


def login(

    username,

    password

):

    with open(

        USER_DB,

        "r"

    ) as file:

        users = json.load(

            file

        )

    for user in users:

        if (

            user["username"] == username

            and

            user["password"] == password

        ):

            return user

    return None
