'''import all libraries and modules'''

from fastapi import APIRouter, Depends, HTTPException
from .models import User, Project
from .schemas import UserRegister, UserLogin, ProjectCreate
from .auth import hash_password, verify_password, create_access_token, decode_access_token
from fastapi.responses import JSONResponse

'''initialize the router'''

router = APIRouter()

'''create endpoint for user registration'''

@router.post("/users/register")
def register_user(user: UserRegister):
    if User.objects(username=user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password, role=user.role)
    new_user.save()
    return {"message": "User registered successfully"}

'''create endpoint for user login'''

@router.post("/users/login")
def login_user(user: UserLogin):
    db_user = User.objects(username=user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": access_token, "token_type": "bearer"}

'''create endpoint for fetch all projects i.e. only authenticated users can view projects'''

@router.get("/")
def get_projects(token: str):
    try:
        payload = decode_access_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    #fetch projects from MongoDB database
    projects = Project.objects.all()

    #convert MongoEngine documents to dictionaries
    project_list = [
        {"id": str(project.id), "name": project.name, "description": project.description}
        for project in projects
    ]
    return JSONResponse(content=project_list)

'''create endpoint for the creation of projects i.e only admins can create projects'''

@router.post("/projects")
def create_project(project: ProjectCreate, token: str):
    try:
        payload = decode_access_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    new_project = Project(name=project.name, description=project.description)
    new_project.save()
    return {"message": "Project created successfully"}

'''Note: Every endpoints handles invalid tokens, unauthorized access, and duplicate usernames'''