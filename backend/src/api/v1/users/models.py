from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    nomor_rekening: str
    nik: str
    balance: float = 0.0
    api_token: str | None = None
