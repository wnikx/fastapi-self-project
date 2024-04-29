from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.api.v1.routers.divisions import division_router
from src.api.v1.routers.employees import employee_router
from src.api.v1.routers.login import login_router
from src.api.v1.routers.registration import reg_router
from src.api.v1.routers.task import task_rout

security = HTTPBearer()

token_dep = Annotated[HTTPAuthorizationCredentials, Depends(security)]

app = FastAPI()


app.include_router(reg_router)
app.include_router(login_router)
app.include_router(employee_router)
app.include_router(task_rout)
app.include_router(division_router)
