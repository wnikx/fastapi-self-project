from fastapi import APIRouter, HTTPException, Response

from src import token_dep
from src.schemas.task import TaskSchema
from src.services.task import create_task, refresh_task, remove_task

task_rout = APIRouter(prefix="/task/api/v1", tags=["Task manage"])


@task_rout.post("/add-task")
async def add_task(new_task: TaskSchema, token: token_dep):
    task_created = await create_task(new_task, token.credentials)
    if task_created:
        return Response(content="New task added", status_code=201)
    raise HTTPException(detail="Something gone wrong", status_code=404)


@task_rout.patch("/update-task/{task_id}")
async def update_task(task_id: int, task: TaskSchema, token: token_dep):
    task_updated = await refresh_task(task_id, task, token.credentials)
    if task_updated:
        return Response(content="Task updated", status_code=200)
    raise HTTPException(detail="Something gone wrong", status_code=404)


@task_rout.delete("/delete-task/{task_id}")
async def delete_task(task_id: int, token: token_dep):
    task_deleted = await remove_task(task_id, token.credentials)
    if task_deleted:
        return Response(content="Task deleted", status_code=200)
    raise HTTPException(detail="Something gone wrong", status_code=404)
