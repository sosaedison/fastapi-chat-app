from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from websockets.exceptions import ConnectionClosedError
from starlette.websockets import WebSocketDisconnect


from websocket_manager import ConnectionManager

from utils import now_as_str

manager = ConnectionManager()

chat_db = []

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
- when a new user connects, they should be sent all the messages that they don't already have 
- the messages only live while the app is live
"""


@app.get("/")
def home():
    return "Hello world"


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket=websocket, messages=chat_db)
    try:
        while True:
            print("RECEIVING AND SENDING MESSAGES")
            data = await websocket.receive_text()
            msg = {"msg": data, "created": now_as_str()}
            chat_db.append(msg)
            await manager.broadcast_json(msg)
    except (ConnectionClosedError, WebSocketDisconnect) as ex:
        manager.disconnect(websocket=websocket)
