from pytest import fixture
from config import settings
import logging

@fixture
def get_data_execucao_spsadt():
    def _get_data_execucao_spsadt(*data):

        data = {
            "codigo_beneficiario": data[0],
            "codigo_contratado": data[1],
            "codigo_solicitante": data[2],
            "operadora_registro_ans": data[3],
            "login": data[4],
            "indicacao_clinica": data[5],
            "indicacao_acidente": data[6],
            "observacao": data[7],
            "senha": data[8],
            "tipo_transacao": data[9]
        }
        logging.debug(data)

        return data

    yield _get_data_execucao_spsadt

@fixture(scope="session")
def get_data_execucao_spsadt():
    def _get_data_execucao_spsadt(*data):

        data = {
            "codigo_beneficiario": data[0],
            "codigo_contratado": data[1],
            "codigo_solicitante": data[2],
            "operadora_registro_ans": data[3],
            "login": data[4],
            "indicacao_clinica": data[5],
            "indicacao_acidente": data[6],
            "observacao": data[7],
            "senha": data[8],
            "tipo_transacao": data[9]
        }
        logging.debug(data)

        return data

    yield _get_data_execucao_spsadt