from flask import Flask
from src.routes.index import main
from src.models.db import db
from dotenv import load_dotenv
import os
from flask_migrate import Migrate, upgrade, migrate, init

load_dotenv(dotenv_path="api/.env")

def create_app():

    app = Flask(__name__)
    app.register_blueprint(main)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{get_db_path()}"
    db.init_app(app)

    Migrate(app,db)

    return app

def get_db_path():

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    db_folder = os.path.join(BASE_DIR, "instance")
    os.makedirs(db_folder, exist_ok=True)

    db_path = os.path.join(db_folder, os.getenv("BD_NAME"))

    return db_path

