def attack_priority(

    severity

):

    if severity == "CRITICAL":

        return "P1"

    elif severity == "HIGH":

        return "P2"

    elif severity == "MEDIUM":

        return "P3"

    return "P4"
