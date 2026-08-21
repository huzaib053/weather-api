from sqlalchemy import Boolean, String,Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    cities = relationship("City", back_populates="user", cascade="all, delete-orphan")
    weather_history = relationship(
        "WeatherHistory",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    phone_no = Column(String(15), nullable=True)