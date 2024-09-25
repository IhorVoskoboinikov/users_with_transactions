from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from users.schemas import UserCreate, UserUpdate
from users.crud import (
    create_user,
    get_user,
    get_all_users,
    delete_user,
    update_user,
    get_user_by_name
)
from logger import logger
import config

router = APIRouter()


@router.post("/users", tags=["Users"], responses=config.RESPONSES_USER)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info("start.add_user...")
    db_user = await get_user_by_name(db=db, user_name=user.user_name)
    if db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await create_user(db=db, user_data=user)
    return user


@router.get("/users/{user_id}", tags=["Users"], responses=config.RESPONSES_USER)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("start.get_user...")
    db_user = await get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users", tags=["Users"], responses=config.RESPONSES_USER)
async def read_all_users(db: AsyncSession = Depends(get_db)):
    logger.info("start.read_all_users...")
    users = await get_all_users(db)
    return users


@router.put("/users/{user_id}", tags=["Users"], responses=config.RESPONSES_USER)
async def update_existing_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db)):
    logger.info("start.update_existing_user...")

    user = await get_user(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    existing_user = await get_user_by_name(db=db, user_name=user_update.user_name)

    if existing_user and existing_user.id != user_id:
        raise HTTPException(status_code=400, detail="User with this name already exists")

    return await update_user(db=db, user_id=user_id, user_update=user_update)


@router.delete("/users/{user_id}", tags=["Users"], responses=config.RESPONSES_USER)
async def remove_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("start.remove_user...")
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await delete_user(db=db, user=db_user)
    return {"detail": f"User '{db_user.user_name}' deleted successfully"}
