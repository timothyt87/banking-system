import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection
from motor.motor_asyncio import AsyncIOMotorDatabase
from configurations.settings import Settings
from pymongo import ASCENDING, DESCENDING, TEXT, IndexModel


class MongoDbDatabaseClass:
    __conn: str = None

    @classmethod
    def get_connection(cls) -> AsyncIOMotorClient:
        # Check if connection already initialize
        if cls.__conn is None:
            cls.__conn = AsyncIOMotorClient(Settings.DATABASE_MONGO_DSN)

        # return connection
        return cls.__conn

    # Initialize MongoDB Database
    @classmethod
    async def initialize_mongodb(cls):
        # Create Connection
        conn: AsyncIOMotorClient = cls.get_connection()

        # Create Database
        database: AsyncIOMotorDatabase = conn[Settings.DATABASE_NAME]

        # Create User Collections
        user_collections: AsyncIOMotorCollection = database['users']

        # Create Index for User Collections
        index_username = IndexModel([("username", TEXT)], unique=True)
        index_email = IndexModel([("email", TEXT)], unique=True)

        await user_collections.create_indexes([
            index_username,
            index_email
        ])


mongodb = MongoDbDatabaseClass()
