from flask import Blueprint, jsonify, request
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente
from src.models.UserTipo import TipoUser
from src.models.db import db

tipo_user = Blueprint("tipo_user", __name__)


@tipo_user.route("/tipo_user", methods=["POST"])
def cadastrar_tipo_user():

    try:
        dados = request.get_json()

        dados = TipoUser.inserir(TipoUser(tipo=dados["tipo_user"]))

        return jsonify({"message": "Cadastrado com sucesso !", "data": dados}), 201

    except Exception as e:
        return jsonify({"message": f"Falha ao cadastrar ! {e}"}), 500
