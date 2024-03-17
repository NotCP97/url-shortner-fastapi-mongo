import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv("MONGO_CONNECTION_URL")


MongoClient = pymongo.MongoClient(mongo_url)


class MongoHandler:
    def __init__(self, db_name = "url_shortner", collection_name="url"):
        self.db = MongoClient[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: dict, id=None):
        if id:
            data["_id"] = id
        return self.collection.insert_one(data)

    def find(self, query: dict):
        return self.collection.find_one(query)

    def update(self, query: dict, data: dict):
        return self.collection.update_one(query, {"$set": data})

    def delete(self, query: dict):
        return self.collection.delete_one(query)
    
    def count(self):
        return self.collection.count_documents({})
    
    def get_real_url(self, short_url: str):
        result = self.find({"short_url": short_url})
        if result is not None:
            return result.get("real_url")
        return None