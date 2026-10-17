"""Application settings, read from environment variables (and an optional .env file)."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://bakery:change-me@localhost:5432/bakery"


@lru_cache
def get_settings() -> Settings:
    """Cached so the environment is parsed once; use as a FastAPI dependency."""
    return Settings()
