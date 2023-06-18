import datetime

from fastapi import APIRouter
from .utils import generate_trx_id

# Initialize /transactions routes
transactions_router = APIRouter(
    prefix='/transactions',
    tags=['api', 'v1', 'transactions']
)


# get all transactions
@transactions_router.get('/')
async def index():
    return await generate_trx_id()


# Create new transactions
@transactions_router.post(
    path="/",
    description="Transfer fund to another account"
)
async def transfer_fund(
        sender_account_number: int,
        recipient_account_number: int,
        amount: int
):
    trx_fee: int = 6500
    total_fund_deduct = amount + trx_fee
    return {
        "trx_id": await generate_trx_id(),
        "trx_timestamp": datetime.datetime.now(),
        "sender_account_number": sender_account_number,
        "recipient_account_number": recipient_account_number,
        "amount": amount,
        "trx_fee": trx_fee,
        "total_fund_deduct": total_fund_deduct,
        "transfer_method": "immediate"
    }
