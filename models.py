from mongoengine import connect, Document, EmbeddedDocument, ListField, DateTimeField, StringField, ObjectIdField
from datetime import datetime
from dotenv import load_dotenv
import random
import string
import os

load_dotenv('.env')

connect(host=os.environ.get('MONGODB_URI'))

class Account(EmbeddedDocument):
    id = ObjectIdField(primary_key=True)
    name = StringField(required=True)
    category = StringField(required=True)
    password = StringField(required=True)
    account_note = StringField()

class Note(EmbeddedDocument):
    id = ObjectIdField(primary_key=True)
    title = StringField(required=True)
    category = StringField(required=True)
    note = StringField()

class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    date_added = DateTimeField(default=datetime.utcnow)
    status = StringField(default='active')
    accounts = ListField(EmbeddedDocument(Account))
    notes = ListField(EmbeddedDocument(Note))

class PasswordGenerator:
    def generate_password(self, character_choice, length):
        pass
