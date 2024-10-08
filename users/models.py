from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(255), nullable=False, unique=True)

    transactions = relationship(
        "UserTransaction", back_populates="user", cascade="all, delete-orphan"
    )
