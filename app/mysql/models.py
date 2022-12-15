import enum
from sqlalchemy import Column, Enum, Integer, Boolean, String, Sequence, ForeignKey
from app.mysql.base import Base
from sqlalchemy.orm import relationship

class Specie(Base):
  __tablename__ = "species"
  id = Column(Integer, Sequence("spec_id_seq"), primary_key=True)
  name = Column(String(50))
  dinosaur = relationship("Dinosaur")

  def __repr__(self) -> str:
    return "<(id= '%d', name='%s')>" % (
      self.id,
      self.name,
    )

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
  specie_id = Column(Integer, ForeignKey("species.id"))
  age = Column(Integer)#a
  weight = Column(Integer)
  gender = Column(Enum(Gender))
  dangerousness = Column(Enum(Dangerousness))
  enclosure_id = Column(Integer, ForeignKey("enclosure.id"))

  def __repr__(self) -> str:
    return "<(id= '%d', name='%s', specie='%s', age='%d', weight='%d', gender='%s', dangerousness='%s', enclosure_id='%d')>" % (
      self.id,
      self.name,
      self.species,
      self.age,
      self.weight,
      self.gender,
      self.dangerousness,
      self.enclosure_id
    )

class Enclosure(Base):
  __tablename__ = "enclosure"
  id = Column(Integer, Sequence("enclosure_id_seq"), primary_key=True)
  name = Column(String(50))
  status = Column(Boolean)
  dinosaur = relationship("Dinosaur")

  def __repr__(self) -> str:
    return "<Recinto(id='%d', name='%s', status='%r')>" % (
      self.id,
      self.name,
      self.status,
    )

class OffRoad(Base):
  __tablename__ = "offroad"
  id = Column(Integer, Sequence("offroad_id_seq"), primary_key=True)
  on_route = Column(Boolean)
  n_visitors = Column(Integer)
  security_system = Column(Boolean)

  def __repr__(self) -> str:
    return "<OffRoad(id='%d', on_route='%r', n_visitors='%s', security_system='%r')>" % (
      self.id,
      self.on_route,
      self.n_visitors,
      self.security_system,
    )

class AlarmEnum(enum.Enum):
    maximum = 'maximum'
    average = 'average'
    low = 'low'
    normal = 'normal'

class Alarm(Base):
  __tablename__ = "alarm"
  status = Column(Enum(AlarmEnum), primary_key=True)

  def __repr__(self) -> str:
    return "<Alarm(status='%s')>" % (
      self.status,
    )