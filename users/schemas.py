from typing import List
from users import TransactionList

from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserList(UserBase):
    id: int
    transactions: List[TransactionList] = []

    class Config:
        from_attributes = True
