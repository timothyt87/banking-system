from pydantic import BaseModel
from pydantic import Field

"""
:var branch_name 
    - hanya boleh mengandung Alpha, Numeric, Underscore 
    - ^[a-zA-Z0-9_]+$

:var branch_code 
    - hanya boleh mengandung angka
    - harus 4 digit

:var branch_abbr_code 
    - harus di awali dengan huruf
    - hanya boleh di isi dengan huruf capital
    - tidak melebihi 4 huruf. 
    - ^[A-Z][A-Z0-9]+$
:var branch_address
    - hanya boleh mengandung Alpha, Numeric, Underscore 
    - - ^[a-zA-Z0-9_]+$
"""


class CreateNewBranch(BaseModel):
    branch_name: str  # = Field(pattern=r'^[a-zA-Z0-9_]+$')
    branch_code: str  # = Field(min_length=4, max_length=4, pattern=r'^[1-9][0-9]+$')
    branch_abbr_code: str  # = Field(min_length=3, max_length=4)
    branch_address: str  # = Field(pattern=r'^[a-zA-Z0-9_]+$')
    branch_location_code: str  # = Field(pattern=[0-9])
    branch_phone_number: str

    class Config:
        schema_extra = {
            "examples": [
                {
                    "branch_abbr_code": "PAM",
                    "branch_code": "0001",
                    "branch_location_code": "36.74.06.1001.0001",
                    "branch_address": "Jl. Raya Pamulang Blok SH 21 No.17-18 Tangerang, Banten, Indonesia 15417",
                    "branch_name": "KCP Pamulang",
                    "branch_phone_number": "(021) 7432427-28"
                }
            ]
        }


class NewBranchCreated(BaseModel):
    status_code: int
    message: str


create_new_branch_responses = {
    200: {
        "description": "Response when the branch is successfully created",
        "content": {
            "application/json": {
                "example": {
                    "status_code": 201,
                    "message": "64a12150b951a8e76c93258c"
                }
            },
        },
    },
    400: {
        "description": "Response when failed to create the branch, because branch already exists",
        "content": {
            "application/json": {
                "example": {
                    'status_code': 400,
                    "messages": "Branch already exists"
                }
            },
        },
    },
    403: {
        "description": "Response when failed to Authenticate the user requesting this service",
        "content": {
            "application/json": {
                "example": {
                    'status_code': 403,
                    "messages": "Unauthorized!!!"
                }
            },
        },
    }
}
