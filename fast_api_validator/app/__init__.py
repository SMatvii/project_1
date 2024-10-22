import asyncio
from fastapi import FastAPI
from uvicorn import Server, Config

app = FastAPI()

config = Config(app=app, host="localhost", port=8080)

def main() -> None:
    server = Server(config)
    asyncio.run(server.serve())

from . import routes