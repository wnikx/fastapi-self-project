from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr

from src.utils.enums import StatusTask


class TaskSchema(BaseModel):
    title: str
    author: EmailStr
    assignee: EmailStr
    observers: List[str] = []
    performers: List[str] = []
    deadline: datetime
    status: StatusTask
    estimated_time: int
