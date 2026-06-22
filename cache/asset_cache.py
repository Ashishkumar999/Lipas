from cache.redis_manager import (

    set_cache,

    get_cache

)


def cache_assets(

    assets

):

    set_cache(

        "assets",

        assets

    )


def get_cached_assets():

    return get_cache(

        "assets"

    )
