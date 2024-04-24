import pytest
from sqlalchemy import insert, text

from src.models import Invite
from tests.fakes import fake_sign_up_schema


@pytest.fixture(scope="session")
async def add_invite_token(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            invite_token = fake_sign_up_schema.model_dump()
            stmt = insert(Invite).values(**invite_token)
            await session.execute(stmt)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def delete_invite_token(async_session_maker):
    sql = text("TRUNCATE public.invite RESTART IDENTITY CASCADE;")

    async def _clean_rows() -> None:
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_rows
