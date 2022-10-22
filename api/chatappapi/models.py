from sqlalchemy.sql import func

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from base import Base


class User(Base):
    __tablename__ = "users"

    id: Column = Column(String, primary_key=True, index=True)
    first_name: Column = Column(String)
    last_name: Column = Column(String)
    email: Column = Column(String, unique=True, index=True)
    profile_image_url: Column = Column(String)


class Chat(Base):
    __tablename__: str = "chats"

    id: Column = Column(String, primary_key=True)
    data: Column = Column(String)
    created: Column = Column(DateTime(timezone=True), default=func.now())
