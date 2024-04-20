from pydantic import BaseModel, EmailStr, field_validator

from src.utils.validators import PasswordValidator


class AddNewEmployeeSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    position: str


class NewPassScheme(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def password_strength(cls, value):
        if not PasswordValidator.validate_password_strength(value):
            raise ValueError("Password must be strength")
        return value
