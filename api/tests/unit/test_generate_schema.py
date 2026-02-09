from pathlib import Path
from src.schema.generate_schema import generate_schema
from config import settings


def test_deve_criar_imagem_do_schema_banco_de_dados(capfd, app, tmp_path, monkeypatch):

    monkeypatch.setattr(settings, "path_image_schema_bd", f"{str(tmp_path)}")
    generate_schema()

    path = Path(tmp_path)

    imagens = [imagem for imagem in path.iterdir() if imagem.suffix == ".svg"]
    assert imagens[0].name == "db.svg"
