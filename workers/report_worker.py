from workers.task_queue import (

    get_task

)


def report_worker():

    task = get_task()

    if task:

        print()

        print(

            "Generating Report"

        )

        print()

        print(

            task

        )

    else:

        print(

            "No Tasks"

        )
