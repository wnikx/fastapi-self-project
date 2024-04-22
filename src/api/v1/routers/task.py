from fastapi import APIRouter, HTTPException, Response

from src import token_dep
from src.schemas.task import TaskSchema
from src.services.task import create_new_task

task_rout = APIRouter(prefix="/task/api/v1", tags=["Task manage"])


@task_rout.post("/add-new-task")
async def add_new_task(new_task: TaskSchema, token: token_dep):
    task_created = await create_new_task(new_task, token)
    if task_created:
        return Response(content="New task added", status_code=201)
    raise HTTPException(detail="Something gone wrong", status_code=404)
