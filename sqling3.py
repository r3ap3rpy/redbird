from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer,create_engine
from redbird.repos import SQLRepo

Base = declarative_base()

class Car(Base):
    __tablename__ = "my_table"
    color = Column(String, primary_key=True)
    car_type=Column(String)
    mileage = Column(Integer)

engine = create_engine('sqlite://')
repo = SQLRepo(engine=engine, model_orm=Car, reflect_model=True)