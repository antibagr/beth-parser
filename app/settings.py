from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    ENVIRONMENT: str
    DEBUG: bool
    SITEMAP_URL: HttpUrl
    ANTI_CAPTCHA_API_KEY: str
    ANTI_CAPTCHA_SITE_KEY: str
    BATCH_SIZE: int
    MONGO_DB_URI: str
    MONGO_DB_NAME: str

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "prod"


settings = Settings(_env_file=".env")  # type: ignore[call-arg]
