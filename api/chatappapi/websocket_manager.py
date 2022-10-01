from fastapi import WebSocket
from typing import List


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, messages: List):
        await websocket.accept()
        self.active_connections.append(websocket)
        print("NUM CONNECTIONS:", len(self.active_connections))

        print("AVAILABLE MESSAGES", len(messages))
        for m in messages:
            print("Message", m)
            await self.broadcast_json(m)

    def disconnect(self, websocket: WebSocket):
        print("DISCONNECT CALLED")
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_json(self, data: object):
        for connection in self.active_connections:
            print("MESSAGE BROADCASTED", data)
            await connection.send_json(data=data)
