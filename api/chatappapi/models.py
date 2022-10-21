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
