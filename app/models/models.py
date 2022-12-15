from pydantic import BaseModel

class Specie(BaseModel):
  name: str

class Dinosaur(BaseModel):
  name: str
  specie_id: int
  age: int
  weight: int
  gender: str
  dangerousness: str
  enclosure_id: int
  
class Enclosure(BaseModel):
  name: str
  status: bool
  
class OffRoad(BaseModel):
  on_route: bool
  n_visitors: int
  security_system: bool

class Alarm(BaseModel):
  status: str
