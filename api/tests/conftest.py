from pytest import fixture
from __init__ import create_app,db
import os
from dotenv import load_dotenv

@fixture
def criar_banco_de_dados():

    load_dotenv(dotenv_path="api/.env")

    app = create_app()

    with app.app_context():

        db.create_all()
        print(os.getenv("connection_string"))

    yield [app,db]

    with app.app_context():

        db.drop_all()
        db.engine.dispose()

    caminho_pasta_instance = f"{os.getcwd()}/api/src/instance/"
    caminho_arquivo_banco = f"{caminho_pasta_instance}/{os.getenv("BD_NAME")}"

    os.remove(caminho_arquivo_banco)
    os.removedirs(caminho_pasta_instance)