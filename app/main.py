"""! @brief Se define la clase main."""
##
# @file main.py
#
# @brief Define las diferentes clases del parque jurasico

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Union
from app.controllers.handler import Controllers
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
import app.models.models as models


def initialize() -> None:
  # initialize database
  """! Inicializa la base de datos"""
  dbClient = DatabaseClient(gb.MYSQL_URL)
  dbClient.init_database()
  return


app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

initialize()

controller = Controllers()

if controller.get_alarm() == []:
  body=models.Alarm
  body.status = "normal"
  controller.create_alarm(body)

# CREATE METHODS

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur): 
  """! Es la funcion que crea el metodo para generar dinosaurios
  
  @param body: Dinosaur se envia los parametros que configura un dinosaurio

  @return devuelve una mensaje si o no, se ha creado el dinosaurio en la base de datos  
  """
  return controller.create_dinosaur(body)

@app.post('/specie/create')
async def create_specie(body: models.Specie): 
  """! Es la funcion que crea el metodo para generar especies
  
  @param body: Specie se envia los parametros que configuran las especie

  @return devuelve un menssaje si o no, se ha creado la especie en la base de datos  
  """
  return controller.create_specie(body)

@app.post('/enclosure/create')
async def create_enclosure(body: models.Enclosure):
  """! Es la funcion que crea el metodo para generar recintos
  
  @param body: Enclosure se envia los parametros que configuran el recinto

  @return devuelve un mensaje si o no, se ha creado el recinto en la base de datos   
  """ 
  return controller.create_enclosure(body)

@app.post('/offroad/create')
async def create_offroad(body: models.OffRoad): 
  """! Es la funcion que crea el metodo para generar todoterrenos
  
  @param body: OffRoad se envia los parametros que configuran el todoterreno

  @return devuelve un mensaje si o no, se ha creado el todoterreno en la base de datos   
  """ 
  return controller.create_offroad(body)

@app.post('/alarm/create')
async def create_alarm(body: models.Alarm): 
  """! Es la funcion que crea el metodo para generar alarmas
  
  @param body: Alarm se envia los parametros que configuran la alarma

  @return devuelve un mensaje si o no, se ha creado la alarma en la base de datos   
  """ 
  return controller.create_alarm(body)


# GET METHODS

@app.get('/dinosaur/get_all')
async def get_Dinosaurs():
  """! Es la funcion que llama a la base de datos para obtener el dinosaurio

  @return devuelve los dinosaurios de la base de datos   
  """ 
  return controller.get_dinosaurs()

@app.get('/specie/get_all')
async def get_Species():
  """! Es la funcion que llama a la base de datos para obtener las especies

  @return devuelve las especies de la base de datos   
  """ 
  return controller.get_species()

@app.get('/enclosure/get_all')
async def get_Enclosures():
  """! Es la funcion que llama a la base de datos para obtener los recintos

  @return devuelve los recintos de la base de datos   
  """ 
  return controller.get_enclosures()

@app.get('/offroad/get_all')
async def get_offroads():
  """! Es la funcion que llama a la base de datos para obtener los todoterrenos

  @return devuelve los todoterrenos de la base de datos   
  """ 
  return controller.get_offroads()

@app.get('/alarm/get')
async def get_alarm():
  """! Es la funcion que llama a la base de datos para obtener la alarma

  @return devuelve las alarmas de la base de datos   
  """ 
  return controller.get_alarm()


# UPDATE METHODS

@app.post('/dinosaur/update')
async def update_dinosaur(dinosaur_id, body: models.Dinosaur):
  """! Es la funcion que llama a la base de datos para realizar una actualizacion en un dinosaurio

  @param dinosaur_id es el indentificador de un dinosaurio
  @param body: Dinosaur contiene los nuevos atributos para la actualizacion

  @return devuelve el identificador del dinosaurio y la nueva informacion  
  """ 
  return controller.update_dinosaur(dinosaur_id, body)

@app.post('/specie/update')
async def update_specie(specie_id, body: models.Specie):
  """! Es la funcion que llama a la base de datos para realizar una actualizacion una especie

  @param specie_id es el indentificador de una especie
  @param body: Specie contiene los nuevos atributos para la actualizacion

  @return devuelve el identificador de la especie y la nueva informacion  
  """ 
  return controller.update_specie(specie_id, body)

@app.post('/enclosure/update')
async def update_enclosure(enclosure_id, body: models.Enclosure):
  """! Es la funcion que llama a la base de datos para realizar una actualizacion del recinto

  @param enclosure_id es el indentificador de un recinto
  @param body: Enclosure contiene los nuevos atributos para la actualizacion

  @return devuelve el identificador del recinto y la nueva informacion  
  """ 
  return controller.update_enclosure(enclosure_id, body)

@app.post('/offroad/update')
async def update_offroad(offroad_id, body: models.OffRoad):
  """! Es la funcion que llama a la base de datos para realizar una actualizacion del todoterreno

  @param offroad_id es el indentificador de un todoterreno
  @param body: OffRoad contiene los nuevos atributos para la actualizacion

  @return devuelve el identificador del todoterreno y la nueva informacion  
  """
  return controller.update_offroad(offroad_id, body)


# DELETE METHODS

@app.get('/dinosaur/delete/{dinosaur_id}')
async def delete_dinosaur(dinosaur_id: int):
  """! Es la funcion que llama a la base de datos para realizar una eliminacion de un dinosaurio

  @param dinosaur_id se envia el identificador del dinosaurio

  @return devuelve un "ok", para aceptar la eliminacion del usuario
  """
  return controller.delete_dinosaur(dinosaur_id)

@app.get('/specie/delete/{specie_id}')
async def delete_specie(specie_id: int):
  """! Es la funcion que llama a la base de datos para realizar una eliminacion de una especie

  @param specie_id se envia el identificador del especie

  @return devuelve un "ok", para aceptar la eliminacion de la especie
  """
  return controller.delete_specie(specie_id)

@app.get('/enclosure/delete/{enclosure_id}')
async def delete_enclosure(enclosure_id: int):
  """! Es la funcion que llama a la base de datos para realizar una eliminacion de un recinto

  @param enclosure_id se envia el identificador del recinto

  @return devuelve un "ok", para aceptar la eliminación del recinto
  """
  return controller.delete_enclosure(enclosure_id)

@app.get('/offroad/delete/{offroad_id}')
async def delete_offroad(offroad_id: int):
  """! Es la funcion que llama a la base de datos para realizar una eliminacion de un todotorreno

  @param offroad_id se envia el identificador del todotorreno

  @return devuelve un "ok", para aceptar la eliminacion del todotorreno
  """
  return controller.delete_offroad(offroad_id)