from fastapi import APIRouter, HTTPException, Response

from src import token_dep
from src.schemas.employee import AddNewEmployeeSchema, NewPassScheme
from src.services.manage_employee import add_new_employee_service, add_new_password

employee_router = APIRouter(prefix="/employee/api/v1", tags=["Employee manage"])


@employee_router.post("/add-new-employee")
async def add_new_employee(data: AddNewEmployeeSchema, token: token_dep):
    create_new_employee = await add_new_employee_service(data, token.credentials)
    if create_new_employee:
        return Response(
            content="A link was sent to the email with the end of registration",
            status_code=200,
        )


@employee_router.post("/add-new-employee-complete/{token}")
async def add_new_employee_complete(token: str, new_pass: NewPassScheme):
    new_password = await add_new_password(new_pass.password, token)
    if new_password is True:
        return Response(content="Registration is complete", status_code=200)
