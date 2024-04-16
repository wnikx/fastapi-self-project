from sqlalchemy import insert, select

from src.auth.models import Account, Invite
from src.database import async_session_maker


async def get_check_account_service(account: str):
    async with async_session_maker() as session:
        stmt = select(Account).filter_by(account_name=account)
        query = await session.execute(stmt)
        return query.scalar()


async def add_account_with_invite(account: str, invite_token: str):
    async with async_session_maker() as session:
        new_row = Invite(account_name=account, invite_token=invite_token)
        session.add(new_row)
        await session.commit()
