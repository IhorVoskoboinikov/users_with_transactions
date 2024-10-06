from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import openapi_responses
from dependencies import get_db
from transactions.schemas import TransactionCreate, TransactionUpdate
from transactions.crud import (
    create_transaction,
    get_transaction,
    get_all_transactions,
    update_transaction,
    delete_transaction
)
from users.crud import get_user
from logger import logger

router = APIRouter()

@router.post("/transactions", tags=["Transactions"], responses=openapi_responses.RESPONSES_TRANSACTION)
async def add_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    logger.info("start.add_transaction...")
    db_user = await get_user(db=db, user_id=transaction.user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=[f"User with ID '{transaction.user_id} 'doesn't exist in db"])
    return await create_transaction(db=db, transaction_data=transaction)

@router.get("/transactions/{transaction_id}", tags=["Transactions"], responses=openapi_responses.RESPONSES_TRANSACTION)
async def read_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("start.read_transaction...")
    transaction = await get_transaction(db=db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail=f"Transaction with ID '{transaction_id}' not found")
    return transaction

@router.get("/transactions", tags=["Transactions"], responses=openapi_responses.RESPONSES_TRANSACTION)
async def read_all_transactions(db: AsyncSession = Depends(get_db)):
    logger.info("start.read_all_transactions...")
    return await get_all_transactions(db=db)

@router.put("/transactions/{transaction_id}",
            tags=["Transactions"],
            responses=openapi_responses.RESPONSES_TRANSACTION
            )
async def update_existing_transaction(
        transaction_id: int,
        transaction_update: TransactionUpdate,
        db: AsyncSession = Depends(get_db)
):
    logger.info("start.update_existing_transaction...")

    db_user = await get_user(db=db, user_id=transaction_update.user_id)

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User with ID '{transaction_update.user_id} 'doesn't exist in db"
        )

    transaction = await update_transaction(db=db, transaction_id=transaction_id, transaction_update=transaction_update)

    if transaction is None:
        raise HTTPException(status_code=404, detail=f"Transaction with ID '{transaction_id}' not found")
    return transaction

@router.delete("/transactions/{transaction_id}", tags=["Transactions"], responses=openapi_responses.RESPONSES_TRANSACTION)
async def delete_existing_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("start.delete_existing_transaction...")
    transaction = await delete_transaction(db=db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail=f"Transaction with ID '{transaction_id}' not found")
    return {"detail": f"Transaction with ID {transaction_id} deleted"}
