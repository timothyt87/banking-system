from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.router import api_router
import uvicorn
import pathlib
import logging

from configurations.settings import settings

# Initialize FastAPI
app = FastAPI()

# include api router
app.include_router(
    router=api_router
)


@app.get('/')
async def index():
    return settings.SERVER_BASE_PATH


# define things to run on startup
@app.on_event('startup')
async def startup_events():
    settings.SERVER_BASE_PATH = pathlib.Path(__file__).parent.resolve()


if __name__ == '__main__':
    # Define Uvicorn Server Settings
    server_settings = {
        'app': 'server:app',
        'host': settings.SERVER_HOST,
        'port': settings.SERVER_PORT,
        'server_header': False,
        'reload': True
    }
    uvicorn.run(**server_settings)
