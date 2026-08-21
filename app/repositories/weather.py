from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.weather import WeatherHistory


class WeatherRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, weather: WeatherHistory):
        self.db.add(weather)
        self.db.commit()
        self.db.refresh(weather)
        return weather

    def get_history(self, user_id: int, skip: int = 0, limit: int = 20):
        return self.db.scalars(
            select(WeatherHistory)
            .where(WeatherHistory.user_id == user_id)
            .order_by(WeatherHistory.observed_at.desc())
            .offset(skip)
            .limit(limit)
        ).all()
