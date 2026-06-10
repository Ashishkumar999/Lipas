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

        if "wordpress" in html:
            technologies.append("WordPress")

        if "react" in html:
            technologies.append("React")

        if "angular" in html:
            technologies.append("Angular")

        if "vue" in html:
            technologies.append("Vue.js")

        if "bootstrap" in html:
            technologies.append("Bootstrap")

        if "jquery" in html:
            technologies.append("jQuery")

        print("\nDetected Technologies:\n")

        if technologies:

            for tech in technologies:
                print(f"[+] {tech}")

        else:

            print("No technologies detected")

    except Exception as e:

        print(f"Error: {e}")
