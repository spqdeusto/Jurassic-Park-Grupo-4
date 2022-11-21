from pydantic import BaseModel
#jfdjfsj
class UserRequest(BaseModel):
  name: str
  fullname: str
  age: int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: UserRequest