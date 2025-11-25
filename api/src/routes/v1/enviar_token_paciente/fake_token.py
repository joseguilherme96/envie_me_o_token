from src.routes.v1.enviar_token_paciente.abstract_token import AbstractTokenPaciente
from src.rpa.fake.fake_execucao_sp_sadat import FakeExecucaoSPSADAT as FakeRPAExecucaoSPSADAT
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from flask import jsonify

class FakeTokenPaciente(AbstractTokenPaciente):

    def __init__(self):
        pass

    def validar_dados_enviados():

        return True

    def receber_token_consulta_paciente_route(self):

        try:

            self.validar_dados_enviados()
            
            where = {}
            buscar_sp_sadat = ExecucaoSPSADT()
            sp_sadat = buscar_sp_sadat.select(where)
       
            executar_rpa = FakeRPAExecucaoSPSADAT(sp_sadat)
            executar_rpa.processar_rpa()

            return jsonify({"message": "O paciente foi autorizado com sucesso !"}),201

        except Exception as e:

            return jsonify({"message":e})

