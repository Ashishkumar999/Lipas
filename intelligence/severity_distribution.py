from database.finding_db import (
    load_findings
)


def severity_distribution():

    findings = load_findings()

    distribution = {

        "CRITICAL 🔴":0,

        "HIGH 🔴":0,

        "MEDIUM 🟠":0,

        "LOW 🟢":0

    }

    for finding in findings:

        severity = finding["severity"]

        if severity in distribution:

            distribution[severity] += 1

    return distribution

