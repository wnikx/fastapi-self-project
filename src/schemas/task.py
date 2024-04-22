from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr

from src.utils.enums import StatusTask


class TaskSchema(BaseModel):
    title: str
    author_id: int
    assignee_id: int
    observers: List[int] = []
    performers: List[int] = []
    deadline: date
    status: StatusTask
    estimated_time: int
