from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Union
from app.controllers.handler import Controllers
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
import app.models.models as models


def initialize() -> None:
  # initialize database
  dbClient = DatabaseClient(gb.MYSQL_URL)
  dbClient.init_database()
  return


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
		allow_headers=["*"],
    max_age=3600,
)

initialize()

controller = Controllers()

# CREATE METHODS

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur): 
  return controller.create_dinosaur(body)

@app.post('/specie/create')
async def create_specie(body: models.Specie): 
  return controller.create_specie(body)

@app.post('/enclosure/create')
async def create_enclosure(body: models.Enclosure): 
  return controller.create_enclosure(body)

@app.post('/offroad/create')
async def create_offroad(body: models.OffRoad): 
  return controller.create_offroad(body)

@app.post('/alarm/create')
async def create_alarm(body: models.Alarm): 
  return controller.create_alarm(body)

# GET METHODS

@app.get('/dinosaur/get_all')
async def get_Dinosaurs():
  return controller.get_dinosaurs()

@app.get('/specie/get_all')
async def get_Dinosaurs():
  return controller.get_species()

@app.get('/enclosure/get_all')
async def get_Enclosures():
  return controller.get_enclosures()

@app.get('/offroad/get_all')
async def get_offroads():
  return controller.get_offroads()

@app.get('/alarm/get_all')
async def get_alarms():
  return controller.get_alarms()

# UPDATE METHODS

@app.post('/dinosaur/update')
async def update_dinosaur(dinosaur_id, body: models.Dinosaur):
  return controller.update_dinosaur(dinosaur_id, body)

@app.post('/specie/update')
async def update_specie(specie_id, body: models.Dinosaur):
  return controller.update_specie(specie_id, body)

@app.post('/enclosure/update')
async def update_enclosure(enclosure_id, body: models.Dinosaur):
  return controller.update_enclosure(enclosure_id, body)

@app.post('/offroad/update')
async def update_offroad(offroad_id, body: models.Dinosaur):
  return controller.update_offroad(offroad_id, body)

@app.post('/alarm/update')
async def update_alarm(alarm_id, body: models.Dinosaur):
  return controller.update_alarm(alarm_id, body)