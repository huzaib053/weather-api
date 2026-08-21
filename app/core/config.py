from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Weather API"
    DEBUG: bool = True

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    WEATHER_API_KEY: str
    WEATHER_API_BASE_URL: str = "https://api.openweathermap.org/data/2.5"

    CORS_ORIGINS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        return [
            x.strip()
            for x in self.CORS_ORIGINS.split(",")
            if x.strip()
        ]


settings = Settings()