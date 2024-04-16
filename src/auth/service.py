from sqlalchemy import select

from src.auth.models import Account
from src.database import async_session_maker


async def get_check_account_service(account: str):
    async with async_session_maker() as session:
        stmt = select(Account).filter_by(account_name=account)
        query = await session.execute(stmt)
        return query.scalar()
