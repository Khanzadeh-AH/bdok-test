import os
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db


async def connect_to_mongo():
    logging.info("Connecting to database...")
    db.client = AsyncIOMotorClient(
        f'mongodb://{os.environ.get("MONGO_USERNAME")}:{os.environ.get("MONGO_PASSWORD")}@{os.environ.get("MONGO_HOST")}:{os.environ.get("MONGO_PORT")}'
    )
    logging.info('Connected to database!')


async def close_mongo_connection():
    logging.info('Closing connection to database...')
    db.client.close()
    logging.info('Disconnected from database!')
