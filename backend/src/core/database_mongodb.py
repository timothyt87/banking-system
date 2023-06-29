import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection
from motor.motor_asyncio import AsyncIOMotorDatabase
from configurations.settings import Settings
from pymongo import ASCENDING, DESCENDING, TEXT, IndexModel
from pymongo.errors import CollectionInvalid


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
        try:
            await database.create_collection(
                name="users",
                check_exists=True
            )
        except CollectionInvalid as e:
            Settings.SERVER_LOGGER.debug(e)


mongodb = MongoDbDatabaseClass()
