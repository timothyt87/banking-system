from fastapi import APIRouter

# Initialize /auth routes
auth_router = APIRouter(
    prefix='/auth',
    tags=['api', 'v1', 'auth']
)
