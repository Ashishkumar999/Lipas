ATTACK_PATHS = {

    "Missing CSP":

        [
            "Internet",
            "XSS",
            "Session Theft",
            "Account Takeover"
        ],

    "Wildcard CORS Policy":

        [
            "Malicious Website",
            "Cross-Origin Request",
            "Sensitive Data Access"
        ],

    "JWT Uses alg=none":

        [
            "Token Forgery",
            "Authentication Bypass",
            "Privilege Escalation"
        ],

    "Sensitive File Exposed":

        [
            "File Download",
            "Credential Disclosure",
            "System Compromise"
        ],

    "Backup File Exposed":

        [
            "Source Code Access",
            "Credential Discovery",
            "Full Application Compromise"
        ]
}
