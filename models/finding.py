class Finding:

    def __init__(

        self,

        finding_id,

        title,

        severity,

        owasp,

        cvss,

        impact,

        remediation,

        asset

    ):

        self.finding_id = finding_id

        self.title = title

        self.severity = severity

        self.owasp = owasp

        self.cvss = cvss

        self.impact = impact

        self.remediation = remediation

        self.asset = asset


    def to_dict(self):

        return {

            "id": self.finding_id,

            "title": self.title,

            "severity": self.severity,

            "owasp": self.owasp,

            "cvss": self.cvss,

            "impact": self.impact,

            "remediation": self.remediation,

            "asset": self.asset
        }
