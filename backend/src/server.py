from fastapi import FastAPI
from api.router import api_router
import uvicorn
import pathlib
import logging

from configurations.settings import Settings
from core.database_mongodb import mongodb

# Initialize FastAPI
app = FastAPI()

# include api router
app.include_router(
    router=api_router
)


@app.get('/')
async def index():
    return Settings.SERVER_BASE_PATH


# define things to run on startup
@app.on_event('startup')
async def startup_events():
    #  Set up base path for server
    Settings.SERVER_BASE_PATH = pathlib.Path(__file__).parent.resolve()

    # Setup logging
    Settings.SERVER_LOGGER = logging.getLogger("uvicorn")
    if Settings.SERVER_ENV == "dev" and Settings.SERVER_DEBUG:
        # Setup Debug Logger
        Settings.SERVER_LOGGER.setLevel("DEBUG")
    Settings.SERVER_LOGGER.info("Setting Up Server...")

    # Setup database
    Settings.SERVER_LOGGER.info("Setting Up Database...")
    await mongodb.initialize_mongodb()

    Settings.SERVER_LOGGER.debug(Settings.dict())


@app.on_event("shutdown")
async def shutdown_events():
    # Shutdown message
    Settings.SERVER_LOGGER.info("Shutting Down Server...")


if __name__ == '__main__':
    # Define Uvicorn Server Settings

    server_settings = {
        'app': 'server:app',
        'host': Settings.SERVER_HOST,
        'port': Settings.SERVER_PORT,
        'server_header': False,
        'reload': True
    }
    uvicorn.run(**server_settings)
