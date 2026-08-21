from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.weather import router as weather_router
from app.api.v1.cities import router as cities_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(weather_router, prefix="/weather", tags=["Weather"])
api_router.include_router(cities_router, prefix="/cities", tags=["Cities"])
