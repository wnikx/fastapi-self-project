from pydantic import BaseModel


class SignUpSchema(BaseModel):
    account: str
    invite_token: str
