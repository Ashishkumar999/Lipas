from intelligence.owasp_intelligence import (
    OWASP_INTELLIGENCE
)


def enrich_finding(

    finding

):

    owasp = finding.get(
        "owasp"
    )

    data = OWASP_INTELLIGENCE.get(
        owasp
    )

    if not data:

        return finding

    finding["owasp_name"] = (
        data["name"]
    )

    finding["attack_scenario"] = (
        data["attack"]
    )

    finding["business_impact"] = (
        data["impact"]
    )

    finding["reference"] = (
        data["reference"]
    )

    return finding
