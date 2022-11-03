from redbird.repos import MongoRepo
from pydantic import BaseModel

class MyItem(BaseModel):
    id: int
    name: str
    quantity: int

repo = MongoRepo(uri="mongodb://user:pass@localhost:27017",database='my_db',
collection='my_items',model=MyItem)