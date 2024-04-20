from pydantic import BaseModel, EmailStr


class AddNewEmployeeSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    position: str
