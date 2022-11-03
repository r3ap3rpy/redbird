from redbird.repos import CSVFileRepo
from pydantic import BaseModel

class CSVDemo(BaseModel):
    name:str
    age: int
    height: int
repo = CSVFileRepo(filename="test.csv",model=CSVDemo)
