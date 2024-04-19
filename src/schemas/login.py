from pydantic import BaseModel, EmailStr


class LogInSchema(BaseModel):
    email: EmailStr
    password: str
