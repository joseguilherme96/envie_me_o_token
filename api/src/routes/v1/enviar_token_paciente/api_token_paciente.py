from src.abstract.abstract_api_token_paciente import AbstractAPITokenPaciente
from flask import jsonify

class APITokenPaciente(AbstractAPITokenPaciente):

    def __init__(self):
        pass

    def validar_dados_paciente():

        return True

    def receber_token_consulta_paciente_route(self):

        return jsonify({}),201