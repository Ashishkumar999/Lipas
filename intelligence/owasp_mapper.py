OWASP_MAP = {

    "Missing CSP":

        "A05",

    "Wildcard CORS Policy":

        "A05",

    "JWT Uses alg=none":

        "A07",

    "Sensitive File Exposed":

        "A05",

    "Backup File Exposed":

        "A05",

    "Known Vulnerability":

        "A06"
}


def map_owasp(title):

    for key in OWASP_MAP:

        if key.lower() in title.lower():

            return OWASP_MAP[key]

    return "Unknown"
