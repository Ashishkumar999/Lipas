def generate_html():

    html = """

<html>

<body>

<h1>

LIPAS REPORT

</h1>

</body>

</html>

"""

    with open(

        "reports/report.html",

        "w"

    ) as file:

        file.write(
            html
        )

    print(

        "HTML Report Created"

    )
