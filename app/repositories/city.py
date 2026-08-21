from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.city import City


class CityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, user_id: int):
        return self.db.scalars(
            select(City)
            .where(City.user_id == user_id)
            .order_by(City.created_at.desc())
        ).all()

    def get_by_id(self, city_id: int, user_id: int):
        return self.db.scalar(
            select(City).where(
                City.id == city_id,
                City.user_id == user_id,
            )
        )

    def get_by_name(self, name: str, user_id: int):
        return self.db.scalar(
            select(City).where(
                City.name == name,
                City.user_id == user_id,
            )
        )

    def create(self, city: City):
        self.db.add(city)
        self.db.commit()
        self.db.refresh(city)
        return city

    def delete(self, city: City):
        self.db.delete(city)
        self.db.commit()
