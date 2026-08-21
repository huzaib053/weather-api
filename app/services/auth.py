from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import UserCreate


class AuthService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register(self, data: UserCreate):
        if self.repository.get_by_email(data.email):
            raise HTTPException(400, "Email already registered")

        if self.repository.get_by_username(data.username):
            raise HTTPException(400, "Username already taken")

        user = User(
            email=data.email,
            username=data.username,
            hashed_password=hash_password(data.password),
        )
        return self.repository.create(user)

    def login(self, username: str, password: str):
        user = self.repository.get_by_username(username)

        if not user or not verify_password(password, user.hashed_password):
            return None

        return create_access_token({
            "sub": str(user.id),
            "username": user.username,
        })
