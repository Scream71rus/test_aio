
import os
import json

import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncpg

from workers.listen_mq import listen_to_mq
from application import Application
from urls import urls
from models.base_model import BaseModel


app = Application()

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(os.path.abspath(os.curdir), 'templates')))

async def connect_to_db(app):
    app['db'] = await asyncpg.connect(
        database = 'aio',
        user = 'admin',
        password = 'admin',
        host = 'localhost'
    )
    BaseModel.db = app['db']

async def start_background_tasks(app):
    loop = asyncio.get_event_loop()
    app['mq_listener'] = asyncio.create_task(listen_to_mq(loop, app))
    app['websockets'] = []

app.add_routes(urls)
app.on_startup.append(connect_to_db)
app.on_startup.append(start_background_tasks)
web.run_app(app, port=9090)
