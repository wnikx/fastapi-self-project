from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

token_dep = Annotated[HTTPAuthorizationCredentials, Depends(security)]
