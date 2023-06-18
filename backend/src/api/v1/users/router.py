from fastapi import APIRouter
from .schemas import PostNewUser

user_router = APIRouter(
    prefix='/users',
    tags=['api', 'v1', 'users']
)


# Create new user
@user_router.post(
    path='/',
    description='Create new user',
)
async def create_new_user(User: PostNewUser):
    return User
