import app.models.models as models
import app.mysql.models as mysql_models
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
from sqlalchemy.orm import Session


class Controllers:
  def __init__(self) -> None:
    pass
  
  # CREATE METHODS 

  def create_dinosaur(self, body: models.Dinosaur):
    body_row = mysql_models.Dinosaur(name=body.name, specie_id=body.specie_id, age=body.age, weight=body.weight, gender=body.gender, dangerousness=body.dangerousness, enclosure_id=body.enclosure_id)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def create_specie(self, body: models.Specie):
    body_row = mysql_models.Specie(name=body.name)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def create_enclosure(self, body: models.Enclosure):
    body_row = mysql_models.Enclosure(name=body.name, status=body.status)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def create_offroad(self, body: models.OffRoad):
    body_row = mysql_models.OffRoad(on_route=body.on_route, n_visitors=body.n_visitors, security_system=body.security_system)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def create_alarm(self, body: models.Alarm):
    body_row = mysql_models.Alarm(status=body.status)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()

    return {"status": "ok"}


  # GET METHODS

  def get_dinosaurs(self):
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.Dinosaur).all()
      session.close()
      
    return response

  def get_species(self):
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.Specie).all()
      session.close()
      
    return response

  def get_enclosures(self):
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.Enclosure).all()
      session.close()
      
    return response

  def get_offroads(self):
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.OffRoad).all()
      session.close()
      
    return response
  
  def get_alarm(self):
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.Alarm).all()
      session.close()
      
    return response


  # UPDATE METHODS 

  def update_dinosaur(self, dinosaur_id, body: models.Dinosaur):
    body_row = mysql_models.Dinosaur(name=body.name, specie_id=body.specie_id, age=body.age, weight=body.weight, gender=body.gender, dangerousness=body.dangerousness, enclosure_id=body.enclosure_id)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaur: mysql_models.Dinosaur = session.query(mysql_models.Dinosaur).get(dinosaur_id)
      dinosaur.name = body.name
      dinosaur.specie_id = body.specie_id
      dinosaur.age = body.age
      dinosaur.weight = body.weight
      dinosaur.gender = body.gender
      dinosaur.dangerousness = body.dangerousness
      dinosaur.enclosure_id = body.enclosure_id
      session.dirty
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}
    
  def update_specie(self, specie_id, body: models.Specie):
    body_row = mysql_models.Specie(name = body.name)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      specie: mysql_models.Specie = session.query(mysql_models.Specie).get(specie_id)
      specie.name = body.name
      session.dirty
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def update_enclosure(self, enclosue_id, body: models.Enclosure):
    body_row = mysql_models.Enclosure(name = body.name, status = body.status)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      enclosure: mysql_models.Enclosure = session.query(mysql_models.Enclosure).get(enclosue_id)
      enclosure.name = body.name
      enclosure.status = body.status
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def update_offroad(self, offroad_id, body: models.OffRoad):
    body_row = mysql_models.OffRoad(on_route = body.on_route, n_visitors = body.n_visitors, security_system = body.security_system)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      offroad: mysql_models.OffRoad = session.query(mysql_models.OffRoad).get(offroad_id)
      offroad.on_route = body.on_route
      offroad.n_visitors = body.n_visitors
      offroad.security_system = body.security_system
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def update_alarm(self):
    db = DatabaseClient(gb.MYSQL_URL)
    alarm_status = "normal"

    with Session(db.engine) as session:
      result = session.query(mysql_models.Enclosure).filter_by(status = False).\
        join(mysql_models.Enclosure.dinosaur).filter_by(dangerousness = "aggressive").first()
      result_2 = session.query(mysql_models.OffRoad).filter_by(on_route = True).first()

      if (result != None) and (result_2 != None):
        alarm_status = "maximum"
      else:
        result_2 = session.query(mysql_models.OffRoad).filter_by(on_route = False).first()
        if (result != None) and (result_2 != None):
          alarm_status = "average"
        else:
          result = session.query(mysql_models.Enclosure).filter_by(status = False).\
            join(mysql_models.Enclosure.dinosaur).filter_by(dangerousness = "peaceful").first()
          if result != None:
            alarm_status = "low"
     
      alarm: mysql_models.Alarm = session.query(mysql_models.Alarm).first()
      alarm.status = alarm_status

      if alarm_status != "normal" and alarm_status != "low":
        for offroad in session.query(mysql_models.OffRoad).all():
          offroad.security_system = True
      else:
        for offroad in session.query(mysql_models.OffRoad).all():
          offroad.security_system = False
      
      session.commit()
      session.close()

    return {"status": "ok"}

  
  # DELETE METHODS 

  def delete_dinosaur(self, dinosaur_id):
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaur: mysql_models.Dinosaur = session.query(mysql_models.Dinosaur).get(dinosaur_id)
      session.delete(dinosaur)
      session.dirty
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}
    
  def delete_specie(self, specie_id):
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      specie: mysql_models.Specie = session.query(mysql_models.Specie).get(specie_id)
      session.delete(specie)
      session.dirty
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def delete_enclosure(self, enclosue_id):
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      enclosure: mysql_models.Enclosure = session.query(mysql_models.Enclosure).get(enclosue_id)
      session.delete(enclosure)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}

  def delete_offroad(self, offroad_id):
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      offroad: mysql_models.OffRoad = session.query(mysql_models.OffRoad).get(offroad_id)
      session.delete(offroad)
      session.commit()
      session.close()
    self.update_alarm()
    return {"status": "ok"}