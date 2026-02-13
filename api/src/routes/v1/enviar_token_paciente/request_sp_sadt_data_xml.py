from src.abstract.abstract_request_sp_sadt_data_xml import AbstractRequestSPSADTDataXML
import logging
from pathlib import Path
from config import settings
import json
from datetime import date, time


class RequestSPSADTDataXML(AbstractRequestSPSADTDataXML):
    def __init__(self, dados_sp_sadt_db):

        self.dados_sp_sadt_db = dados_sp_sadt_db
        self.xml = None
        self.template = self.carregar_template_xml()

    def carregar_template_xml(self):

        try:
            # Importar template
            template = (
                Path(settings.BASE_PATH_MODELO_TEMPLATE) / "data_request_sp_sadt_v1.xml"
            )

            with open(template, "r"):
                template = template.read_text()
                logging.debug(template)
                return template

        except Exception as e:
            raise Exception(
                {
                    "message": "Erro ao carregar o template xml de solicitação do paciente",
                    "status_code": 500,
                }
            ) from e

    def construir_xml(self):

        try:
            logging.debug("Construindo xml para envio de autorização do paciente")
            logging.debug(json.dumps(self.dados_sp_sadt_db, indent=3))

            self.xml = self.template.format(
                tipo_transacao=self.dados_sp_sadt_db["tipo_transacao"],
                sequencial_transacao=self.dados_sp_sadt_db["codigo_execucao"],
                data_registro_transacao=date.today().strftime("%Y-%m-%d"),
                hora_registro_transacao=time(hour=15, minute=30, second=0).strftime(
                    "%H:%M:%S"
                ),
                codigo_prestador_na_operadora=f"{
                    self.dados_sp_sadt_db['codigo_solicitante']
                }",
                registro_ANS=f"00{self.dados_sp_sadt_db['operadora']['registro_ans']}",
                numero_guia_operadora=self.dados_sp_sadt_db["codigo_execucao"],
                padrao="3.05.00",
                login_prestador=self.dados_sp_sadt_db["login"],
                senha_prestador=self.dados_sp_sadt_db["senha"],
                numero_guia_prestador=self.dados_sp_sadt_db["codigo_execucao"],
                tipo_etapa_autorizacao="2",
                numero_carteira=self.dados_sp_sadt_db["codigo_beneficiario"],
                atendimento_rn="S"
                if self.dados_sp_sadt_db["beneficiario"]["atendimento_rn"]
                else "N",
                nome_beneficiario=self.dados_sp_sadt_db["beneficiario"][
                    "nome_beneficiario"
                ],
                nome_contratado=self.dados_sp_sadt_db["contratado"]["nome_contratado"],
                cnes="1",
                nome_profissional=self.dados_sp_sadt_db["solicitante"][
                    "profissional_solicitante"
                ],
                conselho_profissional=f"0{
                    self.dados_sp_sadt_db['solicitante']['conselho_profissional']
                }",
                numero_conselho_profissional=self.dados_sp_sadt_db["solicitante"][
                    "numero_conselho_profissional"
                ],
                uf=self.dados_sp_sadt_db["solicitante"]["uf"],
                cbos=self.dados_sp_sadt_db["solicitante"]["cbos"],
                carater_atendimento=self.dados_sp_sadt_db["contratado"][
                    "carater_atendimento"
                ],
                data_solicitacao=date.today().strftime("%Y-%m-%d"),
                indicacao_clinica=self.dados_sp_sadt_db["indicacao_clinica"],
                codigo_tabela="22",
                codigo_procedimento=self.dados_sp_sadt_db[
                    "execucao_spsadt_procedimento"
                ][0]["codigo_procedimento"],
                descricao_procedimento=self.dados_sp_sadt_db[
                    "execucao_spsadt_procedimento"
                ][0]["descricao_procedimento"],
                quantidade_solicitada=self.dados_sp_sadt_db[
                    "execucao_spsadt_procedimento"
                ][0]["quantidade_solicitada"],
                codigo_operadora=self.dados_sp_sadt_db["operadora"]["registro_ans"],
                observacao=self.dados_sp_sadt_db["observacao"],
                hash="",
            )

            logging.info("XML Construído com sucesso !")
            logging.debug(self.xml)

        except Exception as e:
            raise Exception(
                {
                    "message": "Erro ao construir o xml de solicitação do paciente",
                    "status_code": 500,
                }
            ) from e
