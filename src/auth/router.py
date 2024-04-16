from fastapi import APIRouter, BackgroundTasks

from src.auth.service import get_check_account_service
from src.auth.utils import generate_token_invate

auth_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])


@auth_router.get("/check_account/{account}")
async def get_check_account(account: str):
    check_account = await get_check_account_service(account)
    if not check_account:
        invite_token = generate_token_invate()
