from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.v1.users.schemas import PostNewUser, ResponseUserCreated
from api.v1.users.service import insert_new_user

user_router = APIRouter(
    prefix='/users',
    tags=['api', 'v1', 'users']
)


# Create new user
@user_router.post(
    path='/',
    description='Create new user',
    response_model=ResponseUserCreated
)
async def create_new_user(user: PostNewUser):
    created_user = await insert_new_user(user)

    if created_user:
        return ResponseUserCreated(
            status=status.HTTP_201_CREATED,
            message=created_user
        )
    else:
        return JSONResponse(content="User Already Exists", status_code=status.HTTP_400_BAD_REQUEST)


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
