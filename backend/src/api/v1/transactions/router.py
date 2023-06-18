from fastapi import APIRouter
from .utils import generate_trx_id

# Initialize /transactions routes
transactions_router = APIRouter(
    prefix='/transactions',
    tags=['api', 'v1', 'transactions']
)


# index route
@transactions_router.get('/')
async def index():
    return await generate_trx_id()
