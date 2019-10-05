
import json

import aiohttp.web
import redis


class Application(aiohttp.web.Application):

    @property
    def cache(self):
        return self._cache

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._redis_pool = redis.ConnectionPool(
            host='localhost',
            port=6379,
            db=1)

        self._cache = redis.StrictRedis(connection_pool=self._redis_pool)

