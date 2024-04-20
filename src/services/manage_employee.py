from fastapi import HTTPException
from sqlalchemy import select

from src.database.database import async_session_maker
from src.models import Account, Invite, Position, User
from src.schemas.employee import AddNewEmployeeSchema
from src.utils.hash_pass import get_password_hash
from src.utils.invite_token import generate_token_invate
from src.utils.jwt import get_user_from_token


async def add_new_employee_service(data: AddNewEmployeeSchema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        position_id = await check_position(data.position)
        new_user = await create_new_user(user, data, position_id)
        async with async_session_maker() as session:
            new_token = generate_token_invate()
            new_invite = Invite(email=data.email, invite_token=new_token)
            new_account = Account(email=data.email)
            session.add_all([new_invite, new_account])
            await session.flush()
            await session.commit()
            print(f"http://127.0.0.1:8000/add-new-employee-complete/{new_token}")
        return True
    raise HTTPException("You do not have sufficient rights to use this resource", status_code=403)


async def create_new_user(user, data, position_id):
    async with async_session_maker() as session:
        stmt = select(User).filter_by(email=user["email"])
        query = await session.execute(stmt)
        company = query.scalar().company_id
        new_user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            hashed_password=get_password_hash(f"{data.first_name + data.last_name}"),
            company_id=company,
            email=data.email,
            role_id=2,
            position_id=position_id,
        )
        session.add(new_user)
        await session.flush()
        await session.commit()


async def check_position(position):
    async with async_session_maker() as session:
        stmt = select(Position).filter_by(position_title=position)
        query = await session.execute(stmt)
        position_exists = query.scalar()
        if position_exists:
            return position_exists.id
        new_position = Position(position_title=position)
        query = await session.execute(stmt)
        session.add(new_position)
        await session.flush()
        await session.commit()
        return new_position.id
