from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class DuaCreate(BaseModel):
    title: str
    content: str

class Dua(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True
