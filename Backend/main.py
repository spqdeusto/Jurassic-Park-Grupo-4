from fastapi import FastAPI

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

engine = create_engine('direccion del servidor mysql')
Base = declarative_base()

class Dinosaurio(Base):
    __tablename__ = 'dinosaurios'

    id = Column(Integer(), primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.nombre

Session = sessionmaker(engine)
session = Session()

if __name__ == 'main':

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
