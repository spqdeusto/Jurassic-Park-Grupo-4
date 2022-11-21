from sqlalchemy import Column, Integer, String, Sequence
from app.mysql.base import Base
from sqlalchemy import Enum

class Species(enum.Enum):
  dilophosaurus = 'dilophosaurus'
  trex = 't-rex'
  velociraptor = 'velociraptor'
  brachiosaurus = 'brachiosaurus'
  parasaulophus = 'parasaulophus'
  galliminus = 'galliminus'
  triceratops = 'triceratops'
class Gender(enum.Enum):
  male = 'male'
  female = 'female'

class Dangerousness(enum.Enum):
  peaceful = 'peaceful'
  aggressive = 'aggressive'

class Dinosaur(Base):
  __tablename__ = "dinosaurs"
  id = Column(Integer, Sequence("dino_id_seq"), primary_key=True)
  name = Column(String(50))
  species = Column(Enum(Species))
  age = Column(Integer)
  weigth = Column(Integer)
  gender = Column(Enum(Gender))
  dangerousness = Column(Enum(Dangerousness))

  def __repr__(self) -> str:
    return "<(id= '%d', name='%s', specie='%s', age='%d', weigth='%d', gender='%s', dangerousness='%s')>" % (
      self.id,
      self.name,
      self.species,
      self.age,
      self.weigth,
      self.gender,
      self.dangerousness
    )