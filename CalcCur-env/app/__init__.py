from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    return app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Ставим редирект, если пользователь не авторизован, для страниц где обязательна авторизация
login_manager = LoginManager(app)
login_manager.login_view = 'admin_blueprint.login'