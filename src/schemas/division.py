from pydantic import BaseModel


class AddNewDivisionSchema(BaseModel):
    division_title: str


class AddNewPositionShema(BaseModel):
    new_position: str


class AddNewSupervisor(BaseModel):
    new_supervisor: str
