from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.models.city import City
from app.models.user import User
from app.repositories.city import CityRepository
from app.schemas.city import CityCreate, CityResponse

router = APIRouter()


@router.post(
    "",
    response_model=CityResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_city(
    data: CityCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = CityRepository(db)

    if repo.get_by_name(data.name, current_user.id):
        raise HTTPException(400, "City already saved")

    return repo.create(
        City(
            user_id=current_user.id,
            name=data.name,
            country=data.country,
            latitude=data.latitude,
            longitude=data.longitude,
        )
    )


@router.get("", response_model=list[CityResponse])
def get_cities(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return CityRepository(db).get_all(current_user.id)


@router.delete("/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_city(
    city_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repo = CityRepository(db)
    city = repo.get_by_id(city_id, current_user.id)

    if not city:
        raise HTTPException(404, "City not found")

    repo.delete(city)
