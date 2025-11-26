
from flask import Blueprint,jsonify
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente

token_service = FactoryAPITokenPaciente()

token = Blueprint("token_paciente",__name__)

@token.route('/enviar_token_paciente')
def receber_token_consulta_paciente_route():
    return token_service.receber_token_consulta_paciente_route()