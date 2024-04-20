from fastapi import APIRouter, HTTPException, Response

from src import token_dep
from src.schemas.employee import AddNewEmployeeSchema, NewPassScheme
from src.schemas.registration import CheckEmailSchema
from src.services.manage_employee import add_new_employee_service, add_new_password, update_email

employee_router = APIRouter(prefix="/employee/api/v1", tags=["Employee manage"])


@employee_router.post("/add-new-employee")
async def add_new_employee(data: AddNewEmployeeSchema, token: token_dep):
    created_new_employee = await add_new_employee_service(data, token.credentials)
    if created_new_employee:
        return Response(
            content="A link was sent to the email with the end of registration",
            status_code=200,
        )


@employee_router.post("/add-new-employee-complete/{token}")
async def add_new_employee_complete(token: str, new_pass: NewPassScheme):
    created_password = await add_new_password(new_pass.password, token)
    if created_password:
        return Response(content="Registration is complete", status_code=200)


@employee_router.post("/change-email")
async def change_email(new_email: CheckEmailSchema, token: token_dep):
    email_changed = await update_email(new_email, token.credentials)
    if email_changed:
        return Response(content="Email successfully changed", status_code=200)
