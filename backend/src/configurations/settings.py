# Settings Class
import logging
import os
from dotenv import load_dotenv
from pydantic import BaseSettings, AnyUrl, MongoDsn
from enum import Enum

# Load .env file
load_dotenv()


class ApplicationSettings(BaseSettings):
    # Configure Server Settings
    SERVER_HOST: str = str(os.getenv("SERVER_HOST", '127.0.0.1'))
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))
    SERVER_BASE_PATH: str = ''
    SERVER_LOGGER: logging.Logger = None
    SERVER_ENV: str = os.getenv("SERVER_ENV", "prod")
    SERVER_DEBUG: bool = os.getenv("SERVER_DEBUG", False)

    # Configure Server Secrets
    SERVER_SECRETS: str = str(os.getenv("SERVER_SECRETS", 'Sup3rR4nd0m5Tr111ngzzs!!!:D_PlzChgMeee'))
    SERVER_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("SERVER_TOKEN_EXPIRE_MINUTES", 60))  # in minutes
    SERVER_JWT_ALGO: str = str(os.getenv("SERVER_JWT_ALGO", "HS256"))

    # Database configuration
    DATABASE_HOST: str = str(os.getenv("DATABASE_HOST", '127.0.0.1'))
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", 27017))  # mongodb port
    DATABASE_USERNAME: str = str(os.getenv("DATABASE_USERNAME", "mongodb"))
    DATABASE_PASSWORD: str = str(os.getenv("DATABASE_PASSWORD", "mongodb"))
    DATABASE_NAME: str = str(os.getenv("DATABASE_NAME", "application_database"))
    DATABASE_MONGO_DSN: str = f"mongodb://{DATABASE_USERNAME}:{DATABASE_PASSWORD}" \
                              f"@{DATABASE_HOST}:{DATABASE_PORT}" \
                              f"/{DATABASE_NAME}?authSource=admin"

    class Config:
        pass


Settings = ApplicationSettings()
