import ssl
import socket


def ssl_inspector(target):

    print("\n" + "=" * 50)
    print("LIPAS SSL INSPECTOR")
    print("=" * 50 + "\n")

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (target, 443)
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=target
            ) as ssock:

                cert = ssock.getpeercert()

                print(
                    f"Issuer : {cert.get('issuer')}"
                )

                print(
                    f"Subject : {cert.get('subject')}"
                )

                print(
                    f"Valid From : {cert.get('notBefore')}"
                )

                print(
                    f"Valid Until : {cert.get('notAfter')}"
                )

    except Exception as e:

        print(
            f"SSL Inspection Failed: {e}"
        )
