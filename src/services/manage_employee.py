from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select, update

from src.database.database import async_session_maker
from src.models import Account, Invite, Position, User
from src.schemas.employee import AddNewEmployeeSchema, NewNameSchema
from src.schemas.registration import CheckEmailSchema
from src.services.registration import check_free_email
from src.utils.hash_pass import get_password_hash
from src.utils.invite_token import generate_token_invate
from src.utils.jwt import get_user_from_token


async def add_new_employee_service(data: AddNewEmployeeSchema, token: str) -> bool:
    user = get_user_from_token(token)
    if user["role"] == "admin":
        email_free = await check_free_email(CheckEmailSchema(email=data.email))
        if email_free:
            position_id = await check_position(data.position)
            await create_new_user(user, data, position_id)
            async with async_session_maker() as session:
                new_token = generate_token_invate()
                new_invite = Invite(email=data.email, invite_token=new_token)
                new_account = Account(email=data.email)
                session.add_all([new_invite, new_account])
                await session.flush()
                await session.commit()
                print(f"http://127.0.0.1:8000/add-new-employee-complete/{new_token}")
            return True
        raise HTTPException("This e-mail has already been registered", status_code=400)
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )


async def create_new_user(user: dict, data: AddNewEmployeeSchema, position_id: int) -> None:
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


async def check_position(position: str) -> int:
    async with async_session_maker() as session:
        stmt = select(Position).filter_by(position_title=position)
        query = await session.execute(stmt)
        position_exists = query.scalar()
        if position_exists:
            return position_exists.id
        new_position = Position(position_title=position)
        session.add(new_position)
        await session.flush()
        position_id = new_position.id
        await session.commit()
        return position_id


async def add_new_password(new_pass: str, token: str) -> bool:
    email = await check_token(token)
    async with async_session_maker() as session:
        new_pass = get_password_hash(new_pass)
        stmt = update(User).filter_by(email=email).values({"hashed_password": new_pass})
        await session.execute(stmt)
        await session.commit()
    return True


async def check_token(token: str) -> Optional[str]:
    async with async_session_maker() as session:
        stmt = select(Invite).filter_by(invite_token=token)
        query = await session.execute(stmt)
        result = query.scalar()
        if result:
            return result.email
        raise HTTPException("Invalid token", status_code=400)


async def update_email(new_email: CheckEmailSchema, token: str) -> Optional[bool]:
    email_free = await check_free_email(new_email)
    if email_free:
        user = get_user_from_token(token)
        async with async_session_maker() as session:
            stmt = update(User).filter_by(email=user["email"]).values({"email": new_email.email})
            await session.execute(stmt)
            await session.commit()
        return True
    raise HTTPException("This e-mail has already been registered", status_code=400)


async def update_name(new_name: NewNameSchema, token: str) -> bool:
    user = get_user_from_token(token)
    values = new_name.model_dump()
    async with async_session_maker() as session:
        stmt = update(User).filter_by(email=user["email"]).values(**values)
        await session.execute(stmt)
        await session.commit()
    return True
