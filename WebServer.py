# Webserver.py
import asyncio
import websockets
from random import uniform
from flask import Flask, render_template

app = Flask(__name__)

# Store connected WebSocket clients
clients = set()

# Function to simulate stock price updates
async def stock_price_updates():
    while True:
        # Simulate price updates (you can replace this with actual data)
        price = round(uniform(100, 200), 2)

        # Send the price to all connected clients
        for client in clients:
            await client.send(str(price))
        await asyncio.sleep(1)  # Update every second

# WebSocket handler
async def handle_websocket(websocket, path):
    clients.add(websocket)
    try:
        await websocket.recv()
    except websockets.ConnectionClosedError:
        pass
    finally:
        clients.remove(websocket)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(handle_websocket, "localhost", 8766))
    asyncio.run(stock_price_updates())
    app.run()

    
