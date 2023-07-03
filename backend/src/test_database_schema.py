import random
import secrets
import string
import asyncio
import time
from datetime import datetime

from core.database_mongodb import mongodb
from configurations.settings import Settings
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient, AsyncIOMotorDatabase
from passlib.hash import bcrypt

from faker import Faker

# Set Faker Locale to Indonesia
fake = Faker('id_ID')


def __create_account_number() -> str:
    return ''.join(secrets.choice(string.digits) for i in range(12))


def __create_nik_number() -> str:
    return ''.join(secrets.choice(string.digits) for i in range(18))


def __create_pin_number() -> str:
    return ''.join(secrets.choice(string.digits) for i in range(6))


def __hash_password(password: str):
    hash = bcrypt.hash(password)
    return hash


dummy_user_data = []


def create_user():
    for x in range(0, 100):
        nama_depan = fake.first_name()
        nama_belakang = fake.last_name()
        email = fake.ascii_free_email()
        username = nama_depan + nama_belakang + str(random.randint(0, 99))
        nomor_telepon = fake.phone_number()
        tanggal_lahir = fake.date_of_birth().strftime("%B %d, %Y")
        tempat_lahir = fake.city_name()
        alamat = fake.address()

        user_data: dict = {
            'nik': __create_nik_number(),
            'nama_depan': nama_depan,
            'nama_belakang': nama_belakang,
            'email': email,
            'username': username,
            'password': __hash_password('P@ssw0rd'),
            'phone_number': nomor_telepon,
            'tanggal_lahir': tanggal_lahir,
            'tempat_lahir': tempat_lahir,
            'alamat': alamat
        }
        dummy_user_data.append(user_data)


async def get_collection(collection_name: str):
    conn: AsyncIOMotorClient = mongodb.get_connection()
    database: AsyncIOMotorDatabase = conn[Settings.DATABASE_NAME]
    collections = database[collection_name]
    return collections


async def insert_data_to_database(data):
    user_collections = await get_collection('users')
    user_id = await user_collections.update_one(
        {"nik": data.get('nik')},
        {"$setOnInsert": data},
        upsert=True
    )
    user_id = user_id.upserted_id

    account_collections = await get_collection('accounts')
    number_of_account = random.randrange(1, 10)

    for num_of_account in range(1, number_of_account):
        print(user_id)
        await account_collections.insert_one(
            {
                "parent_id_ref": user_id,
                "nomor_rekening": __create_account_number(),
                "balance": random.randrange(0, 999999999),
                "created_at": datetime.now(),
                'pin_number': __create_pin_number(),
                "is_active": True
            }
        )


async def main():
    create_user()
    for data in dummy_user_data:
        await asyncio.create_task(insert_data_to_database(data))


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(end_time - start_time)
