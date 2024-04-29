from src.schemas.division import AddNewDivisionSchema
from src.utils.jwt import get_user_from_token


async def add_new_divsion_service(data: AddNewDivisionSchema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        pass
