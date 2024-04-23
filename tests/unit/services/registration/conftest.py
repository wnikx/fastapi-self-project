import pytest
from sqlalchemy import insert, text

from src.models import Account
from tests.fakes import fake_email_schemas


@pytest.fixture(scope="session")
async def delete_all_the_accounts(async_session_maker):
    sql = text("TRUNCATE public.account RESTART IDENTITY CASCADE;")

    async def _clean_users():
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_users


@pytest.fixture(scope="session")
async def add_account(async_session_maker):
    print("here")

    async def _add_users() -> None:
        async with async_session_maker() as session:
            for fake_email_schema in fake_email_schemas:
                await session.execute(
                    insert(Account).values(**fake_email_schema.model_dump()),
                )
            await session.commit()

    return _add_users
