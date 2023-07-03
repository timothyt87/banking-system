import secrets
import string
import bson

from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient, AsyncIOMotorCollection
from passlib.hash import bcrypt
from configurations.settings import Settings
from core.database_mongodb import mongodb
from .models import User
from .schemas import PostNewUser


