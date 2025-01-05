from pydantic import BaseModel

'''define datatypes for user-registration'''
class UserRegister(BaseModel):
    username: str
    password: str
    role: str

'''define datatypes for user-login'''
class UserLogin(BaseModel):
    username: str
    password: str

'''define datatypes for projects-detail'''
class ProjectCreate(BaseModel):
    name: str
    description: str