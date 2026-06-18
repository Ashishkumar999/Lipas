from plugins.plugin_manager import (
    register_plugin
)

from plugins.header_plugin import (
    run as header_plugin
)

from plugins.ssl_plugin import (
    run as ssl_plugin
)

from plugins.cookie_plugin import (
    run as cookie_plugin
)

from plugins.cors_plugin import (
    run as cors_plugin
)

from plugins.security_score_plugin import (
    run as security_score_plugin
)


def load_plugins():

    register_plugin(

        "header",

        header_plugin

    )

    register_plugin(

        "ssl",

        ssl_plugin

    )

    register_plugin(

        "cookie",

        cookie_plugin

    )

    register_plugin(

        "cors",

        cors_plugin

    )

    register_plugin(

        "security_score",

        security_score_plugin

    )
