TECH_RESULTS = []

import requests


def detect_technology(target):

    if not target.startswith("http"):
        target = "https://" + target

    try:

        response = requests.get(
            target,
            timeout=10
        )

        headers = response.headers
        html = response.text.lower()

        print("\n" + "=" * 50)
        print("LIPAS TECHNOLOGY DETECTOR")
        print("=" * 50 + "\n")

        server = headers.get(
            "Server",
            "Unknown"
        )

        print(f"Server : {server}")

        technologies = []

        if "cloudflare" in str(headers).lower():
            technologies.append("Cloudflare")
            TECH_RESULTS.append("Cloudflare")

        if "wordpress" in html:
            technologies.append("WordPress")
            TECH_RESULTS.append("WordPress")

        if "react" in html:
            technologies.append("React")
            TECH_RESULTS.append("WordPress")

        if "angular" in html:
            technologies.append("Angular")
            TECH_RESULTS.append("Angular")

        if "vue" in html:
            technologies.append("Vue.js")
            TECH_RESULTS.append("Vue.js")

        if "bootstrap" in html:
            technologies.append("Bootstrap")
            TECH_RESULTS.append("Bootstrap")

        if "jquery" in html:
            technologies.append("jQuery")
            TECH_RESULTS.append("jQuery")

        print("\nDetected Technologies:\n")

        if technologies:

            for tech in technologies:
                print(f"[+] {tech}")

        else:

            print("No technologies detected")

    except Exception as e:

        print(f"Error: {e}")
