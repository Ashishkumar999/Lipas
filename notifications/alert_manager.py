from notifications.email_notification import (
    send_email
)

from notifications.slack_notification import (
    send_slack
)

from notifications.telegram_notification import (
    send_telegram
)


def send_alert(

    title,

    message

):

    send_email(

        title,

        message

    )

    send_slack(

        message

    )

    send_telegram(

        message

    )
