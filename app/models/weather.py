from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class WeatherHistory(Base, TimestampMixin):
    __tablename__ = "weather_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    city: Mapped[str] = mapped_column(String(100), index=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    temperature: Mapped[float | None] = mapped_column(Float, nullable=True)
    feels_like: Mapped[float | None] = mapped_column(Float, nullable=True)
    humidity: Mapped[int | None] = mapped_column(Integer, nullable=True)
    pressure: Mapped[int | None] = mapped_column(Integer, nullable=True)
    wind_speed: Mapped[float | None] = mapped_column(Float, nullable=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    observed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user = relationship("User", back_populates="weather_history")
