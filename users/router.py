from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import openapi_responses
from dependencies import get_db
from users.schemas import UserCreate
from users.crud import create_user, get_user_by_id, get_user_by_name, get_users
from logger import logger

router = APIRouter()


@router.post(
    "/users", tags=["Users"], responses=openapi_responses.RESPONSES_USER_CREATE
)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info("start.add_user...")
    db_user = await get_user_by_name(db=db, user_name=user.user_name)
    if db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await create_user(db=db, user_data=user)
    return user


@router.get(
    "/users/{user_id}", tags=["Users"], responses=openapi_responses.RESPONSES_GER_USER
)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("start.get_user...")
    db_user = await get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users", tags=["Users"], responses=openapi_responses.RESPONSES_USERS)
async def get_all_users(db: AsyncSession = Depends(get_db)):
    logger.info("start.get_all_users...")
    users = await get_users(db)
    return users
