from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    FAST_APP_HOST: str
    FAST_APP_PORT: int

    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env"


# Инициализация настроек
settings = Settings()

