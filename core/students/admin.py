from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask import abort, redirect, url_for, request
from flask_login import current_user
from ..app import application
from ..models import db
from ..admin import admin
from .models import Exam
from datetime import datetime


class ExamModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm
    this_year = lambda: datetime.now().year
    form_choices = {
        "stream": [
            (
                "A",
                "A",
            ),
            ("B", "B"),
            ("C", "C"),
            ("BL", "Blue"),
            ("RD", "Red"),
            ("ET", "East"),
        ],
        "form": [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
        ],
        "term": [
            (1, 1),
            (2, 2),
            (3, 3),
        ],
        "year": [
            (this_year(), this_year()),
            (this_year() - 1, this_year() - 1),
            (this_year() - 2, this_year() - 2),
        ],
    }

    def is_inaccessible(self):
        if current_user.is_athenticated:
            return any([current_user.is_admin])
        else:
            abort(401)

    def unaccessible_callback(self):
        flash("You're not authorised to access this site!")
        return redirect(url_for("home"))


admin.add_view(ExamModelView(Exam, db.session))
