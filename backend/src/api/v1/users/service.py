import secrets
import string
import bcrypt

from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient, AsyncIOMotorCollection

from configurations.settings import Settings
from core.database_mongodb import mongodb
from .models import User
from .schemas import PostNewUser


async def __create_account_number() -> str:
    return ''.join(secrets.choice(string.digits) for i in range(12))


async def __hash_password(password: str):
    # converting password to array of bytes
    bytes = password.encode('utf-8') + Settings.SERVER_SECRETS.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)

    return hash


async def get_collection(collection_name: str):
    conn: AsyncIOMotorClient = mongodb.get_connection()
    database: AsyncIOMotorDatabase = conn[Settings.DATABASE_NAME]
    collections = database[collection_name]
    return collections


async def insert_new_user(user: PostNewUser):
    user_collection: AsyncIOMotorCollection = await get_collection('users')

    user_data = User(
        **user.dict(),
        nomor_rekening=await __create_account_number(),
        balance=user.opening_balance
    )
    user_data.password = await __hash_password(user_data.password)

    _id = await user_collection.update_one(
        {
            "nik": user.nik
        },
        {"$setOnInsert": user_data.dict()},
        upsert=True
    )

    if _id:
        created_user = await user_collection.find_one(_id.upserted_id)
        return created_user
    else:
        return None
