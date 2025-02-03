from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from os import environ
from dotenv import load_dotenv

load_dotenv()

mongo_uri = environ.get('MONGO_URL')
database ="PAG-church"
client = AsyncIOMotorClient(mongo_uri)
db = client.database


async def get_db():
    return db