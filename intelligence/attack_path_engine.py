from database.attack_path_db import (
    add_attack_path
)


def analyze_attack_path(

    target,

    ports,

    findings

):

    if 22 in ports:

        add_attack_path(

            {

                "target":target,

                "path":

                "SSH Credential Attack"

            }

        )

    if 80 in ports:

        if "Missing Content Security Policy" in findings:

            add_attack_path(

                {

                    "target":target,

                    "path":

                    "A05 Security Misconfiguration"

                }

            )
