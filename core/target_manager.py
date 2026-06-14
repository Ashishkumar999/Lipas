CURRENT_TARGET = None


def set_target(

    target

):

    global CURRENT_TARGET

    CURRENT_TARGET = target


def get_target():

    return CURRENT_TARGET


def show_target():

    print(
        f"\nCurrent Target: "
        f"{CURRENT_TARGET}"
    )
