# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
db = SQLAlchemy()
app = Flask(__name__)


def create_app():

    app.config.from_object(Config)
    # deferred import
    from app.models import Service

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
