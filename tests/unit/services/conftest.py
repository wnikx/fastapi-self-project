import pytest
from sqlalchemy import insert, text

from src.models import User


@pytest.fixture(scope="session")
async def delete_user(async_session_maker):
    sql = text("TRUNCATE public.user RESTART IDENTITY CASCADE;")

    async def _clean_users():
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_users


@pytest.fixture(scope="session")
async def add_user(async_session_maker):
    async def _add_users() -> None:
        async with async_session_maker() as session:
            await session.execute(
                insert(User).values(**faku_user_schema.model_dump()),
            )
            await session.commit()

    return _add_users
