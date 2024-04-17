from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBearer

from src.auth.jwt import create_jwt_token
from src.registration.schema import NewEmployeeSchema, SignUpCompleteSchema, SignUpSchema
from src.registration.service import (
    add_account_with_invite_service,
    check_validation_service,
    get_check_account_service,
    sign_up_complete_service,
)
from src.registration.utils import generate_token_invate

reg_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])
security = HTTPBearer()


@reg_router.get("/check_account/{account}")
async def get_check_account(account: str):
    check_account = await get_check_account_service(account)
    if not check_account:
        invite_token = generate_token_invate()
        await add_account_with_invite_service(account, invite_token)
        # return RedirectResponse("/auth/api/v1/sign-up", status_code=307)
        return {"account": account, "invite token": invite_token}
    raise HTTPException(
        status_code=409,
        detail="A company with that account already exists",
    )


@reg_router.post("/sign-up")
async def post_sign_up(sign_up_data: SignUpSchema):
    valid = await check_validation_service(sign_up_data)
    if valid:
        # return RedirectResponse("/auth/api/v1/sign-up-complete", status_code=307)
        return sign_up_data.dict()
    raise HTTPException(detail="Incorrectly entered data", status_code=400)


@reg_router.post("/sign-up-complete")
async def post_sign_up_complete(sign_up_comp_data: SignUpCompleteSchema):
    complete = await sign_up_complete_service(sign_up_comp_data)
    if complete:
        data = sign_up_comp_data.dict()
        return {"token": create_jwt_token({"name": data["first_name"], "pass": data["password"]})}
    raise HTTPException(detail="Something's gone wrong", status_code=404)


@reg_router.post("/add_new_employee")
async def add_new_employee(data: NewEmployeeSchema, authorization: str = Depends(security)):
    pass


# # защищенный роут для получения информации о пользователе
# @app.get("/about_me")
# async def about_me(
#     authorization: str = Depends(security),
# ):
#     current_user = get_user_from_token(authorization.credentials)
#     user = get_user(current_user)
#     if user:
#         return user
#     return {"error": "User not found"}
