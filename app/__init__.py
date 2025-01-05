'''import all libraries and modules'''

from fastapi import FastAPI
from mongoengine import connect
from .routes import router

'''define function to create or initialize app'''
def create_app() -> FastAPI:
    app = FastAPI()

    #connect to MongoDB driver
    connect(host="mongodb+srv://mongoDBusername:mongoDBpassword@cluster0.qridz.mongodb.net/mongoDBdatabase?retryWrites=true&w=majority&appName=Cluster0")

    #include routes
    app.include_router(router)
    return app