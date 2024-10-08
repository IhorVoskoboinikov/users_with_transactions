from sqlalchemy.ext.asyncio import AsyncSession

from transactions.models import UserTransaction
from transactions.schemas import TransactionCreate


async def create_transaction(
    db: AsyncSession, transaction_data: TransactionCreate
) -> UserTransaction:
    transaction = UserTransaction(**transaction_data.model_dump())
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction
