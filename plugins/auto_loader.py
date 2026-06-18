from plugins.plugin_manager import (
    register_plugin
)

from plugins.header_plugin import run as header

from plugins.ssl_plugin import run as ssl

from plugins.cookie_plugin import run as cookie

from plugins.cors_plugin import run as cors

from plugins.security_score_plugin import run as score


def load_plugins():

    register_plugin(
        header
    )

    register_plugin(
        ssl
    )

    register_plugin(
        cookie
    )

    register_plugin(
        cors
    )

    register_plugin(
        score
    )
