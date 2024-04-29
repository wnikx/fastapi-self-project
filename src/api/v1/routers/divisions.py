from fastapi import APIRouter, Response

from src import token_dep
from src.schemas.division import AddNewDivisionSchema
from src.services.division import add_new_divsion_service

division_router = APIRouter(prefix="/division/api/v1", tags=["Division manage"])


@division_router.post("/add-new-division")
async def add_new_division(data: AddNewDivisionSchema, token: token_dep):
    created_new_division = await add_new_divsion_service(data, token.credentials)
    if created_new_division:
        return Response(status_code=200)
