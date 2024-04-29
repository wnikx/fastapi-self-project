from pydantic import BaseModel


class AddNewDivisionSchema(BaseModel):
    division_title: str
