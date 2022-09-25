from flask import Flask, Response, Request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import os

import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

secret = os.getenv("mysql_password")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{secret}@localhost/test'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

