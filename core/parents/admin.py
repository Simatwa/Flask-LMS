from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_login import current_user
from flask import url_for, redirect

from core.admin import admin
from core.models import db
from core.app import application

from core.parents.models import Parent

from flask_wtf.file import FileAllowed
from flask_admin.form import FileUploadField

class ParentModelView(ModelView):
    can_create = True
    can_edit = True
    can_export = True
    page_size = 60
    export_max_row = 60
    form_base_class = SecureForm
    can_view_details = True
    form_choices = {
        "gender": [
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Unisex"),
        ],
    }

    form_extra_fields = {
       "profile":FileUploadField(
               "Profile picture",
               base_path=application.config["USER_PROFILE_DIR"], 
               validators=[
                     FileAllowed(['jpg', 'jpeg', 'png'], message='Images only!'),
                     #FileRequired(message="Choose profile picture")
                     ]
            ),
    }
    
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        else:
            return False

    def unaccessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


admin.add_view(ParentModelView(Parent, db.session, name="Parents"))
