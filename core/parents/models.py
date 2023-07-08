from core.models import db
from core.app import application
from datetime import datetime
from core.models import add_user_variables

@add_user_variables()
class Parent(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    sname = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(30), nullable=True, unique=True)
    phone_no = db.Column(db.String(13), nullable=False, unique=True)
    id_number = db.Column(db.Integer, nullable=False, unique=True)
    occupation = db.Column(db.String(15), nullable=True)
    residence = db.Column(db.String(15), nullable=False)
    
# EventListeners
from core.models import event_listener

db.event.listen(Parent, "before_insert", event_listener.rename_user_profile)
db.event.listen(Parent, "before_update", event_listener.rename_user_profile)

db.event.listen(Parent, "before_insert", event_listener.hash_password)
db.event.listen(Parent, "before_update", event_listener.hash_password)

db.event.listen(Parent, "before_delete", event_listener.delete_user_profile)
