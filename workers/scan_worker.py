from workers.task_queue import (

    get_task

)


def scan_worker():

    task = get_task()

    if task:

        print()

        print(

            "Processing Scan Task"

        )

        print()

        print(

            task

        )

    else:

        print(

            "No Tasks"

        )
