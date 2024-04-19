from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings
from src.models.base import Base

async_engine = create_async_engine(settings.DB_URL, echo=False)
async_session_maker = async_sessionmaker(bind=async_engine)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
