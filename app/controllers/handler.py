import app.models.models as models
import app.mysql.models as mysql_models
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
from sqlalchemy.orm import Session


class Controllers:
  def __init__(self) -> None:
    pass
  
  def create_enclosure(self, name, status):
    """
    Creates new user in  the database
    """
    body_row = mysql_models.Enclosure(name=name, status=status)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

  def create_specie(self):
    body_row = mysql_models.Dinosaur(name="T-Rex")
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()


  def create_dinosaur(self):
    body_row = mysql_models.Dinosaur(name="Toby", species=1, age= 16, weight = 100, gender = "male", dangerousness = "peaceful", enclosure_id = 1)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def create_offroad(self):
    """
    Creates new user in  the database
    """
    body_row = mysql_models.OffRoad(on_route = True, n_visitors = 100, security_system= False)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

  def create_alarm(self):
    """
    Creates new user in  the database
    """
    body_row = mysql_models.Alarm(status = "maximum")
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

    #-------
  
  def create_specieModel(self, body: models.Specie):
    body_row = mysql_models.Species(name = body.name)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

  def create_enclosureModel(self, body: models.Enclosure):
    body_row = mysql_models.Enclosure(name = body.name, status = body.status)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

  def create_dinosaurModel(self, body: models.Dinosaur):
    body_row = mysql_models.Dinosaur(name=body.name, specie_id=body.specie_id, age= body.weight, weight = body.weight, gender = body.gender, dangerousness = body.dangerousness, enclosure_id = body.encosure_id)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}

  def create_offRoadModel(self, body: models.OffRoad):
    body_row = mysql_models.OffRoad(on_route = body.on_route, n_visitors = body.n_visitors, security_system = body.security_system)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()

    return {"status": "ok"}

  def create_alarmModel(self, body: models.Alarm):
    body_row = mysql_models.Alarm(status = body.status)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()

    return {"status": "ok"}

  

  
