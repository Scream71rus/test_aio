
import json

import aio_pika

async def listen_to_mq(loop, app):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
        loop=loop
    )

    async with connection:
        queue_name = "test_queue"
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    mq_data = message.body.decode()
                    data = json.loads(mq_data)

                    for ws_data in app['websockets']:
                        if ws_data.get('id') == str(data.get('id')):
                            await ws_data.get('ws').send_str(str(data.get('msg')))
