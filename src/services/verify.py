from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.database.database import async_session_maker
from src.models.user import User
from src.schemas.login import LogInSchema
from src.utils.hash_pass import verify_password
from src.utils.jwt import create_jwt_token


async def verify_data(data: LogInSchema):
    async with async_session_maker() as session:
        stmt = select(User).filter_by(email=data.email).options(selectinload(User.role))
        query = await session.execute(stmt)
        account_exists = query.scalar()
        password_is_valid = verify_password(data.password, account_exists.hashed_password)
        if account_exists and password_is_valid:
            token = create_jwt_token(
                data={"email": account_exists.email, "role": account_exists.role.role.value},
            )
            return token
        return False
