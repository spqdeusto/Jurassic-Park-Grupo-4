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

  def create_dinosaur(self):
    body_row = mysql_models.Dinosaur(name="Toby", species="dilophosaurus", age= 16, weight = 100, gender = "male", dangerousness = "peaceful", enclosure_id = 1)
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}