import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del .env

def get_db_connection():
    mongo_uri = os.getenv('MONGO_URI')
    db_name = os.getenv('MONGO_DB')
    collection_name = os.getenv('MONGO_COLLECTION')
    client = MongoClient(mongo_uri)
    db = client[db_name]
    coleccion = db[collection_name]
    return coleccion, client

def close_db_connection(client):
    client.close()