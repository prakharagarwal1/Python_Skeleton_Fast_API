from app.api.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_user(self, user_id: int):
          return await self.repository.get_by_id(user_id)  


    async def create_user(self, request: UserCreate):
        return await self.repository.create(
            name=request.name,
            email=request.email
        )