import os

from flask import Flask, render_template, request
from models import *

from flask_sqlalchemy import SQLAlchemy

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C://Users//User//cs50WPPJ_Lecture2//first//new_test.db'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:ShPyR13_@localhost:5432/test2.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://shammun:ShPyR13_13_@localhost:5432/new_test3.db' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy()
db.init_app(app)


def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
