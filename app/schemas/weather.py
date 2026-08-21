from datetime import datetime

from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    country: str | None
    temperature: float | None
    feels_like: float | None
    humidity: int | None
    pressure: int | None
    wind_speed: float | None
    description: str | None
    observed_at: datetime


class ForecastItem(BaseModel):
    datetime: datetime
    temperature: float | None
    feels_like: float | None
    humidity: int | None
    wind_speed: float | None
    description: str | None


class ForecastResponse(BaseModel):
    city: str
    country: str | None
    forecast: list[ForecastItem]
