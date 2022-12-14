from uuid import uuid4
from fastapi import Depends, FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from websockets.exceptions import ConnectionClosedError
from starlette.websockets import WebSocketDisconnect

from sqlalchemy.orm import Session

from models import User, Chat

from websocket_manager import ConnectionManager

from deps import get_db
from schemas import UserIn, UserOut

from base import Base
from database import engine, SessionLocal as session

# wipe the database on app startup
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with session.begin() as session:

    res = session.query(User).all()
    print("USERS -> ", res)

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


@app.post("/user/register", response_model=UserOut)
def user(user: UserIn, db: Session = Depends(get_db)) -> UserOut:
    new_user = User(
        id=str(uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        profile_image_url=user.profile_img_url,
    )
    with db.begin():
        db.add(new_user)
    return user


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket, db: Session = Depends(get_db)
) -> None:
    await manager.connect(websocket=websocket, messages=chat_db)
    try:
        while True:
            print("RECEIVING AND SENDING MESSAGES")
            data: str = await websocket.receive_text()

            new_chat: Chat = Chat(id=str(uuid4()), data=data)
            with db.begin():
                db.add(new_chat)

            msg = {
                "msg": data,
                "created": new_chat.created.strftime("%m/%d/%Y %-I:%M:%S %p"),
            }
            await manager.broadcast_json(msg)
    except (ConnectionClosedError, WebSocketDisconnect) as ex:
        manager.disconnect(websocket=websocket)
