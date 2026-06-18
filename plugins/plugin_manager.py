from plugins.plugin_registry import (
    PLUGIN_REGISTRY
)


def register_plugin(

    name,

    function

):

    PLUGIN_REGISTRY[
        name
    ] = function


def run_plugin(

    name

):

    if name in PLUGIN_REGISTRY:

        PLUGIN_REGISTRY[
            name
        ]()

    else:

        print(

            "Plugin Not Found"

        )


def show_plugins():

    print()

    print(

        "Loaded Plugins"

    )

    print()

    for plugin in PLUGIN_REGISTRY:

        print(

            plugin

        )
