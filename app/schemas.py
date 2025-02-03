from pydantic import BaseModel , EmailStr
from typing import Optional


class NewUser(BaseModel):
    email: EmailStr
    full_name:str
    password: str
    phone_number: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str