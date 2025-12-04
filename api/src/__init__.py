from flask import Flask
from src.routes.index import main
from src.routes.v1.enviar_token_paciente.index import token
from src.models.db import db
from dotenv import load_dotenv
import os
from config import settings
from dynaconf import FlaskDynaconf

from src.config_migrate import instancia_migrate

def create_app():

    app = Flask(__name__)
    FlaskDynaconf(app)

    app.register_blueprint(main)
    app.register_blueprint(token)

    print("Ambiente Flask :",settings.ENV_FOR_DYNACONF)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{get_db_path()}"
    db.init_app(app)

    instancia_migrate.init_app(app,db)

    return app

def get_db_path():

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    db_folder = os.path.join(BASE_DIR, "instance")
    os.makedirs(db_folder, exist_ok=True)

    db_path = os.path.join(db_folder, settings.BD_NAME)

    return db_path

