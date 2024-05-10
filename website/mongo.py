from pymongo import MongoClient
from django.conf import settings
from pymongo.server_api import ServerApi

def get_mongo_collection():
    client = MongoClient(settings.MONGODB_URI, server_api=ServerApi('1'))
    db = client.get_database("db_hpms")  # Replace <dbname> with your actual database name
    collection = db.get_collection("patient")  # Replace <collection_name> with your actual collection name
    return collection