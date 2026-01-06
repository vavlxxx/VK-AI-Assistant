from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR: Path = Path(__file__).parent.parent


class Settings(BaseSettings):
    vk_api_key: str
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env",),
        extra="ignore",
        case_sensitive=False,
        # env_nested_delimiter="__",
        # env_prefix="CFG_",
    )


settings = Settings()
