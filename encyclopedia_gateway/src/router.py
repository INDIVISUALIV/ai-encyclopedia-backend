from fastapi import FastAPI

from src.routers.temp import router as temp_router

app = FastAPI()

app.include_router(temp_router)
