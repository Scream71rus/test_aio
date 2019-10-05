
from aiohttp import web

from handlers.main.main import Main

urls = [web.get('/', Main)]
