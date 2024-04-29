from sqlalchemy import func, select

from src.database.database import async_session_maker
from src.models import StructAdmPositions
from src.schemas.division import AddNewDivisionSchema
from src.utils.jwt import get_user_from_token


async def add_new_divsion_service(data: AddNewDivisionSchema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        existed = await check_exist_email(user["email"])
        if existed:
            async with async_session_maker() as session:
                stmt = select(StructAdmPositions).filter_by(email=user["email"])
                parent = (await session.execute(stmt)).scalar()
                new_div = StructAdmPositions(id=existed, note=data.division_title, parent=parent)
                session.add(new_div)
                await session.commit()
        else:
            ceo_id = await check_ceo_email()
            async with async_session_maker() as session:
                ceo_pos = StructAdmPositions(id=ceo_id, note="CEO")
                session.add(ceo_pos)
                await session.flush()
                new_div = StructAdmPositions(
                    id=1,
                    note=data.division_title,
                    parent=ceo_pos,
                )
                session.add(new_div)
                await session.commit()


async def check_exist_email(email):
    async with async_session_maker() as session:
        stmt = select(func.count()).select_from(StructAdmPositions).filter_by(email=email)
        query = await session.execute(stmt)
        position_count = query.scalar()
        if position_count:
            return position_count
        return 0


async def check_ceo_email():
    async with async_session_maker() as session:
        stmt = select(func.count()).select_from(StructAdmPositions).filter_by(note="CEO")
        query = await session.execute(stmt)
        ceo_count = query.scalar()
        return ceo_count + 1
