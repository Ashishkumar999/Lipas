from compliance.owasp_checker import (
    owasp_checker
)

from compliance.cis_checker import (
    cis_checker
)

from compliance.mitre_mapper import (
    mitre_mapper
)

from compliance.nist_mapper import (
    nist_mapper
)


def compliance_dashboard():

    print()

    print(

        "LIPAS COMPLIANCE DASHBOARD"

    )

    print()

    owasp_checker()

    cis_checker()

    mitre_mapper()

    nist_mapper()
