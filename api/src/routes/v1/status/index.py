
from flask import Blueprint,jsonify,request
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente
from src.models.UserTipo import TipoUser
from src.models.db import db
from config import settings
from datetime import datetime
from src.models.db import db

status = Blueprint("status",__name__)

@status.route('/status',methods=["GET"])
def cadastrar_tipo_user():

    engine = db.get_engine()
    url = engine.url

    try:
        
        return jsonify({
            "data_hora": datetime.now(),
            "enviroment": settings.ENV_FOR_DYNACONF,
            "db": url.database
        }),200
    
    except Exception as e:

        return jsonify({"message":f"Falha ao buscar status ! {e}"}),500