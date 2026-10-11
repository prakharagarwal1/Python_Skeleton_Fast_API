from app.core.database import engine, Base
from app.models.user import User


async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)