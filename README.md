# Weather Backend MVP

FastAPI + MySQL + SQLAlchemy + Alembic + JWT + OpenWeatherMap.

## Setup

1. Create the database:
   CREATE DATABASE weather_db;

2. Install:
   pip install -r requirements.txt

3. Edit `.env` with your MySQL password and OpenWeatherMap API key.

4. Run:
   alembic upgrade head

5. Start:
   uvicorn app.main:app --reload

Swagger: http://127.0.0.1:8000/docs
