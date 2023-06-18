from fastapi import APIRouter
from .v1.router import v1_router

# Initialize api router
api_router = APIRouter(
    prefix='/api',
    tags=['api']
)

# include v1 routes
api_router.include_router(
    router=v1_router
)
