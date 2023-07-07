from core.admin import admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_login import current_user, login_required
from flask import flash, redirect, url_for
from core.models import db
from core.teachers.models import Teacher, Subject, Stream, AcademicYear, Activity, Department


class TeacherModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True
    form_choices = {
        "gender": [
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Unisex"),
        ],
    }

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))


class SubjectModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))


class StreamModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))


class AcademicYearModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))

class ActivityModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))
        
class DepartmentModelView(ModelView):
    form_base_class = SecureForm
    page_size = 40
    can_export = True
    export_max_row = 40
    can_create = True
    can_edit = True
    can_view_details = True

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inaccessible_callback(self):
        flash("You're not authorised to access this site", "warn")
        return redirect(url_for("home"))
        
admin.add_view(TeacherModelView(Teacher, db.session, name="Teachers"))
admin.add_view(SubjectModelView(Subject, db.session, name="Subjects"))
admin.add_view(StreamModelView(Stream, db.session, name="Streams"))
admin.add_view(AcademicYearModelView(AcademicYear, db.session, name="Academic Period"))
admin.add_view(ActivityModelView(Activity,db.session, name="Activities"))
admin.add_view(DepartmentModelView(Department, db.session, name="Departments"))