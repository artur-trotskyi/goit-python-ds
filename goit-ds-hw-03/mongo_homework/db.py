import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DB_NAME")

if not mongo_uri or not db_name:
    raise ValueError("MongoDB URI or Database name not provided in the environment variables.")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client[db_name]
