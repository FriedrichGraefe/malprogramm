from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from malprogramm import models

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

from malprogramm import views
