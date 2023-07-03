from datetime import datetime
from pydantic import BaseModel, Field


class BranchData(BaseModel):
    branch_name: str = Field(pattern=r'^[a-zA-Z0-9_]+$')
    branch_code: str = Field(min_length=4, max_length=4, pattern=r'^[1-9][0-9]+$')
    branch_abbr_code: str = Field(min_length=3, max_length=4)
    branch_address: str = Field(pattern=r'^[a-zA-Z0-9_]+$')
    branch_location_code: str = Field(pattern=[0 - 9])
    branch_created_at: datetime
    branch_updated_at: datetime | None
