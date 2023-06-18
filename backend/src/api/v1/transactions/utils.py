import uuid
from uuid import UUID


async def generate_trx_id() -> UUID:
    trx_id = uuid.uuid4()
    return trx_id
