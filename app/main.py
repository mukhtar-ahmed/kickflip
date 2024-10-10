from fastapi import FastAPI
from app.models.users import User,Base
from app.routers.auth import router

from .database import engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router=router)

@app.post('/')
async def  root():
    return {"message": 'user'}