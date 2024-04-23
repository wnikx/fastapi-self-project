from sqlalchemy import select

from src.database.database import async_session_maker
from src.models.account import Account
from src.models.company import Company
from src.models.invite import Invite
from src.models.user import User
from src.schemas.registration import CheckEmailSchema, SignUpCompleteSchema, SignUpSchema
from src.utils.hash_pass import get_password_hash
from src.utils.invite_token import generate_token_invate


async def email_free(email: CheckEmailSchema):
    email_not_exists = await check_free_email(email)
    if email_not_exists:
        invite_token = generate_token_invate()
        await add_account_with_invite_token(email, invite_token)
        imitation_send_email = f"Account - {email.email}, Invite token - {invite_token}"
        print(imitation_send_email)
        return True
    return False


async def add_account_with_invite_token(email: CheckEmailSchema, invite_token: str):
    async with async_session_maker() as session:
        new_row = Invite(email=email.email, invite_token=invite_token)
        session.add(new_row)
        await session.commit()


async def check_validation(sign_up_data: SignUpSchema):
    async with async_session_maker() as session:
        data = sign_up_data.model_dump()
        stmt = select(Invite).filter_by(**data)
        query = await session.execute(stmt)
        return query.scalar()


async def finalize_registration(data: SignUpCompleteSchema):
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
            email=data.email,
            role_id=1,
            position_id=1,
        )
        session.add(new_user)
        await session.commit()
    return 1


async def check_free_email(email: CheckEmailSchema):
    async with async_session_maker() as session:
        stmt = select(Account).filter_by(email=email.email)
        query = await session.execute(stmt)
        email_exists = query.scalar()
        if not email_exists:
            return True
        return False
