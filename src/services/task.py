from fastapi import HTTPException
from sqlalchemy import select

from src import token_dep
from src.database.database import async_session_maker
from src.models import Task, User
from src.schemas.task import TaskSchema
from src.utils.jwt import get_user_from_token


async def create_new_task(new_task: TaskSchema, token: token_dep):
    user = get_user_from_token(token.credentials)
    if user["role"] == "admin":
        async with async_session_maker() as session:
            stmt = select(User).filter_by(email=new_task.author)
            stmt_2 = select(User).filter_by(email=new_task.assignee)
            query = await session.execute(stmt)
            query_2 = await session.execute(stmt_2)
            author = query.scalar()
            assignee = query_2.scalar()
            new_task = Task(
                title=new_task.title,
                author_id=author.id,
                assignee_id=assignee.id,
                deadline=new_task.deadline,
                status=new_task.status,
                estimated_time=new_task.estimated_time,
            )
            for observer in new_task.observers:
                new_observer = (
                    await session.execute(User).filter_by(email=observer.email).scalar_one()
                )
                new_task.observers.append(new_observer)
            for performer in new_task.performers:
                new_performer = (
                    await session.query(User).filter_by(email=performer.email).scalar_one()
                )
                new_task.performers.append(new_performer)
            session.add(new_task)
            await session.commit()
    raise HTTPException(
        detail="You do not have sufficient rights to use this resource",
        status_code=403,
    )
