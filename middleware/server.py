import asyncio, websockets, json, random

async def producer():
    while True:
        await asyncio.sleep(0.05)
        yield {'value': random.random()}

async def handler(ws):
    async for d in producer():
        await ws.send(json.dumps(d))

async def main():
    print('ws://localhost:9001')
    async with websockets.serve(handler,'0.0.0.0',9001):
        await asyncio.Future()

if __name__=='__main__': asyncio.run(main())
