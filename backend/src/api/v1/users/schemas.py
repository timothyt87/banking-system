from pydantic import BaseModel, EmailStr
from bson import BSON


class PostNewUser(BaseModel):
    nik: str
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr
    opening_balance: float


class ResponseUserCreatedDetail(BaseModel):
    _id: BSON
    nik: str
    first_name: str
    last_name: str
    username: str
    balance: float


class ResponseUserCreated(BaseModel):
    status: int
    message: ResponseUserCreatedDetail
