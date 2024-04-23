import asyncio
from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings
from src.models import Base


@pytest.fixture(scope="session")
def async_engine():
    async_engine = create_async_engine(url=settings.DB_URL, echo=False, poolclass=NullPool)
    return async_engine


@pytest.fixture(scope="session")
def async_session_maker(async_engine):
    async_session_maker = async_sessionmaker(bind=async_engine)
    return async_session_maker


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_db(async_engine):
    print(settings.DB_NAME)
    assert settings.MODE == "TEST"
    async with async_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)
        await db_conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def async_session(async_session_maker):
    async with async_session_maker() as async_session:
        yield async_session


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://127.0.0.1:8000/results",
    ) as ac:
        yield ac
