from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr

from src.utils.enums import StatusTask


class TaskSchema(BaseModel):
    title: str
    author_id: int
    assignee_id: int
    observers: List[str] = []
    performers: List[str] = []
    deadline: date
    status: StatusTask
    estimated_time: int
