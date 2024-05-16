from flask import Flask, request, jsonify, render_template
import websockets
import asyncio
import json

app = Flask(__name__)

async def get_data():

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        
        # Subscribe with personal APIKey and Coordinates bounding the Laconian Gulf
        subscribe_message = {"APIKey": "3c82996c4984bb95afc17ada12dd4c193c6c47ea",
                             "BoundingBoxes": [[[36.86687546866755, 22.184442828560584], 
                                                [36.199014645278616, 23.13974778084953]]]} 

        subscribe_message_json = json.dumps(subscribe_message)
        
        
        await websocket.send(subscribe_message_json)

        
        while True:
            # Process websocket messages
            message = await websocket.recv()
            print(message)



@app.route("/")
def index():
    message =  asyncio.run(get_data())
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
