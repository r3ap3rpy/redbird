from redbird.repos import MongoRepo
from pymongo import MongoClient

repo = MongoRepo(
    client=MongoClient("mongodb://user:pass@localhost:27017"),
    database='my_db',
    collection = 'my_items'
)