
from aiohttp import web

from handlers.auth.registration import Registration


urls = [
    web.get('/registration', Registration),
    web.post('/registration', Registration),
]
