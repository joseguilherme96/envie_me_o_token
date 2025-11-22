from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph
from src.__init__ import create_app
import os
from dotenv import load_dotenv
from src.models.db import db

def generate_schema():

    try:
        load_dotenv(dotenv_path="api/.env")
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
                rankdir='LR',
                concentrate=False
            )

            path_image_schema_bd = os.getenv("path_image_schema_bd")
            path_file_save_svg = f"{os.getcwd()}/{path_image_schema_bd}/db.svg"
            graph.write_svg(f"{path_image_schema_bd}/db.svg")
            db.engine.dispose()
            print(f"O schema foi gerado com sucesso ! {path_file_save_svg}")

    except Exception as e:

        print(f"Falha ao gerar schema : {e}")


if __name__ == "__main__":

    generate_schema()