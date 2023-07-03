from fastapi import APIRouter

from .branch.router import branch_router

admin_router = APIRouter(
    prefix='/admin'
)

# Add branch route
admin_router.include_router(
    router=branch_router
)