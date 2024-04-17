from sqlalchemy import insert, select

from src.database import async_session_maker
from src.registration.models import (
    Account,
    Company,
    Invite,
    User,
    UserAccount,
    UserCompany,
    UserPosition,
)
from src.registration.schema import SignUpCompleteSchema, SignUpSchema


async def get_check_account_service(account: str):
    async with async_session_maker() as session:
        stmt = select(Account).filter_by(account_name=account)
        query = await session.execute(stmt)
        return query.scalar()


async def add_account_with_invite_service(account: str, invite_token: str):
    async with async_session_maker() as session:
        new_row = Invite(account_name=account, invite_token=invite_token)
        session.add(new_row)
        await session.commit()


async def check_validation_service(sign_up_data: SignUpSchema):
    async with async_session_maker() as session:
        data = sign_up_data.dict()
        stmt = select(Invite).filter_by(**data)
        query = await session.execute(stmt)
        return query.scalar()


async def sign_up_complete_service(data: SignUpCompleteSchema):
    async with async_session_maker() as session:
        new_company = Company(company_name=data.company_name)
        new_user = User(first_name=data.first_name, last_name=data.last_name)
        new_account = Account(account_name=data.account)
        session.add_all([new_company, new_user, new_account])
        await session.flush()
        new_user_account = UserAccount(
            user_id=new_user.id,
            account_id=new_account.id,
            password=data.password,
        )
        new_user_company = UserCompany(user_id=new_user.id, company_id=new_company.id)
        new_user_position = UserPosition(user_id=new_user.id, position_id=1)
        session.add_all(
            [
                new_user_account,
                new_user_company,
                new_user_position,
            ],
        )
        await session.commit()
        return 1
