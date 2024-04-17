from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Form, HTTPException
from fastapi.responses import RedirectResponse

from src.auth.schema import SignUpCompleteSchema, SignUpSchema
from src.auth.service import add_account_with_invite, check_validation, get_check_account_service
from src.auth.utils import generate_token_invate

auth_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])


@auth_router.get("/check_account/{account}")
async def get_check_account(account: str):
    check_account = await get_check_account_service(account)
    if not check_account:
        invite_token = generate_token_invate()
        await add_account_with_invite(account, invite_token)
        # return RedirectResponse("/auth/api/v1/sign-up", status_code=307)
        return {"account": account, "invite token": invite_token}
    raise HTTPException(
        status_code=409,
        detail="A company with that account already exists",
    )


# @auth_router.get("/sign-up")
# async def get_sign_up():
#     return {"good": "good"}


@auth_router.post("/sign-up")
async def post_sign_up(sign_up_data: SignUpSchema):
    valid = await check_validation(sign_up_data)
    if valid:
        # return RedirectResponse("/auth/api/v1/sign-up-complete", status_code=307)
        return sign_up_data.dict()
    raise HTTPException(detail="Incorrectly entered data", status_code=400)


# @auth_router.get("/sign-up-complete")
# async def get_sign_up_complete():
#     return {"good": "good"}


@auth_router.post("/sign-up-complete")
async def post_sign_up_complete(sign_up_comp_data: SignUpCompleteSchema):
    pass
