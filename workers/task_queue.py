TASK_QUEUE = []


def add_task(

    task

):

    TASK_QUEUE.append(

        task

    )


def get_task():

    if TASK_QUEUE:

        return TASK_QUEUE.pop(

            0

        )

    return None


def show_queue():

    print()

    print(

        TASK_QUEUE

    )
