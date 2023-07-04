from .app import application

from .accounts.views import app as account_view
from .students.views import app as student_view
from .parents.views import app as parent_view

application.register_blueprint(account_view, url_prefix="/accounts", cli_group="user")
application.register_blueprint(
    student_view, url_prefix="/students", cli_group="student"
)
application.register_blueprint(parent_view, url_prefix="/parents", cli_group="parent")

from flask_migrate import Migrate
from .models import db

migrate = Migrate()
migrate.init_app(application, db)
