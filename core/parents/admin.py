from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_login import current_user
from flask import url_for, redirect

from ..admin import admin
from ..models import db

from .models import Parents


class ParentsModelView(ModelView):
    can_create = True
    can_edit = True
    can_export = True
    page_size = 60
    max_export_size = 60
    form_base_class = SecureForm

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        else:
            abort(401)

    def unaccessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


admin.add_view(ParentsModelView(Parents, db.session))
