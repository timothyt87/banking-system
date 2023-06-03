# Settings Class
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:
    SERVER_HOST: str = str(os.getenv("SERVER_HOST", '127.0.0.1'))
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))

    BASE_PATH: str = ''


settings = Settings
