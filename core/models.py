from flask_sqlalchemy import SQLAlchemy
from .app import application
from datetime import datetime
import os

# from core.accounts.views import Utils

# db = SQLAlchemy(application)
db = SQLAlchemy()

db.init_app(application)

full_path = lambda filename : os.path.join(application.config["USER_PROFILE_DIR"],filename)

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
        target.password = target.password
    
    @classmethod
    def rename_user_profile(cls, mapper, connection, target):
    	"""Uniquify the profile name"""
    	current_profile = target.profile
    	new_profile = f"{target.__tablename__[:-1]}_{target.id or target.fname}_{target.profile}"
    	if current_profile:
    		os.rename(full_path(current_profile),full_path(new_profile))
    		target.profile = new_profile
    	
    @classmethod
    def delete_user_profile(cls, mapper, connection, target):
    	"""Deletes user profile"""
    	profile_path = full_path(target.profile)
    	if os.path.isfile(profile_path):
    		os.remove(profile_path)
    	
event_listener = EventListener()
