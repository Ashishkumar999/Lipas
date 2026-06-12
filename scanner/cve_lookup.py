CVE_RESULTS = []

CVE_DATABASE = {

    "OpenSSH_8.2": [
        "CVE-2023-38408"
    ],

    "Apache/2.4.49": [
        "CVE-2021-41773",
        "CVE-2021-42013"
    ],

    "Apache/2.4.50": [
        "CVE-2021-42013"
    ],

    "nginx/1.18.0": [
        "Review current advisories"
    ]
}


def cve_lookup():

    print("\n" + "=" * 50)
    print("LIPAS CVE LOOKUP")
    print("=" * 50 + "\n")

    software = input(
        "Enter Software Version: "
    )

    results = CVE_DATABASE.get(
        software
    )

   if results:

    CVE_RESULTS.extend(
        results
    )

    print(
        "\nKnown References:\n"
    )

    for cve in results:

        print(cve)

    else:

        print(
            "\nNo local match found."
        )
