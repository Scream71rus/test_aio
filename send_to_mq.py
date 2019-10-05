
import random
import json

import asyncio
import aio_pika

async def main(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/", loop=loop
    )

    routing_key = "test_queue"
    channel = await connection.channel()
    msg = {
        'id': 1,
        'msg': random.randint(1, 100),
    }
    print(msg)

    await channel.default_exchange.publish(
        aio_pika.Message(
            body=json.dumps(msg).encode()
        ),
        routing_key=routing_key
    )

    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()