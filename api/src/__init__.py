from flask import Flask
from src.routes.index import main
from src.routes.v1.enviar_token_paciente.index import token
from src.routes.v1.tipo_user.index import tipo_user
from src.routes.v1.status.index import status
from src.routes.v1.contratado.index import contratado
from src.routes.v1.beneficiario.index import beneficiario
from src.routes.v1.operadora.index import operadora
from src.routes.v1.solicitante.index import solicitante
from src.routes.v1.execucao_spsadt.index import execucao_spsadt
from src.routes.v1.execucao_spsadt_procedimento.index import execucao_spsadt_procedimento
from src.routes.v1.users.index import users
from src.routes.v1.login.index import login
from src.models.db import db
from config import settings
from dynaconf import FlaskDynaconf
import logging
from src.config_migrate import instancia_migrate
from logging.config import dictConfig
from flask_jwt_extended import JWTManager

def create_app(app_config=None):

    formatar_logging()

    app = Flask(__name__)
    FlaskDynaconf(app)

    app.register_blueprint(main)
    app.register_blueprint(token)
    app.register_blueprint(tipo_user)
    app.register_blueprint(status)
    app.register_blueprint(contratado)
    app.register_blueprint(beneficiario)
    app.register_blueprint(operadora)
    app.register_blueprint(solicitante)
    app.register_blueprint(execucao_spsadt)
    app.register_blueprint(execucao_spsadt_procedimento)
    app.register_blueprint(users)
    app.register_blueprint(login)
    
    if app_config:

        logging.info(f'Atualizando configuracoes do app....')
        app.config.update(app_config)
        logging.info(f"Atualizando DATABASE_URL do Dynaconf")
        settings.configure(DATABASE_URL=app_config["SQLALCHEMY_DATABASE_URI"])

    else :

        app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
    jwt = JWTManager(app)

    logging.debug(f"ENV_FOR_DYNACONF : {settings.ENV_FOR_DYNACONF}")
    logging.debug(f"DATABASE_URL : {settings.DATABASE_URL}")
    logging.debug(f"DATABASE_URL_SCOPE_FUNCTION : {settings.DATABASE_URL_SCOPE_FUNCTION}")
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

 