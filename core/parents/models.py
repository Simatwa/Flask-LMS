from core.models import db
from core.app import application
from datetime import datetime


class Parent(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    sname = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(30), nullable=True)
    phone_no = db.Column(db.String(13), nullable=False)
    id_number = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(15), nullable=True)
    residence = db.Column(db.String(15), nullable=False)
    is_authenticated = db.Column(db.Boolean(), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=True)
    is_anonymous = db.Column(db.Boolean(), nullable=True)
    password = db.Column(db.String(40), nullable=False, default="parent")
    token = db.Column(db.String(8), nullable=True)
    lastly_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return "<Parent %r>" % self.id

    def __str__(self):
        return self.fullname

    def get_id(self):
        return "%r" % self.id

    @property
    def fullname(self):
        return f"{self.fname} {self.sname if self.sname else ''}"
