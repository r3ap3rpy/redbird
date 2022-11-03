from redbird.repos import JSONDirectoryRepo
from pydantic import BaseModel

class Inventory(BaseModel):
    id: int
    name: str
    manufacturer: str
    quantity: int

repo = JSONDirectoryRepo(path='jsons',id_field='id')

repo.add({'id':7,'name':'Meepo','manufacturer':'Asian','quantity':10})
repo.add({'id':8,'name':'Backfire','manufacturer':'EU','quantity':20})
repo.add({'id':9,'name':'Exway','manufacturer':'American','quantity':30})

for item in list(repo):
    print(item)

repo.filter_by(name='Meepo').update(quantity=33)

repo.filter_by(name='Exway').delete()

for item in list(repo):
    print(item)
