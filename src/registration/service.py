from sqlalchemy import insert, select

from src.auth.service import get_password_hash
from src.database import async_session_maker
from src.registration.models import Account, Company, Invite, User
from src.registration.schema import CheckEmailSchema, SignUpCompleteSchema, SignUpSchema


async def get_check_email_service(email: CheckEmailSchema):
    async with async_session_maker() as session:
        stmt = select(Account).filter_by(email=email.email)
        query = await session.execute(stmt)
        return query.scalar()


async def add_account_with_invite_service(email: CheckEmailSchema, invite_token: str):
    async with async_session_maker() as session:
        new_row = Invite(email=email.email, invite_token=invite_token)
        session.add(new_row)
        await session.commit()


async def check_validation_service(sign_up_data: SignUpSchema):
    async with async_session_maker() as session:
        data = sign_up_data.model_dump()
        stmt = select(Invite).filter_by(**data)
        query = await session.execute(stmt)
        return query.scalar()


async def sign_up_complete_service(data: SignUpCompleteSchema):
    async with async_session_maker() as session:
        new_company = Company(company_name=data.company_name)
        new_account = Account(email=data.email)
        session.add_all([new_company, new_account])
        await session.flush()
        new_user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            hashed_password=get_password_hash(data.password),
            company_id=new_company.id,
            email_id=new_account.id,
            role_id=1,
            position_id=1,
        )
        session.add(new_user)
        await session.commit()
    return 1
