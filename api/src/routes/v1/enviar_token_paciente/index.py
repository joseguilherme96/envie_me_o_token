
from flask import Blueprint,jsonify
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.routes.v1.enviar_token_paciente.factory_token import FactoryToken

token_service = FactoryToken()

token = Blueprint("token_paciente",__name__)

@token.route('/enviar_token_paciente')
def receber_token_consulta_paciente_route():
    return token_service.receber_token_consulta_paciente_route()