import pymongo
from pymongo import MongoClient

# connect to cluster
client = MongoClient("mongodb+srv://admin:BT68FdbkPxfbALCm@users.ix3mr.mongodb.net/olheiro?retryWrites=true&w=majority")
# select the database
db = client.olheiro
# select the collection from database
collection = db.events

collection.insert_one({"_id": 0, "name": "test"})