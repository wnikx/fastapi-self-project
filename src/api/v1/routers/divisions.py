from fastapi import APIRouter, Response

from src import token_dep
from src.schemas.division import AddNewDivisionSchema, AddNewPositionShema, AddNewSupervisor
from src.services.division import (
    add_new_divsion_service,
    add_new_position_service,
    add_supervisor_service,
    change_division_name_service,
    change_position_service,
    delete_position_sevice,
)

division_router = APIRouter(prefix="/division/api/v1", tags=["Division manage"])


@division_router.post("/add-new-division")
async def add_new_division(data: AddNewDivisionSchema, token: token_dep):
    created_new_division = await add_new_divsion_service(data, token.credentials)
    if created_new_division:
        return Response(status_code=200)


@division_router.post("/add-new-position")
async def add_new_position(data: AddNewPositionShema, token: token_dep):
    created_new_position = await add_new_position_service(data, token.credentials)
    if created_new_position:
        return Response(status_code=200)


@division_router.patch("/change-position/{position_id}")
async def change_position(position_id: int, data: AddNewPositionShema, token: token_dep):
    changed_position = await change_position_service(position_id, data, token.credentials)
    if changed_position:
        return Response(status_code=200)


@division_router.delete("/delete-position/{position_id}")
async def delete_position(position_id: int, token: token_dep):
    position_deleted = await delete_position_sevice(position_id, token.credentials)
    if position_deleted:
        return Response(status_code=200)


@division_router.post("/add-supervisor/{division_id}")
async def add_supervisor(division_id: int, data: AddNewSupervisor, token: token_dep):
    created_new_supervisor = await add_supervisor_service(
        division_id,
        data,
        token.credentials,
    )
    if created_new_supervisor:
        return Response(status_code=200)


@division_router.patch("/change-division-name/{division_id}")
async def change_division_name(division_id: int, data: AddNewDivisionSchema, token: token_dep):
    division_name_changed = await change_division_name_service(division_id, data, token.credentials)
    if division_name_changed:
        return Response(status_code=200)
