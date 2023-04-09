import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/test_database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie the database with this flask application

def main():
    db.create_all() # This will create table based on what are inside models.py file

if __name__ == "__main__":
    with app.app_context():
        main()
