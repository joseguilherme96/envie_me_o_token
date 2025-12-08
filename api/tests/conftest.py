from pytest import fixture
from __init__ import create_app,db
import os
from config import settings
import pytest
from src import get_db_path
from sqlalchemy  import create_engine, StaticPool
from sqlalchemy.exc import OperationalError as SQLAlchemyOperationalError
import requests
import logging
from sqlalchemy import text


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
            response = requests.get(settings.BASE_URL)

            if response.status_code != 200:

                raise 

            logging.info("A conexão com o servidor flask foi feita com sucesso !")
            
        except Exception as e:

            raise Exception(e)

    except SQLAlchemyOperationalError as e:

        logging.info(f"Falha ao conectar com o banco de dados {db_url}")
        logging.debug(e)
        pytest.exit("Os testes foram finalidados devido a falta de conexão com o banco de dados !")

    except Exception as e:

        logging.info(f"Falha ao conectar com o servidor Flask ! \n")
        logging.debug(e)
        pytest.exit("Os testes foram finalidados devido a falta de conexão com o servidor !")


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

@fixture
def app(db_url):

    test_config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    
    logging.info("Criando app...")
    logging.debug(f"configuracoes do app : {test_config}")
    app = create_app(test_config)

    with app.app_context():

        db.create_all()
        
        yield app

        db.session.execute(text("DROP TABLE IF EXISTS alembic_version"))
        db.session.commit()
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
