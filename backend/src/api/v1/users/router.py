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


# Update User
@user_router.put(
    path='/{user_id}',
    description="Update user data"
)
async def update_user_data(user_id):
    return user_id


# Delete User
@user_router.delete(
    path='/{user_id}',
    description="Delete user"
)
async def update_user_data(user_id):
    return user_id
