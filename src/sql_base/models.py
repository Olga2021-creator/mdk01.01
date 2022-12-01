from pydantic import BaseModel
from typing import Optional


class Staff(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    post_id: int
    name: str
    surname: str
    date_birth: str


class StaffSearch(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    post_id: Optional[int]
    name: Optional[str]
    surname: Optional[str]
    date_birth: Optional[str]


class User(BaseModel):
    login: str
    password: str
