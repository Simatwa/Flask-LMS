from core.teachers import app
from core.teachers.admin import admin
from flask_login import login_required
from flask import request, url_for, redirect, make_response


class TeacherView:
    @classmethod
    @login_required
    def home(cls):
        """ "Respond with index for parents"""
        pass


teachers_view = TeacherView()

app.add_url_rule("/", view_func=teachers_view.home, endpoint="home")
