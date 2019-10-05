
from aiohttp import web
import aiohttp


async def ws_handler(request):
    ws = web.WebSocketResponse(autoping=True, heartbeat=60)
    await ws.prepare(request)

    request.app['websockets'].append({
        'ws': ws,
        'id': request.query.get('id')
    })

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)

        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws
