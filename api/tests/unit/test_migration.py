from src import create_app, db
from flask_migrate import Migrate, upgrade, migrate, init
from pathlib import Path
import os
from dotenv import load_dotenv
import logging
from sqlalchemy import text


def test_deve_iniciar_a_pasta_migrations_temp(capfd, tmp_path, caplog, client_app):

    caplog.set_level(level="INFO")
    temp_dir = tmp_path / "migrations_temp"
    temp_dir.mkdir()

    try:
        init(directory=f"{str(temp_dir)}")

        logging.info(temp_dir)
        assert True

    except:
        assert False


def test_as_migracoes_devem_ser_executadas(capfd, tmp_path, caplog, client_app):

    caplog.set_level(level="INFO")
    temp_dir = tmp_path / "migrations_temp"
    temp_dir.mkdir()

    try:
        db.drop_all()

        init(directory=f"{str(temp_dir)}")
        migrate(directory=f"{str(temp_dir)}")

        logging.info(temp_dir)
        assert True
    except Exception as e:
        assert False, f"str{e}"

    load_dotenv(dotenv_path="api/.env")

    path_versions = Path(os.path.join(temp_dir, "versions"))
    logging.info(path_versions)

    migration_file_versions = [
        file for file in path_versions.iterdir() if file.suffix == ".py"
    ]

    assert len(migration_file_versions) == 1

    try:
        upgrade(directory=f"{str(temp_dir)}")
        assert True

    except:
        assert False
