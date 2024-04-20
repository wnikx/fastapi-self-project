from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.utils.custom_types import int_pk, str_256
from src.utils.enums import StatusTask


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int_pk]
    title: Mapped[str_256]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    deadline: Mapped[datetime]
    status: Mapped[StatusTask]
    estimated_time: Mapped[int]

    observers: Mapped[list["User"]] = relationship(
        secondary="observer_task", back_populates="task_observer"
    )
    performers: Mapped[list["User"]] = relationship()


class ObserverTask(Base):
    __tablename__ = "observer_task"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("task.id", ondelete="CASCADE"),
        primary_key=True,
    )
