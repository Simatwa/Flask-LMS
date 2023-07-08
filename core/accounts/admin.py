from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from core.accounts import app
from core.accounts.models import SchoolAdmin
from core.models import db
from core.admin import admin
from flask_login import current_user
from flask import abort, redirect, url_for, flash
import click
from wtforms.validators import DataRequired, Email

# from core.app import application
from core.accounts.views import Utils


class AdminModelView(ModelView):
    form_base_class = SecureForm
    can_create = True
    can_edit = True
    can_view_details = True
    page_size = 60
    """
    form_excluded_columns = [
        "created_at",
        "last_updated",
        "token",
        "profile",
    ]  # Exclude forms from create/edit
    column_exclude_list = ["password", "token"]  # Exclude columns from view
    column_editable_list = [
        "fname",
        "sname",
        "index_no",
        "email",
        "is_admin",
        "is_parent",
        "is_teacher",
        "is_student",
        "is_stakeholder",
    ]
    column_searchable_list = ["fname", "sname", "index_no", "email"]
    column_filters = ["fname", "sname", "index_no", "email"]
    create_modal = False  # create modal at window view
    edit_modal = False  # edit modal at window view
    can_export = False  # Ability to export entries in csv
    export_max_row = 80

    form_choices = {
        "gender": [
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Unisex"),
        ]
    }

    form_args = {
        "fname": {
            "label": "First Name",
            "validators": [DataRequired(message="First name is required")],
        },
        "sname": {
            "label": "Second Name",
            "validators": [],
        },
        "email": {
            "label": "Email address",
            "validators": [
                DataRequired(message="Email is required"),
                Email(message="Enter valid email address"),
            ],
        },
        "gender": {
            "label": "Pick gender",
            "validators": [
                DataRequired(
                    message="Select gender",
                )
            ],
        },
        "password": {
            "label": "Enter password",
            "validators": [DataRequired(message="Password is required")],
        },
    }
    """

    def is_accessible(self):
        if current_user.is_authenticated and current_user.is_admin:
            return True
        else:
            abort(403)

    def inaccessible_callback(self):
        flash("You're not authorised to access that resource!", "warn")
        return redirect(url_for("home"))


class Cmd:
    @staticmethod
    @app.cli.command(
        "create-admin",
    )
    @click.option("--fname", prompt="Enter first name")
    @click.option(
        "--email",
        prompt="Enter email address",
    )
    @click.password_option(prompt="Enter password")
    def create_admin(fname, email, password):
        """Adds new_admin"""
        admin_exist = SchoolAdmin.query.filter_by(email=email).first()
        if admin_exist:
            email = click.prompt(click.style(
                "User with that email exist. Enter new one", fg="yellow")
            )
        new_admin = SchoolAdmin(
            fname=fname,
            email=email,
            password=Utils.hash_password(password),
        )
        new_admin.is_admin = True
        new_admin.is_active = True
        new_admin.is_anonymous = False
        new_admin.is_authenticated = True
        new_admin.password_hashed = True
        db.session.add(new_admin)
        db.session.commit()
        click.secho(f"'{fname}' added as Admin successfully!", fg="cyan")


admin.add_view(AdminModelView(SchoolAdmin, db.session,name="Admins"))

app.cli.add_command(Cmd.create_admin)
