from fastapi import HTTPException
from sqlalchemy import func, select

from src.database.database import async_session_maker
from src.models import StructAdmPositions
from src.schemas.division import AddNewDivisionSchema, AddNewPositionShema
from src.services.manage_employee import check_position
from src.utils.jwt import get_user_from_token


async def add_new_divsion_service(data: AddNewDivisionSchema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        ceo = await check_ceo_exist()
        if ceo:
            async with async_session_maker() as session:
                stmt = select(func.count()).select_from(StructAdmPositions)
                count_divs = (await session.execute(stmt)).scalar()
                new_div = StructAdmPositions(
                    id=count_divs + 1,
                    note=data.division_title,
                    parent=ceo,
                )
                session.add(new_div)
                await session.commit()
        else:
            async with async_session_maker() as session:
                new_ceo = StructAdmPositions(id=1, note="CEO")
                session.add(new_ceo)
                await session.flush()
                new_div = StructAdmPositions(id=2, note=data.division_title, parent=new_ceo)
                session.add(new_div)
                await session.commit()
        return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )


async def check_ceo_exist():
    async with async_session_maker() as session:
        stmt = select(StructAdmPositions).filter_by(note="CEO")
        query = await session.execute(stmt)
        ceo_existed = query.scalar()
        if ceo_existed:
            return ceo_existed
        return False


async def add_new_position_service(data: AddNewPositionShema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        await check_position(data.new_position)
        return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )
