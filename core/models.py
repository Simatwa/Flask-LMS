from flask_sqlalchemy import SQLAlchemy
from .app import application

db = SQLAlchemy(application)
# sqlalchemy = SQLAlchemy()

# db = sqlalchemy.init_app(application)
