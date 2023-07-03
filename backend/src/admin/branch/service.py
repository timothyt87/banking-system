import datetime

from configurations.settings import Settings
from core.database_mongodb import mongodb
from .models import BranchData


async def insert_new_branch(branch_data_payload: dict) -> str | None:
    branch_collection = await mongodb.get_collection('branch')
    branch_data_payload['branch_created_at'] = datetime.datetime.now()

    branch_data = BranchData(**branch_data_payload)

    _id = await branch_collection.update_one(
        {
            'branch_code': branch_data_payload['branch_code'],
            'branch_abbr_code': branch_data_payload['branch_abbr_code'],
            'branch_location_code': branch_data_payload['branch_location_code']
        },
        {
            "$setOnInsert": branch_data.dict()
        },
        upsert=True
    )

    if _id.upserted_id is not None:
        return str(_id.upserted_id)
    else:
        return None
