from pytest import fixture
from __init__ import create_app,db
import os
from config import settings
import pytest
from src import get_db_path


@fixture(scope="session",autouse=True)
def set_test_settigs():

    os.environ["SETTINGS_FILE_FOR_DYNACONF"] = "api/settings.toml"
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    print("\n🌱 Ambiente Dynaconf: testing ativado")

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

    print(f"🔧 DYNACONF_USE_CLASS_FAKE = {value}")
    

def pytest_addoption(parser):

    parser.addoption(
        "--dburl",
        action="store",
        default=get_db_path(),
        help=f"Database URL para  testes, default : {get_db_path()}"
    )

@fixture(scope="session")
def db_url(request):

    return request.config.getoption("--dburl")

@fixture
def app(db_url):

    test_config = {
        "SQLALCHEMY_DATABASE_URI": db_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }

    app = create_app(test_config)

    with app.app_context():

        db.create_all()
        
        yield app

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    caminho_pasta_instance = f"{os.getcwd()}/api/src/instance/"
    caminho_arquivo_banco = f"{caminho_pasta_instance}/{settings.BD_NAME}"

    os.remove(caminho_arquivo_banco)