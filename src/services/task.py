from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from src import token_dep
from src.database.database import async_session_maker
from src.models import Task, User
from src.schemas.task import TaskSchema
from src.utils.jwt import get_user_from_token


async def create_new_task(new_task_sheme: TaskSchema, token: token_dep):
    user = get_user_from_token(token.credentials)
    if user["role"] == "admin":
        async with async_session_maker() as session:
            stmt = select(User).filter_by(email=new_task_sheme.author)
            stmt_2 = select(User).filter_by(email=new_task_sheme.assignee)
            query = await session.execute(stmt)
            query_2 = await session.execute(stmt_2)
            author = query.scalar()
            assignee = query_2.scalar()
            new_task = Task(
                title=new_task_sheme.title,
                author_id=author.id,
                assignee_id=assignee.id,
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
                        select(User).filter_by(email=observer),
                    )
                ).scalar_one()
                task.observers.append(new_observer)
            for performer in new_task_sheme.performers:
                new_performer = (
                    await session.execute(
                        select(User).filter_by(email=performer),
                    )
                ).scalar_one()
                task.performers.append(new_performer)
            await session.commit()
        return True
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )


async def refresh_task(task_id: int, task: TaskSchema, token: token_dep):
    user = get_user_from_token(token.credentials)
    if user["role"] == "admin":
        values = task.model_dump()
        async with async_session_maker() as session:
            stmt = update(Task).filter_by(id=task_id).values(**values)
            await session.execute(stmt)
            await session.commit()
    return True
