from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from redbird.repos import SQLRepo

engine = create_engine('sqlite://')
session = Session(engine)
repo = SQLRepo(engine=engine,table='my_table')