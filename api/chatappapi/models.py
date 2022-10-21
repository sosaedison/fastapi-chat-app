from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


from typing import Union
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    profile_img_url: Union[str, None] = None


class UserOut(BaseModel):
    first_name: str
    profile_img_url: Union[str, None] = None
