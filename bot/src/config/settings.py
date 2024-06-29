from pydantic import Field
from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")
    redis_password: str = Field(..., env="REDIS_PASSWORD")


class Settings(BaseSettings):
    token: str = Field(..., env="TOKEN")
    parse_mode: str = Field(env="parse_mode")

    redis: RedisSettings = RedisSettings()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
