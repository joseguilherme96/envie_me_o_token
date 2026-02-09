from flask import Blueprint
from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente
from flask_jwt_extended import jwt_required

token_service = FactoryAPITokenPaciente()

token = Blueprint("token_paciente", __name__)


@token.route("/enviar_token_paciente")
@jwt_required()
def receber_token_consulta_paciente_route():
    return token_service.receber_token_consulta_paciente_route()
