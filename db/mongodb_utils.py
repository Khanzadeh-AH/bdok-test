import logging

from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db


async def connect_to_mongo():
    logging.info("Connecting to database...")
    db.client = AsyncIOMotorClient(
        'mongodb://username:password@127.0.0.1:27017/bdokdb'
    )
    logging.info('Connected to database!')


async def close_mongo_connection():
    logging.info('Closing connection to database...')
    db.client.close()
    logging.info('Disconnected from database!')
