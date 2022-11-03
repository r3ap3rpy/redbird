from sqlalchemy import create_engine
from redbird.repos import SQLRepo

engine = create_engine('sqlite://')
repo = SQLRepo(engine=engine,table='my_table')