from __init__ import create_app
from pathlib import Path
from config import settings
from dotenv import load_dotenv

def test_deve_criar_banco_de_dados(capfd,criar_banco_de_dados):

    load_dotenv(dotenv_path="api/.env")

    read = capfd.readouterr()
    assert read.out == f"{settings.connection_string}\n", "Falha ao criar banco de dados !"

   

        

        