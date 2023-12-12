from fastapi import FastAPI
from api.endpoints.items_endpoint import router as router_items
import uvicorn
from configparser import ConfigParser
from api import constants

app = FastAPI()

config = ConfigParser()
config.read(constants.CONFIG_PATH)

HOST = config.get('api', 'host')
PORT = int(config.get('api', 'port'))
PREFIX = config.get('api', 'prefix')

# Include routers with injected dependencies
app.include_router(router_items, prefix=PREFIX)

if __name__ == "__main__":
    # Run the FastAPI application using the Uvicorn server
    uvicorn.run(app, host=HOST, port=PORT)