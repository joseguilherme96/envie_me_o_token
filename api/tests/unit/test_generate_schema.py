from __init__ import create_app
from pathlib import Path
from dotenv import load_dotenv
from src.schema.generate_schema import generate_schema,os
from unittest.mock import patch

def test_deve_criar_imagem_do_schema_banco_de_dados(capfd,criar_banco_de_dados,tmp_path,monkeypatch):

    monkeypatch.setenv("path_image_schema_bd",f"{str(tmp_path)}")
    generate_schema()

    path = Path(tmp_path)

    imagens = [imagem for imagem in path.iterdir() if imagem.suffix == '.svg']
    assert imagens[0].name == "db.svg"

def test_imagem_do_schema_do_bd_deve_estar_na_pasta():

    load_dotenv(dotenv_path="api/.env")
    path_image_schema_bd = os.getenv("path_image_schema_bd")
    path_image_schema_bd = Path(path_image_schema_bd)
    images = list(path_image_schema_bd.glob("**.svg"))

    assert len(images) == 1
    assert images[0].suffix == '.svg'


    
