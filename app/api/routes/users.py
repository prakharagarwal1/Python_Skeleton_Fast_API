from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.api.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    repository = UserRepository(db)
    service = UserService(repository)

    user = await service.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


@router.post("/users", response_model=UserResponse)
async def create_user(
    request: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    repository = UserRepository(db)
    service = UserService(repository)

    return await service.create_user(request)