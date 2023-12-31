from flask import Flask, redirect, url_for
from flask_mail import Mail, Message
from flask_login import login_required, current_user
from flask_babel import Babel

application = Flask(
    __name__,
    static_folder="static",
    template_folder="templates",
)

from dotenv import load_dotenv

load_dotenv(".env")
application.config.from_pyfile("config.py")

mail = Mail()
mail.init_app(application)

# Init Babel

babel = Babel()

babel.init_app(application)


def send_mail(subject, *args, **kwargs):
    """ "Send mails"""
    msg = Message(subject, *args, **kwargs)
    mail.send(msg)


@login_required
def home():
    return redirect(url_for("admin.index"))
    if current_user.is_student:
        view_endpoint = "student.home"
    elif current_user.is_parent:
        view_endpoint = "parent.home"
    elif current_user.is_teacher:
        view_endpoint = "teacher.home"
    elif current_user.is_stakeholder:
        view_endpoint = "stakeholder.home"
    elif current_user.is_admin:
        view_endpoint = ("admin.home",)
    else:
        abort(403)
    return redirect(url_for(view_endpoint))


application.add_url_rule("/", view_func=home, endpoint="home")
