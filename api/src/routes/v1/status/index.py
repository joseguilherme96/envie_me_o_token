from flask import Blueprint, jsonify
from src.models.db import db
from config import settings
from datetime import datetime
from src.models.db import db
from sqlalchemy import text
import logging

status = Blueprint("status", __name__)


@status.route("/status", methods=["GET"])
def status_servidor():

    try:
        engine = db.get_engine()
        url = engine.url

        if url.drivername == "mysql+pymysql":
            execute = db.session.execute(text("SHOW STATUS LIKE 'Threads_connected';"))
            opened_connetions = execute.fetchone()[1]

            logging.debug(opened_connetions)

            execute = db.session.execute(text("SHOW VARIABLES LIKE 'max_connections';"))
            max_connections = execute.fetchone()[1]

            logging.debug(max_connections)

            db.session.close()

        if url.drivername == "sqlite":
            pool = engine.pool
            opened_connetions = pool.checkedout()
            max_connections = pool.size()

        return jsonify(
            {
                "data_hora": datetime.now(),
                "environment": settings.ENV_FOR_DYNACONF,
                "db": url.database,
                "opened_connetions": opened_connetions,
                "max_connections": max_connections,
            }
        ), 200

    except Exception as e:
        return jsonify({"message": f"Falha ao buscar status ! {e}"}), 500
