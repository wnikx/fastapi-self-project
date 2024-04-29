import pytest
from sqlalchemy import insert, text

from src.models import Position, Role, StructAdmPositions
from src.utils.jwt import create_jwt_token
from tests.fakes import fake_company, fake_data_for_token, fake_user


@pytest.fixture(scope="session")
async def add_position_and_role(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            stmt_1 = insert(Position).values({"position_title": "CEO"})
            stmt_2 = insert(Role).values({"role": "admin"})
            stmt_3 = insert(Role).values({"role": "user"})
            await session.execute(stmt_1)
            await session.execute(stmt_3)
            await session.execute(stmt_2)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def delete_all_position_and_role(async_session_maker):
    sql = text("TRUNCATE public.role RESTART IDENTITY CASCADE;")
    sql_2 = text("TRUNCATE public.position RESTART IDENTITY CASCADE;")

    async def _clean_rows() -> None:
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.execute(sql_2)
            await session.commit()

    return _clean_rows


@pytest.fixture(scope="session")
async def add_company(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            new_fake_company = fake_company
            session.add(new_fake_company)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def add_user(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            new_fake_user = fake_user
            session.add(new_fake_user)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def delete_user(async_session_maker):
    sql = text("TRUNCATE public.user RESTART IDENTITY CASCADE;")

    async def _clean_rows() -> None:
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_rows


@pytest.fixture(scope="session")
async def delete_company(async_session_maker):
    sql = text("TRUNCATE public.company RESTART IDENTITY CASCADE;")

    async def _clean_rows() -> None:
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_rows


@pytest.fixture(scope="session")
def fake_token():
    token = create_jwt_token(fake_data_for_token)
    return token


@pytest.fixture(scope="session")
async def add_ceo_position(async_session_maker):
    async def _add_row() -> None:
        async with async_session_maker() as session:
            fake_ceo_position = StructAdmPositions(id=1, note="CEO")
            session.add(fake_ceo_position)
            await session.commit()

    return _add_row


@pytest.fixture(scope="session")
async def delete_ceo_position(async_session_maker):
    sql = text("TRUNCATE public.struct_adm_positions RESTART IDENTITY CASCADE;")

    async def _clean_rows() -> None:
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_rows
