'''define the table of the database'''

from mongoengine import Document, StringField

'''table for user details'''
class User(Document):
    username = StringField(required=True, unique=True)
    hashed_password = StringField(required=True)
    role = StringField(required=True, choices=["admin", "user"])

'''table for projects details'''
class Project(Document):
    name = StringField(required=True)
    description = StringField()
