from datetime import datetime

from scanner.port_scanner import OPEN_PORTS
from scanner.tech_detector import TECH_RESULTS
from scanner.dir_discovery import FOUND_DIRS
from recon.subdomain_enum import FOUND_SUBDOMAINS


def generate_html_report(target):

    filename = target.replace(".", "_")

    report_file = f"reports/{filename}_report.html"

    ports_html = ""

    for port in OPEN_PORTS:
        ports_html += f"<li>{port}</li>"

    tech_html = ""

    for tech in TECH_RESULTS:
        tech_html += f"<li>{tech}</li>"

    dir_html = ""

    for item in FOUND_DIRS:
        dir_html += f"<li>{item}</li>"

    sub_html = ""

    for sub in FOUND_SUBDOMAINS:
        sub_html += f"<li>{sub}</li>"

    html = f"""
<html>

<head>

<title>LIPAS Report</title>

<style>

body {{
    font-family: Arial;
    background: #f4f6f9;
    margin: 30px;
}}

h1 {{
    color: #0066cc;
}}

.card {{
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
}}

ul {{
    margin-top: 10px;
}}

</style>

</head>

<body>

<h1>LIPAS VAPT REPORT</h1>

<div class="card">
<h2>Target</h2>
<p>{target}</p>
</div>

<div class="card">
<h2>Scan Date</h2>
<p>{datetime.now()}</p>
</div>

<div class="card">
<h2>Open Ports</h2>
<ul>
{ports_html}
</ul>
</div>

<div class="card">
<h2>Technologies</h2>
<ul>
{tech_html}
</ul>
</div>

<div class="card">
<h2>Directories</h2>
<ul>
{dir_html}
</ul>
</div>

<div class="card">
<h2>Subdomains</h2>
<ul>
{sub_html}
</ul>
</div>

</body>

</html>
"""

    with open(report_file, "w") as file:
        file.write(html)

    print(
        f"\n[+] HTML Report Saved: {report_file}"
    )
