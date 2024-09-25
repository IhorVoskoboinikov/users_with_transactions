from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class UserTransaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    creation_date = Column(Date, default=func.current_date(), nullable=False)
    transaction_type = Column(String(255), nullable=False)
    transaction_amount = Column(Float(), nullable=False)

    user = relationship("User", back_populates="transactions")