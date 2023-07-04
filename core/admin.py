from flask_admin import Admin
from .app import application

admin = Admin(application, name="Andersen HS", template_mode="bootstrap3")
