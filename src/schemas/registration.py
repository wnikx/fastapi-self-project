from pydantic import BaseModel, EmailStr, field_validator

from src.utils.validators import PasswordValidator


class CheckEmailSchema(BaseModel):
    email: EmailStr


class SignUpSchema(BaseModel):
    email: EmailStr
    invite_token: str


class SignUpCompleteSchema(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    company_name: str

    @field_validator("password")
    @classmethod
    def password_strength(cls, value):
        if not PasswordValidator.validate_password_strength(value):
            raise ValueError("Password must be strength")
        return value
