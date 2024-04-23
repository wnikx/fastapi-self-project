from fastapi import APIRouter, HTTPException, Response

from src.schemas.registration import (
    CheckEmailSchema,
    SignUpCompleteSchema,
    SignUpSchema,
)
from src.services.registration import check_validation, email_free, finalize_registration

reg_router = APIRouter(prefix="/auth/api/v1", tags=["Auth"])


@reg_router.post("/check-email")
async def check_email(email: CheckEmailSchema) -> Response:
    """A router that checks to see if an e-mail is free."""
    email_is_free = await email_free(email)
    if email_is_free:
        return Response(
            status_code=200,
            content="A confirmation e-mail has been sent to your e-mail address ",
        )
    raise HTTPException(
        status_code=409,
        detail="User with that email already exists",
    )


@reg_router.post("/sign-up")
async def sign_up(sign_up_data: SignUpSchema) -> Response:
    """The router checks for a match between the e-mail and the token that came to the e-mail."""
    is_valid = await check_validation(sign_up_data)
    if is_valid:
        return Response(content="Data is valid", status_code=200)
    raise HTTPException(detail="Incorrectly entered data", status_code=400)


@reg_router.post("/sign-up-complete")
async def sign_up_complete(sign_up_comp_data: SignUpCompleteSchema) -> Response:
    """The router completes the registration process"""
    complete_registration = await finalize_registration(sign_up_comp_data)
    if complete_registration:
        return Response(content="Registration was successful", status_code=201)
    raise HTTPException(detail="Something's gone wrong", status_code=404)
