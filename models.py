from mongoengine import connect, Document, EmbeddedDocument, EmbeddedDocumentField, ListField, DateTimeField, StringField, ObjectIdField
from datetime import datetime
from dotenv import load_dotenv
import random
import os

load_dotenv('.env')

connect(host=os.environ.get('MONGODB_URI'))

class Account(EmbeddedDocument):
    id = ObjectIdField(primary_key=True)
    name = StringField(required=True)
    category = StringField(required=True)
    password = StringField(required=True)
    account_note = StringField()

    def create_account():
        pass

    def update_account(email):
        pass

    def delete_account():
        pass

    def filter_account(filter):
        pass


class Note(EmbeddedDocument):
    id = ObjectIdField(primary_key=True)
    title = StringField(required=True)
    category = StringField(required=True)
    note = StringField()

    def save_note():
        pass

    def retrieve_notes():
        pass

    def retrieve_note(note_id):
        pass

    def edit_note(note_id):
        pass

    def delete_note(note_id):
        pass

class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    date_added = DateTimeField(default=datetime.utcnow)
    status = StringField(default='active')
    accounts = ListField(EmbeddedDocumentField(Account))
    notes = ListField(EmbeddedDocumentField(Note))

    @staticmethod
    def retrieve_user_account(email):
        pass

    def add_user_account():
        pass

    def update_user_account(email):
        pass

    def deactivate_user_account():
        pass

    def check_for_user_account(email):
        pass


class PasswordGenerator:
    def generate_password(self, character_choice, length):
        return ''.join([random.choice(character_choice)for _ in range(length)])
