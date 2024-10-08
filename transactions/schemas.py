from pydantic import BaseModel, Field

from transactions.models import TransactionType


class TransactionBase(BaseModel):
    user_id: int
    transaction_type: TransactionType
    amount: float


class TransactionCreate(TransactionBase):
    pass


class TransactionList(TransactionBase):
    id: int

    class Config:
        from_attributes = True
