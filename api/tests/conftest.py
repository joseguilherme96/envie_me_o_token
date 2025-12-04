from pytest import fixture
from __init__ import create_app,db
import os
from config import settings
import pytest


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
    

@fixture
def criar_banco_de_dados():

    app = create_app()

    with app.app_context():

        db.create_all()
        print(settings.connection_string)

    yield [app,db]

    with app.app_context():

        db.drop_all()
        db.engine.dispose()

    caminho_pasta_instance = f"{os.getcwd()}/api/src/instance/"
    caminho_arquivo_banco = f"{caminho_pasta_instance}/{settings.BD_NAME}"

    os.remove(caminho_arquivo_banco)
    os.removedirs(caminho_pasta_instance)