from pydantic import BaseModel, Field


class CityCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class CityResponse(BaseModel):
    id: int
    name: str
    country: str | None
    latitude: float | None
    longitude: float | None

    model_config = {"from_attributes": True}
