from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.schemas.registration import CheckEmailSchema
from src.utils.enums import StatusTask


class Task(BaseModel):
    title: str
    author: str
    assignee: list[CheckEmailSchema] = []
    observers: list[CheckEmailSchema] = []
    performers: str
    deadline: datetime
    status: StatusTask
    estimated_time: int
