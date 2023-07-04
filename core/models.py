from flask_sqlalchemy import SQLAlchemy
from .app import application

# db = SQLAlchemy(application)
db = SQLAlchemy()

db.init_app(application)
