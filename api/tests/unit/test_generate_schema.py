from __init__ import create_app
from pathlib import Path
import os
from dotenv import load_dotenv
from schema.generate_schema import generate_schema

def test_deve_criar_imagem_do_schema_banco_de_dados(capfd,criar_banco_de_dados):

    generate_schema()

    load_dotenv(dotenv_path="api/.env")
    path_image_schema_bd = os.getenv("path_image_schema_bd")
    path = Path(path_image_schema_bd)

    imagens = [imagem for imagem in path.iterdir() if imagem.suffix == '.svg']
    assert imagens[0].name == "db.svg"

    os.remove(f"{path}/{imagens[0].name}")

    
