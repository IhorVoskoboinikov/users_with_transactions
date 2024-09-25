from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from users.models import User
from users.schemas import UserCreate, UserUpdate, UserList


async def create_user(user_data: UserCreate, db: AsyncSession):
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_user_by_name(db: AsyncSession, user_name: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.user_name == user_name))
    return result.scalar_one_or_none()


async def get_all_users(db: AsyncSession):
    result = await db.execute(
        select(User).options(joinedload(User.transactions))
    )
    users = result.scalars().unique().all()
    return [UserList.model_validate(user) for user in users]


async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate) -> Optional[User]:
    user = await get_user(db, user_id)
    if user:
        if user_update.user_name is not None:
            user.user_name = user_update.user_name
        await db.commit()
        await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user: User) -> None:
    await db.delete(user)
    await db.commit()
