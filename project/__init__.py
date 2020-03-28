# -*- coding: utf-8 -*-
# Author: Rowan
import firebase_admin
from firebase_admin import credentials
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask('project')

# call config file
config(app)

# config database
db = SQLAlchemy(app)

# config jwt
jwt = JWTManager(app)

# config mail
mail = Mail(app)

# config firebase
cred = credentials.Certificate(app.config['FIREBASE'])
default_app = firebase_admin.initialize_app(cred)

# import routes
from project.route.v1 import *
