
import hashlib

import aiohttp_jinja2

from handlers.base_handler import BaseHandler
from models.customer_model import CustomerModel

from aiohttp import web

class Registration(BaseHandler):

    @aiohttp_jinja2.template('registration.html')
    async def get(self):
        pass


    async def post(self):
        data = await self.request.post()

        login = data.get('login')
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')

        check = await CustomerModel.find_by_login(login)

        if check is None:
            password = hashlib.sha256(password_1.encode()).hexdigest() if password_1 == password_2 else None
            customer = await CustomerModel.create(login, password)

            self.response.set_cookie('id', customer.get('id'))

            return web.Response(text='ok')
        else:
            return web.Response(text='Ошибка')
