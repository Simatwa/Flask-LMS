from .app import application

from .accounts.views import app as account_view

application.register_blueprint(account_view, url_prefix="/accounts", cli_group="user")

from flask_migrate import Migrate
from .models import db

migrate = Migrate()
migrate.init_app(application, db)
