from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class TransactionBase(BaseModel):
    user_id: int
    creation_date: Optional[datetime] = None
    type: str
    amount: float


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    user_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    type: Optional[str] = None
    amount: Optional[float] = None


class TransactionList(TransactionBase):
    id: int

    class Config:
        from_attributes = True
