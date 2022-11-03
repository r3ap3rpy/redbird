from redbird.repos import MongoRepo

repo = MongoRepo(uri="mongodb://user:pass@localhost:27017",database='my_db',
collection='my_items')
