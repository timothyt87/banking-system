from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.v1.users.schemas import PostNewUser, ResponseUserCreated
# from api.v1.users.service import insert_new_user

user_router = APIRouter(
    prefix='/users',
    tags=['api', 'v1', 'users']
)

