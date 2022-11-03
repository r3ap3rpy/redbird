from redbird.repos import MemoryRepo
from pydantic import BaseModel

class BaseAppModel(BaseModel):
    name: str
    age: int
    height: int

repo = MemoryRepo(model = BaseAppModel)

repo.add({'name':'Daniel','age':31,'height':186})
repo.add(BaseAppModel(name='Florian',age=30,height=183))

for item in list(repo):
    print(item)

for item in repo.filter_by(name='Daniel'):
    print(item)

repo.filter_by(name='Florian').update(age=29)

for item in list(repo):
    print(item)

repo.filter_by(name='Daniel').delete()

for item in list(repo):
    print(item)