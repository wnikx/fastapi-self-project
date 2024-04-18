from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.models import Base
from src.registration.models import (
    Account,
    Company,
    Invite,
    Position,
    User,
)

__all__ = [
    "Base",
    "Account",
    "Company",
    "Position",
    "User",
    "Account",
    "Invite",
]

security = HTTPBearer()

token_dep = Annotated[HTTPAuthorizationCredentials, Depends(security)]
