from profiles.scan_profiles import (
    quick_scan,
    web_audit,
    full_assessment
)


def profile_menu(target):

    print("\n" + "=" * 50)
    print("LIPAS SCAN PROFILES")
    print("=" * 50)

    print("\n1. Quick Scan")
    print("2. Web Audit")
    print("3. Full Assessment")

    choice = input(
        "\nSelect Profile: "
    )

    if choice == "1":

        quick_scan(target)

    elif choice == "2":

        web_audit(target)

    elif choice == "3":

        full_assessment(target)

    else:

        print(
            "Invalid Profile."
        )
