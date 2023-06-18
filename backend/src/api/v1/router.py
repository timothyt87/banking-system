from fastapi import APIRouter
from .auth.router import auth_router
from .transactions.router import transactions_router

# Initialize v1 routes
v1_router = APIRouter(
    prefix='/v1',
    tags=['api', 'v1']
)

# import auth router
v1_router.include_router(
    router=auth_router
)

# import transactions router
v1_router.include_router(
    router=transactions_router
)
