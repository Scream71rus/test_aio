
from aiohttp import web


class BaseHandler(web.View):

    @property
    def response(self):
         return web.Response()

    def redirect(self, url):
        return web.HTTPFound(url)
