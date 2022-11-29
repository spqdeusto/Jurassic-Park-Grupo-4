from fastapi import FastAPI
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
initialize()

controller = Controllers()

""" controller.create_enclosure("pepito", True)
controller.create_specie()
controller.create_dinosaur()
controller.create_alarm()
controller.create_offroad() """

@app.post('/specie/create')
async def create_specie(body: models.Specie): 
  return controller.create_specieModel(body)

@app.post('/enclosure/create')
async def create_enclosure(body: models.Enclosure): 
  return controller.create_enclosureModel(body)

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur): 
  return controller.create_dinosaurModel(body)

@app.post('/offRoad/create')
async def create_offRoad(body: models.OffRoad): 
  return controller.create_offRoadModel(body)

@app.post('/alarm/create')
async def create_alarm(body: models.Alarm): 
  return controller.create_alarmModel(body)

@app.get('/dinosaur/get_all')
async def get_all_dinosaurs():
  return controller.get_Dinosaurs()
