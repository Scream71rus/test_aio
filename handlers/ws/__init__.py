
from aiohttp import web

from .ws import ws_handler

urls = [web.get('/ws', ws_handler)]
