from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from users.models import User
from users.schemas import UserCreate, UserList


async def create_user(user_data: UserCreate, db: AsyncSession):
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"ID": new_user.id}


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(
        select(User).options(joinedload(User.transactions)).where(User.id == user_id)
    )
    return result.unique().scalar_one_or_none()


async def get_user_by_name(db: AsyncSession, user_name: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.user_name == user_name))
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession):
    result = await db.execute(select(User).options(joinedload(User.transactions)))
    users = result.scalars().unique().all()
    return [UserList.model_validate(user) for user in users]
