from cache.redis_manager import (

    set_cache,

    get_cache

)


def cache_findings(

    findings

):

    set_cache(

        "findings",

        findings

    )


def get_cached_findings():

    return get_cache(

        "findings"

    )
