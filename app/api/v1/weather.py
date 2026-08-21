from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.weather import WeatherHistory
from app.repositories.weather import WeatherRepository
from app.schemas.weather import ForecastResponse, WeatherResponse
from app.services.weather import WeatherService

router = APIRouter()


@router.get("/current", response_model=WeatherResponse)
async def current_weather(
    city: str = Query(..., min_length=1, max_length=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    data = await WeatherService().get_current_weather(city)

    WeatherRepository(db).create(
        WeatherHistory(
            user_id=current_user.id,
            **data,
        )
    )

    return data


@router.get("/forecast", response_model=ForecastResponse)
async def forecast(
    city: str = Query(..., min_length=1, max_length=100),
    current_user: User = Depends(get_current_user),
):
    return await WeatherService().get_forecast(city)


@router.get("/history")
def history(
    skip: int = 0,
    limit: int = 20, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    limit = min(max(limit, 1), 100)
    skip = max(skip, 0)
    return WeatherRepository(db).get_history(
        current_user.id,
        skip,
        limit,
    )
