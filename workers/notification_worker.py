from workers.task_queue import (

    get_task

)


def notification_worker():

    task = get_task()

    if task:

        print()

        print(

            "Sending Notification"

        )

        print(

            task

        )

    else:

        print(

            "No Tasks"

        )
