from fastapi import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload

from src.database.database import async_session_maker
from src.models import Task, User
from src.schemas.task import TaskSchema
from src.utils.jwt import get_user_from_token


async def create_task(new_task_sheme: TaskSchema, token: str) -> bool:
    user = get_user_from_token(token)
    if user["role"] == "admin":
        async with async_session_maker() as session:
            new_task = Task(
                title=new_task_sheme.title,
                author_id=new_task_sheme.author_id,
                assignee_id=new_task_sheme.assignee_id,
                deadline=new_task_sheme.deadline,
                status=new_task_sheme.status,
                estimated_time=new_task_sheme.estimated_time,
            )
            session.add(new_task)

            await session.flush()
            task = (
                await session.execute(
                    select(Task)
                    .filter_by(id=new_task.id)
                    .options(selectinload(Task.observers), selectinload(Task.performers)),
                )
            ).scalar_one()

            for observer in new_task_sheme.observers:
                new_observer = (
                    await session.execute(
                        select(User).filter_by(id=observer),
                    )
                ).scalar_one()
                task.observers.append(new_observer)
            for performer in new_task_sheme.performers:
                new_performer = (
                    await session.execute(
                        select(User).filter_by(id=performer),
                    )
                ).scalar_one()
                task.performers.append(new_performer)
            await session.commit()
        return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )


async def refresh_task(task_id: int, task: TaskSchema, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        values = {
            "title": task.title,
            "deadline": task.deadline,
            "assignee_id": task.assignee_id,
            "author_id": task.author_id,
            "status": task.status,
            "estimated_time": task.estimated_time,
        }
        async with async_session_maker() as session:
            stmt = update(Task).filter_by(id=task_id).values(**values)

            await session.execute(stmt)
            updated_task = (
                await session.execute(
                    select(Task)
                    .filter_by(id=task_id)
                    .options(selectinload(Task.observers), selectinload(Task.performers)),
                )
            ).scalar_one()
            updated_task.observers.clear()
            updated_task.performers.clear()
            for observer in task.observers:
                new_observer = (
                    await session.execute(
                        select(User).filter_by(id=observer),
                    )
                ).scalar_one()
                updated_task.observers.append(new_observer)
            for performer in task.performers:
                new_performer = (
                    await session.execute(
                        select(User).filter_by(id=performer),
                    )
                ).scalar_one()
                updated_task.performers.append(new_performer)
            await session.commit()
        return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )


async def remove_task(task_id, token: str):
    user = get_user_from_token(token)
    if user["role"] == "admin":
        async with async_session_maker() as session:
            query = delete(Task).filter_by(id=task_id)
            await session.execute(query)
            return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )
