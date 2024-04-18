from typing import Annotated
from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse

from src.auth.jwt import create_jwt_token
from src.main import token_dep
from src.registration.schema import (
    CheckEmailSchema,
    NewEmployeeSchema,
    SignUpCompleteSchema,
    SignUpSchema,
)
from src.registration.service import (
    add_account_with_invite_service,
    check_validation_service,
    get_check_email_service,
    sign_up_complete_service,
)
from src.registration.utils import generate_token_invate

reg_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])


@reg_router.post("/check_email/")
async def get_check_email(email: CheckEmailSchema):
    check_email = await get_check_email_service(email)
    if not check_email:
        invite_token = generate_token_invate()
        await add_account_with_invite_service(email, invite_token)
        imitation_send_email = f"Account - {email.email}, Invite token - {invite_token}"
        print(imitation_send_email)
        # return RedirectResponse("/auth/api/v1/sign-up", status_code=307)
        return Response(
            status_code=200,
            content="A confirmation e-mail has been sent to your e-mail address ",
        )
    raise HTTPException(
        status_code=409,
        detail="User with that email already exists",
    )


@reg_router.post("/sign-up")
async def post_sign_up(sign_up_data: SignUpSchema):
    valid = await check_validation_service(sign_up_data)
    if valid:
        # return RedirectResponse("/auth/api/v1/sign-up-complete", status_code=307)
        return Response(content="Data is valid", status_code=200)
    raise HTTPException(detail="Incorrectly entered data", status_code=400)


@reg_router.post("/sign-up-complete")
async def post_sign_up_complete(sign_up_comp_data: SignUpCompleteSchema):
    complete = await sign_up_complete_service(sign_up_comp_data)
    if complete:
        return Response(content="Registration was successful", status_code=201)
    raise HTTPException(detail="Something's gone wrong", status_code=404)


# @reg_router.post("/log-in")
# async def log_in():
#     pass


# @reg_router.post("/add_new_employee")
# async def add_new_employee(
#     data: NewEmployeeSchema,
#     access_token: token_dep,
# ):
#     return {"scheme": access_token.scheme, "credentials": access_token.credentials}
