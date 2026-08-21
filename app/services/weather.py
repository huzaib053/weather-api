from datetime import datetime, timezone
import httpx
from fastapi import HTTPException
from app.core.config import settings


class WeatherService:
    async def get_current_weather(self, city: str):
        response = await self._request("/weather", {"q": city})

        data = response.json()
        weather = data.get("weather", [{}])[0]
        main = data.get("main", {})
        wind = data.get("wind", {})
        system = data.get("sys", {})

        return {
            "city": data.get("name"),
            "country": system.get("country"),
            "temperature": main.get("temp"),
            "feels_like": main.get("feels_like"),
            "humidity": main.get("humidity"),
            "pressure": main.get("pressure"),
            "wind_speed": wind.get("speed"),
            "description": weather.get("description"),
            "observed_at": datetime.now(timezone.utc),
        }

    async def get_forecast(self, city: str):
        response = await self._request("/forecast", {"q": city})
        data = response.json()
        forecast = []

        for item in data.get("list", []):
            main = item.get("main", {})
            wind = item.get("wind", {})
            weather = item.get("weather", [{}])[0]

            forecast.append({
                "datetime": datetime.fromtimestamp(
                    item["dt"],
                    tz=timezone.utc,
                ),
                "temperature": main.get("temp"),
                "feels_like": main.get("feels_like"),
                "humidity": main.get("humidity"),
                "wind_speed": wind.get("speed"),
                "description": weather.get("description"),
            })

        city_data = data.get("city", {})

        return {
            "city": city_data.get("name"),
            "country": city_data.get("country"),
            "forecast": forecast,
        }

    async def _request(self, endpoint: str, params: dict):
        params.update({
            "appid": settings.WEATHER_API_KEY,
            "units": "metric",
        })

        url = f"{settings.WEATHER_API_BASE_URL}{endpoint}"

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)

        if response.status_code == 404:
            raise HTTPException(404, "City not found")

        if response.status_code != 200:
            raise HTTPException(502, "Weather provider error")

        return response
