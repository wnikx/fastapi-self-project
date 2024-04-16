from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import RedirectResponse

from src.auth.schema import SignUpSchema
from src.auth.service import add_account_with_invite, get_check_account_service
from src.auth.utils import generate_token_invate

auth_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])


@auth_router.get("/check_account/{account}")
async def get_check_account(account: str):
    check_account = await get_check_account_service(account)
    if not check_account:
        invite_token = generate_token_invate()
        print(f"Account: {account} - Invite Token: {invite_token}")
        await add_account_with_invite(account, invite_token)
        return RedirectResponse(f"/auth/api/v1/sign-up?account={account}", status_code=302)
    return HTTPException(
        status_code=409,
        detail="A company with that e-mail address already exists",
    )


@auth_router.post("/sign-up")
async def sign_up(sign_up: SignUpSchema):
    pass
