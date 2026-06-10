from datetime import datetime


def generate_html_report(target):

    filename = target.replace(".", "_")

    report_file = f"reports/{filename}_report.html"

    html = f"""
<html>
<head>
<title>LIPAS Report</title>

<style>

body {{
    font-family: Arial;
    margin: 40px;
    background: #f5f5f5;
}}

h1 {{
    color: #0a66c2;
}}

.section {{
    background: white;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 10px;
}}

</style>

</head>

<body>

<h1>LIPAS VAPT REPORT</h1>

<div class="section">
<h2>Target</h2>
<p>{target}</p>
</div>

<div class="section">
<h2>Date</h2>
<p>{datetime.now()}</p>
</div>

<div class="section">
<h2>Status</h2>
<p>Scan Completed</p>
</div>

</body>
</html>
"""

    with open(report_file, "w") as file:

        file.write(html)

    print(
        f"\n[+] HTML Report Saved: {report_file}"
    )
