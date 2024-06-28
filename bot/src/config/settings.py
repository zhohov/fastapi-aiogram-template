from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = Field(..., env="TOKEN")
    parse_mode: str = Field(env="parse_mode")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
