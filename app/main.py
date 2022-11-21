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

controller.create_enclosure("pepito", True)
controller.create_dinosaur()
controller.create_alarm()
controller.create_offroad()
