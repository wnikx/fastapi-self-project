from typing import Optional

from fastapi import APIRouter, HTTPException

from src.schemas.login import LogInSchema
from src.services.verify import verify_data

login_router = APIRouter(prefix="/auth/api/v1", tags=["Log-in"])


@login_router.post("/log-in")
async def log_in(log_in_schema: LogInSchema) -> Optional[dict]:
    token = await verify_data(log_in_schema)
    if token:
        return {"token": token}
    raise HTTPException(detail="You entered incorrect data", status_code=400)
