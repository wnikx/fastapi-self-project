import pytest
from sqlalchemy import insert, select, text

from src.models import Account, Invite, Position, Role
from tests.fakes import fake_check_validation_data, fake_data_for_invite_row, fake_email_schemas


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
    async def _add_users() -> None:
        async with async_session_maker() as session:
            await session.execute(
                insert(Account).values(**fake_email_schemas[0].model_dump()),
            )
            await session.commit()

    return _add_users


@pytest.fixture(scope="session")
async def delete_all_the_invites(async_session_maker):
    sql = text("TRUNCATE public.invite RESTART IDENTITY CASCADE;")

    async def _clean_users():
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_users


@pytest.fixture(scope="session")
async def check_invite_row(async_session_maker):
    async def _check_row() -> None:
        async with async_session_maker() as session:
            data = fake_check_validation_data.model_dump()
            row_existed = await session.execute(
                select(Invite).filter_by(**data),
            )
            if row_existed:
                row = row_existed.scalar()
                return row.email, row.invite_token

    return _check_row


@pytest.fixture(scope="session")
async def add_invite_row(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            data = fake_check_validation_data.model_dump()
            await session.execute(
                insert(Invite).values(**data),
            )
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def add_position_and_role(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            stmt_1 = insert(Position).values({"position_title": "admin"})
            stmt_2 = insert(Role).values({"role": "admin"})
            await session.execute(stmt_1)
            await session.execute(stmt_2)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def delete_all_position_and_role(async_session_maker):
    sql = text("TRUNCATE public.role RESTART IDENTITY CASCADE;")
    sql_2 = text("TRUNCATE public.position RESTART IDENTITY CASCADE;")

    async def _clean_rows():
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.execute(sql_2)
            await session.commit()

    return _clean_rows
