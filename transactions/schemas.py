from typing import Optional

from pydantic import BaseModel
from datetime import date


class TransactionBase(BaseModel):
    user_id: int
    creation_date: Optional[date] = None
    transaction_type: str
    transaction_amount: float


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    user_id: Optional[int] = None
    creation_date: Optional[date] = None
    transaction_type: Optional[str] = None
    transaction_amount: Optional[float] = None


class TransactionList(TransactionBase):
    id: int

    class Config:
        from_attributes = True
