from src.abstract.abstract_token import AbstractTokenPaciente
from flask import jsonify

class TokenPaciente(AbstractTokenPaciente):

    def __init__(self):
        pass

    def validar_dados_paciente():

        return True

    def token_paciente(self):

        return jsonify({}),201