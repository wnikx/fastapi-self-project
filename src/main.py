from fastapi import FastAPI

from src import token_dep
from src.registration.router import reg_router

app = FastAPI()


app.include_router(reg_router)


# @app.middleware("http")
# async def authenticate(request: Request, call_next, authorization: str = Depends(security)):
#     #  token = request.headers.get("Authorization")
#     #  if not token:
#     #      raise HTTPException(status_code=401, detail="Unauthorized")
#     #  #  if not await authenticate_token(token):
#     #  #      raise HTTPException(status_code=401, detail="Invalid token")

#     response = await call_next(request)
#     return response
