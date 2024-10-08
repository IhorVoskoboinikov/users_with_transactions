from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import openapi_responses
from dependencies import get_db
from transactions.crud import create_transaction
from transactions.schemas import TransactionCreate
from users.crud import get_user_by_id
from logger import logger

router = APIRouter()


@router.post(
    "/transactions",
    tags=["Transactions"],
    responses=openapi_responses.RESPONSES_TRANSACTION,
)
async def add_transaction(
    transaction: TransactionCreate, db: AsyncSession = Depends(get_db)
):
    logger.info("start.add_transaction...")
    db_user = await get_user_by_id(db=db, user_id=transaction.user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail=[f"User with ID '{transaction.user_id} 'doesn't exist in db"],
        )
    return await create_transaction(db=db, transaction_data=transaction)
