from fastapi import APIRouter
from app.models.users import  User,CreateUserRequest


router = APIRouter()

@router.get("/auth/")
async def  root(create_user_request:CreateUserRequest):
    create_user_model = User(**create_user_request.model_dump())
    return {"message": "Hello World"}
