from src.abstract.abstract_api_token_paciente import AbstractAPITokenPaciente
from flask import jsonify
from src.factory.factory_execucao_sp_sadt import FactoryExecucaoSPSADT
from src.factory.factory_request_sp_sadt_data_xml import FactoryRequestSPSADTDataXML
import logging
from src.repository.ExecucaoSPSADT import ExecucaoSPSADTRepository


class APITokenPaciente(AbstractAPITokenPaciente):
    def __init__(self):

        self.dados_env_e_valido = False
        self.dados_exec_sp_sadat = None
        self.request_sp_sadt_data_xml = None
        self.execucao_sp_sadt = None

    def validar_dados_enviados(self):

        return True

    def buscar_dados_para_execucao_sp_sadt(self, codigo_execucao):

        try:
            logging.debug(codigo_execucao)
            logging.info("Buscando dados para execução SP SADT....")

            execucao_sp_sadt = ExecucaoSPSADTRepository()
            result = execucao_sp_sadt.get_full_by_codigo_execucao(codigo_execucao)

            logging.debug(result)

            self.dados_exec_sp_sadat = result

            logging.debug(self.dados_exec_sp_sadat)

        except TypeError:
            raise TypeError(
                {
                    "message": "O codigo da execução não foi informado !",
                    "status_code": 400,
                }
            )

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
