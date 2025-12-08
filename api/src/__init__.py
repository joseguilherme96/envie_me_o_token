from flask import Flask
from src.routes.index import main
from src.routes.v1.enviar_token_paciente.index import token
from src.routes.v1.tipo_user.index import tipo_user
from src.routes.v1.status.index import status
from src.models.db import db
from config import settings
from dynaconf import FlaskDynaconf
import logging
from src.config_migrate import instancia_migrate
from logging.config import dictConfig

def create_app(app_config=None):

    formatar_logging()

    app = Flask(__name__)
    FlaskDynaconf(app)

    app.register_blueprint(main)
    app.register_blueprint(token)
    app.register_blueprint(tipo_user)
    app.register_blueprint(status)
    
    if app_config:

        logging.info(f'Atualizando configuracoes do app....')
        app.config.update(app_config)
        logging.info(f"Atualizando DATABASE_URL do Dynaconf")
        settings.configure(DATABASE_URL=app_config["SQLALCHEMY_DATABASE_URI"])

    else :

        app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    logging.debug(f"ENV_FOR_DYNACONF : {settings.ENV_FOR_DYNACONF}")
    logging.debug(f"DATABASE_URL : {settings.DATABASE_URL}")
    logging.debug(f"APP_CONFIG : {app_config}")

    db.init_app(app)

    instancia_migrate.init_app(app,db)

    return app

def get_db_path():

    return settings.DATABASE_URL

def formatar_logging():

    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': "DEBUG" if settings.DEBUG else "INFO" ,
            'handlers': ['wsgi']
        }
    })

 