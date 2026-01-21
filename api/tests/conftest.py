from pytest import fixture
from __init__ import create_app,db
import os
from config import settings
import pytest
from src import get_db_path
from sqlalchemy  import create_engine, StaticPool
from sqlalchemy.exc import OperationalError as SQLAlchemyOperationalError
import logging
from sqlalchemy import text
from flask_jwt_extended import create_access_token
import logging

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):

    db_url = session.config.getoption("--dburl")

    try:

        engine = create_engine(
            db_url,
            poolclass=StaticPool
        )

        connection = engine.connect()
        connection.close()

        logging.info("Usando DATA BASE URL:", db_url)
        logging.info("Conexão com o banco de dados feito com sucesso !")

        try:

            logging.debug(settings.BASE_URL)

        except Exception as e:

            raise Exception(e)

    except SQLAlchemyOperationalError as e:

        logging.info(f"Falha ao conectar com o banco de dados {db_url}")
        logging.debug(e)
        pytest.exit("Os testes foram finalidados devido a falta de conexão com o banco de dados !")

    except Exception as e:

        logging.debug(e)
        pytest.exit("Os testes foram finalidados devido o servidor Flask não estar configurado corretamente !")

@fixture(scope="session",autouse=True)
def set_test_settigs(environment):

    os.environ["SETTINGS_FILE_FOR_DYNACONF"] = "api/settings.toml"
    os.environ["ENV_FOR_DYNACONF"] = environment
    settings.configure(FORCE_ENV_FOR_DYNACONF=environment)
    logging.info(f"🌱 Ambiente Dynaconf: {environment} ativado")

    value = os.environ.get("DYNACONF_USE_CLASS_FAKE",None)

    if value is None:
    
        pytest.exit(f"""
                    
        🚨 Variável obrigatória `DYNACONF_USE_CLASS_FAKE` não definida!

        Defina antes de rodar os testes:

        Windows:
            set DYNACONF_USE_CLASS_FAKE=true && pytest api
            set DYNACONF_USE_CLASS_FAKE=false && pytest api

        Linux/mac:
            DYNACONF_USE_CLASS_FAKE=true pytest api
            DYNACONF_USE_CLASS_FAKE=false pytest api
        """)

    logging.info(f"🔧 DYNACONF_USE_CLASS_FAKE = {value}")
    
def pytest_addoption(parser):

    parser.addoption(
        "--dburl",
        action="store",
        default=get_db_path(),
        help=f"Database URL para testes, default : {get_db_path()}"
    )

    parser.addoption(
        "--environment",
        action="store",
        default="testing",
        help="Ambiente para execução dos testes. Default : Testing"
    )

@fixture(scope="session")
def db_url(request):

    return request.config.getoption("--dburl")

@fixture(scope="session")
def environment(request):

    return request.config.getoption("--environment")

@pytest.fixture(scope="session")
def client_app(app):

    test_client = app.test_client()
    client = gerar_token(test_client)

    yield client

@pytest.fixture(scope="function")
def client_app_scope_function(app_scope_function):

    test_client = app_scope_function.test_client()
    client = gerar_token(test_client)
    yield client

@fixture(scope="session")
def app(db_url):

    config = configurar_app(db_url)
    logging.info("Criando app...")
    app = create_app(config)

    with app.app_context():

        db.create_all()
        
        yield app

        clear_db(db)

@fixture(scope="function")
def app_scope_function(db_url):

    config = configurar_app(db_url)
    logging.info("Criando app...")
    app = create_app(config)

    with app.app_context():

        db.create_all()
        
        yield app

        clear_db(db)

def configurar_app(db_url):

    test_config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "TESTING": True
    }
    
    logging.debug(f"configuracoes do app : {test_config}")

    return test_config

def gerar_token(client):

    access_token = create_access_token(identity="usuario_teste")
    client.environ_base["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"

    return client

def clear_db(db):

    db.session.execute(text("DROP TABLE IF EXISTS alembic_version"))
    db.session.commit()
    db.session.remove()
    db.drop_all()
    db.engine.dispose()
