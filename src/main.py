from fastapi import FastAPI

from src.registration.router import reg_router

app = FastAPI()

app.include_router(reg_router)
