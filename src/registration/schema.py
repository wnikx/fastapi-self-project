from pydantic import BaseModel


class SignUpSchema(BaseModel):
    account_name: str
    invite_token: str


class SignUpCompleteSchema(BaseModel):
    account: str
    password: str
    first_name: str
    last_name: str
    company_name: str
