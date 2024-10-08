import enum
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from database import Base


class TransactionType(enum.Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"


class UserTransaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    create_at = Column(DateTime, default=func.now(), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Float(), nullable=False)

    user = relationship("User", back_populates="transactions")
