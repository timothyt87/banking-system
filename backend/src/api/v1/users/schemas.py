from pydantic import BaseModel


class PostNewUser(BaseModel):
    username: str
    password: str
    age: int

