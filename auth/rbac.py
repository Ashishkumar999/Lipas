ROLES = {

    "admin": [

        "all"

    ],

    "analyst": [

        "scan",

        "report",

        "dashboard"

    ]

}


def has_permission(

    role,

    action

):

    permissions = ROLES.get(

        role,

        []

    )

    if "all" in permissions:

        return True

    return action in permissions
