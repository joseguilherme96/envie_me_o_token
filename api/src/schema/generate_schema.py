from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph
from src.__init__ import create_app
import os
from dotenv import load_dotenv
from src.models.db import db
import logging
from config import settings


def generate_schema():

    try:
        app = create_app()

        with app.app_context():
            db.create_all()
            metadata = MetaData()
            metadata.reflect(bind=db.engine)

            graph = create_schema_graph(
                db.engine,
                metadata=metadata,
                show_datatypes=False,
                show_indexes=False,
                rankdir="LR",
                concentrate=False,
            )

            path_image_schema_bd = settings.path_image_schema_bd
            path_file_save_svg = f"{path_image_schema_bd}/db.svg"
            graph.write_svg(path_file_save_svg)
            db.engine.dispose()
            logging.info(f"O schema foi gerado com sucesso ! {path_file_save_svg}")

    except Exception as e:
        logging.info(f"Falha ao gerar schema : {e}")


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO", format="%(asctime)s - %(levelname)s - %(message)s"
    )

    generate_schema()
