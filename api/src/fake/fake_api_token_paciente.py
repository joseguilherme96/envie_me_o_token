from src.abstract.abstract_api_token_paciente import AbstractAPITokenPaciente
from src.factory.factory_execucao_sp_sadt import FactoryExecucaoSPSADT
from src.factory.factory_request_sp_sadt_data_xml import FactoryRequestSPSADTDataXML
from flask import jsonify
import logging


class FakeAPITokenPaciente(AbstractAPITokenPaciente):
    def __init__(self):

        self.dados_env_e_valido = False
        self.dados_exec_sp_sadat = None
        self.request_sp_sadt_data_xml = None
        self.execucao_sp_sadt = None

    def validar_dados_enviados(self):

        self.dados_env_e_valido = True

    def buscar_dados_para_execucao_sp_sadt(self, codigo_execucao):

        self.dados_exec_sp_sadat = {
            "paciente": "Henrique",
            "numero_carteirinha": "32424242242424242",
        }

    def enviar_dados_para_execucao_sp_sadt(self):

        logging.info("Recebendo dados para execução do SP SADT...")

        try:
            self.validar_dados_enviados()
            self.buscar_dados_para_execucao_sp_sadt(1)

            self.factory_request_sp_sadt_data_xml = FactoryRequestSPSADTDataXML.create(
                self.dados_exec_sp_sadat
            )
            self.factory_request_sp_sadt_data_xml.construir_xml()

            self.execucao_sp_sadt = FactoryExecucaoSPSADT.create(
                "http://apifake.com", self.factory_request_sp_sadt_data_xml.xml
            )
            self.execucao_sp_sadt.processar_rpa()

            return jsonify({"message": "O paciente foi autorizado com sucesso !"}), 201

        except Exception as e:
            erro = e.args[0]

            return jsonify({"message": erro["message"]}), erro["status_code"]
