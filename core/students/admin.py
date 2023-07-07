from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask import abort, redirect, url_for, request
from flask_login import current_user, login_required
from flask import flash, redirect, url_for
from core.app import application
from core.models import db
from core.admin import admin
from core.students.models import Student, Class, ClassStream, Payment, Exam


class StudentModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inacessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


class ClassModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inacessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


class ClassStreamModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inacessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


class PaymentModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inacessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


class ExamModelView(ModelView):
    page_size = 50
    can_export = True
    export_max_row = 50
    can_create = True
    can_edit = True
    can_view_details = True
    form_base_class = SecureForm

    @login_required
    def is_accessible(self):
        if hasattr(current_user, "is_admin"):
            return current_user.is_admin
        else:
            return False

    def inacessible_callback(self):
        flash("You're not authorised to access that site!", "warn")
        return redirect(url_for("home"))


admin.add_view(StudentModelView(Student, db.session, name="Students"))
admin.add_view(ClassModelView(Class, db.session, name="Classes"))
admin.add_view(ClassStreamModelView(ClassStream, db.session, name="Forms"))
admin.add_view(PaymentModelView(Payment, db.session, name="Payments"))
admin.add_view(ExamModelView(Exam, db.session, name="Exams"))
