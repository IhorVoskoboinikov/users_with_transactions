from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}" \
                          f"@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal: sessionmaker[AsyncSession] = sessionmaker[AsyncSession](
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()
