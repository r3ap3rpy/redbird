from redbird.repos import MemoryRepo
from pydantic import BaseModel
from redbird.oper import greater_equal,greater_than,less_equal,less_than,not_equal

class BaseAppModel(BaseModel):
    name: str
    age: int
    height: int

repo = MemoryRepo(model = BaseAppModel)

repo.add({'name':'Daniel','age':31,'height':186})
repo.add(BaseAppModel(name='Florian',age=30,height=183))
repo.add({'name':'Erno','age':55,'height':180})
repo.add(BaseAppModel(name='Ildiko',age=56,height=160))

for item in list(repo.filter_by(age=greater_than(40))):
    print(item)


for item in list(repo.filter_by(age=less_equal(55))):
    print(item)

for item in list(repo.filter_by(age=not_equal(56))):
    print(item)
