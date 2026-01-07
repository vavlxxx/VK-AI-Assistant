from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR: Path = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "bot.db"


class Settings(BaseSettings):
    vk_api_key: str
    openai_api_key: str
    ai_model: str = "gpt-4o-mini"
    openai_api_url: str

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env",),
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
