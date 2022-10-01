from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from websocket_manager import ConnectionManager

from utils import now_as_str

manager = ConnectionManager()

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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket=websocket)
    while True:
        data = await websocket.receive_text()
        await manager.broadcast_json({"msg": data, "created": now_as_str()})
