from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth/api/v1")


@auth_router.get("/check_account/{account}")
async def get_check_account(account: str):
    pass
