from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List, Optional

from transactions.models import UserTransaction
from transactions.schemas import TransactionCreate, TransactionList, TransactionUpdate

async def create_transaction(db: AsyncSession, transaction_data: TransactionCreate) -> UserTransaction:
    transaction = UserTransaction(**transaction_data.model_dump())
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction

async def get_transaction(db: AsyncSession, transaction_id: int) -> Optional[UserTransaction]:
    result = await db.execute(select(UserTransaction).where(UserTransaction.id == transaction_id))
    return result.scalar_one_or_none()

async def get_all_transactions(db: AsyncSession) -> List[TransactionList]:
    result = await db.execute(select(UserTransaction).options(selectinload(UserTransaction.user)))
    transactions = result.scalars().all()
    return [TransactionList.model_validate(transaction) for transaction in transactions]

async def update_transaction(
        db: AsyncSession,
        transaction_id: int,
        transaction_update: TransactionUpdate
) -> Optional[UserTransaction]:
    transaction = await get_transaction(db, transaction_id)
    if transaction:
        for key, value in transaction_update.model_dump(exclude_unset=True).items():
            setattr(transaction, key, value)
        await db.commit()
        await db.refresh(transaction)
    return transaction

async def delete_transaction(db: AsyncSession, transaction_id: int) -> Optional[UserTransaction]:
    transaction = await get_transaction(db, transaction_id)
    if transaction:
        await db.delete(transaction)
        await db.commit()
    return transaction
