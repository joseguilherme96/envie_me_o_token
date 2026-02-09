from pathlib import Path
from config import settings
from dotenv import load_dotenv


def test_deve_criar_banco_de_dados_em_memoria(app, request):

    load_dotenv(dotenv_path="api/.env")

    if settings.DATABASE_MEMORY:
        path_bd = Path("/src/instance/testing.db")
        assert path_bd.name == f"{settings.BD_NAME}", "Falha ao criar banco de dados !"
