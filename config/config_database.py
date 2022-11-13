from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import aioredis
from umongo.frameworks import MotorAsyncIOInstance

MONGODB_URL = 'mongodb://localhost:27017'
client =AsyncIOMotorClient(MONGODB_URL).bookmanagementdb
client.get_io_loop = asyncio.get_running_loop
instance = MotorAsyncIOInstance(client)


