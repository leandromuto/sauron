import os
from pymongo import MongoClient
from dotenv import load_dotenv

def get_database():
    load_dotenv()

    client = MongoClient(os.environ.get("MONGO_URI")) # connect to cluster
    database = client.scout # select the database

    return database

def get_collection(name):
    return get_database().get_collection(name)

if __name__ == "__main__":
    db = get_database()
