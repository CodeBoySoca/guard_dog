from flask import Flask, render_template
from models import *

app = Flask(__name__)



@app.route('/')
def index():
    pass

@app.route('/sign-in')
def signin():
    pass

@app.route('/sign-out')
def signout():
    pass

@app.route('/registration')
def registration():
    pass

@app.route('/password-generator')
def password_generator():
    pass

@app.route('/accounts')
def accounts():
    pass

@app.route('/update/account/<account_id>')
def update_account():
    pass

@app.route('/remove/account/<account_id>')
def remove_account():
    pass

@app.route('/add/account')
def add_account():
    pass

@app.route('/notes')
def notes():
    pass

@app.route('/update/note/<note_id>')
def update_note():
    pass

@app.route('/remove/note/<note_id>')
def remove_note():
    pass

@app.route('/add/note')
def add_note():
    pass

@app.route('/settings')
def settings():
    pass

if __name__ == '__main__':
    app.run(debug=True)
