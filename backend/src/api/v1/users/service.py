import secrets
import string
import bson

from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient, AsyncIOMotorCollection
from passlib.hash import bcrypt
from configurations.settings import Settings
from core.database_mongodb import mongodb
from .models import User
from .schemas import PostNewUser


async def __create_account_number() -> str:
    return ''.join(secrets.choice(string.digits) for i in range(12))


def __hash_password(password: str):
    hash = bcrypt.hash(password)
    return hash


async def get_collection(collection_name: str):
    conn: AsyncIOMotorClient = mongodb.get_connection()
    database: AsyncIOMotorDatabase = conn[Settings.DATABASE_NAME]
    collections = database[collection_name]
    return collections


async def insert_new_user(user: PostNewUser):
    user_collection: AsyncIOMotorCollection = await get_collection('users')
    account_collection: AsyncIOMotorCollection = await get_collection("accounts")

    user_data = User(
        **user.dict(),
    )
    # Hash user password
    user_data.password = await __hash_password(user_data.password)

    # Insert user data to database
    # if data exists, update the data
    _id = await user_collection.update_one(
        {
            "nik": user.nik
        },
        {"$setOnInsert": user_data.dict()},
        upsert=True
    )

    # Create User Account
    account_id = await account_collection.insert_one({
        "_id": bson.BSON(_id),
        "nomor_rekening": [await __create_account_number()],
        "balance": user_data.balance
    })

    created_user = await user_collection.find_one(_id.upserted_id)
    created_user_account = await user_collection.find_one(account_id.id, {"_id": -1, "nomor_rekening": 1, "balance": 1})

    print(created_user_account)

    created_user.nomor_rekening = created_user_account.nomor_rekening
    created_user_account.balance = created_user_account.balance

    return created_user
