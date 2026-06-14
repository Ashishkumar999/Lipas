def calculate_cvss(

    severity

):

    if severity == "CRITICAL":

        return 9.5

    elif severity == "HIGH":

        return 8.0

    elif severity == "MEDIUM":

        return 5.5

    elif severity == "LOW":

        return 3.0

    return 0
