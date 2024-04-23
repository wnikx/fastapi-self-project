import pytest
from sqlalchemy import insert, text

from src.models import User
from tests.fakes.services import fake_user


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
            for fake_user_schema in fake_user.fake_user_schemas:
                await session.execute(
                    insert(User).values(**fake_user_schema.model_dump()),
                )
            await session.commit()

    return _add_users
