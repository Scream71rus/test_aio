
import aiohttp_jinja2
from handlers.base_handler import BaseHandler


@aiohttp_jinja2.template('index.html')
class Main(BaseHandler):
    async def get(self):
        pass