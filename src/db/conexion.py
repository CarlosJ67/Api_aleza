import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
db_name = os.getenv('MONGO_DB')
collection_name = os.getenv('MONGO_COLLECTION')

# Crear cliente y colección una vez
client = MongoClient(mongo_uri)
db = client[db_name]
coleccion = db[collection_name]

def get_db_connection():
    return coleccion

def close_db_connection():
    client.close()
