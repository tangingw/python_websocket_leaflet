import asyncio
import json
import websockets
from androidhelper import Android


droid = Android()
droid.startLocating(1, 1000)
droid.eventWaitFor('location', 12500)

async def get_location(websocket, path):

    while True:

        current_location = droid.readLocation().result

        if not current_location:

            current_location = droid.getLastKnownLocation().result
        
        await websocket.send(
            json.dumps(current_location)
        )

        await asyncio.sleep(0.1)


def main():

    start_server = websockets.serve(get_location, '0.0.0.0', 8765)

    websocket_loop = asyncio.get_event_loop()
    websocket_loop.run_until_complete(start_server)

    try:

        websocket_loop.run_forever()

    except KeyboardInterrupt:

        websocket_loop.close()


if __name__ == '__main__':

    main()