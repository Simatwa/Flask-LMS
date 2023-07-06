from flask_sqlalchemy import SQLAlchemy
from .app import application
from datetime import datetime

# from core.accounts.views import Utils

# db = SQLAlchemy(application)
db = SQLAlchemy()

db.init_app(application)


class EventListener:

    admission_start_at = 100

    @classmethod
    def insert_age(cls, mapper, connection, target):
        """Inserts age in a table"""
        year_of_birth = target.year_of_birth
        computed_age = datetime.now().year - year_of_birth
        target.age = computed_age

    @classmethod
    def insert_admission_number(cls, mapper, connection, target):
        """Inserts admission no. to student"""
        student_id = target.id
        # to be fixed
        student.admission_no = cls.admission_start_at + student_id

    @classmethod
    def insert_password(cls, mapper, connection, target):
        """Inserts user password"""
        if target.password == target.__tablename__[:-1]:
            # Hash this password
            target.password = target.fname
        target.password = target.password  # hash password


event_listener = EventListener()
