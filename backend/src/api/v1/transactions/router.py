from fastapi import APIRouter

# Initialize /transactions routes
transactions_router = APIRouter(
    prefix='/transactions',
    tags=['api', 'v1', 'transactions']
)


# index route
@transactions_router.get('/')
async def index():
    return "Transactions index"
