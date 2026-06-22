from cache.redis_manager import (

    set_cache,

    get_cache

)


def cache_reports(

    reports

):

    set_cache(

        "reports",

        reports

    )


def get_cached_reports():

    return get_cache(

        "reports"

    )
