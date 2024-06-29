from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI", env="APP_NAME")
    debug: bool = Field(default=True, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: BaseSettings = Settings()
