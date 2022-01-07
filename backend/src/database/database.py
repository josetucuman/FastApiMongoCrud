from typing import Collection
from model.model import Todo


# Mongo driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://josegelimer:J0s3G3l1m3r@cluster0.ulp1o.mongodb.net/MongoReactDB?retryWrites=true&w=majority')
database = client.MongoReactDB
collection = database.todo



async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        document.append(Todo(**document))
    
    return todos