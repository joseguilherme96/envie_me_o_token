from flask import Flask
from src.routes.index import main
from src.routes.v1.enviar_token_paciente.index import token
from src.models.db import db
from config import settings
from dynaconf import FlaskDynaconf

from src.config_migrate import instancia_migrate

def create_app(app_config=None):

    app = Flask(__name__)
    FlaskDynaconf(app)

    app.register_blueprint(main)
    app.register_blueprint(token)

    print("Ambiente Flask :",settings.ENV_FOR_DYNACONF)
    print("DATABASE_URL :",settings.DATABASE_URL)
    print("APP_CONFIG :", app_config)
    
    if app_config:

        app.config.update(app_config)

    else :

        app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    instancia_migrate.init_app(app,db)

    return app

def get_db_path():

    return settings.DATABASE_URL

