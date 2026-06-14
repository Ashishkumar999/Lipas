from intelligence.vulnerability_knowledge import (
    VULN_KNOWLEDGE
)


def explain_vulnerability(

    title

):

    for key in VULN_KNOWLEDGE:

        if key.lower() in title.lower():

            return VULN_KNOWLEDGE[key]

    return {

        "why":
        "No explanation available.",

        "attack":
        "Unknown",

        "impact":
        "Unknown",

        "remediation":
        "Review manually."
    }
