from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from websockets.exceptions import ConnectionClosedError
from starlette.websockets import WebSocketDisconnect

from websocket_manager import ConnectionManager

from utils import now_as_str
from models import UserIn, UserOut

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


@app.get("/")
def home():
    return "Hello world"


@app.post("/user/login")
def user_login(user: UserIn):
    print(user)
    return "OK"


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
