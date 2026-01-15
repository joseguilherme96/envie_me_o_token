from pytest import fixture
from config import settings
import logging

@fixture
def execucao_spsadt_mark_parametrize(app,endpoint,get_data_execucao_spsadt,codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,
login,indicacao_clinica,indicacao_acidente,
observacao,senha,tipo_transacao,response,client_app):

    data = get_data_execucao_spsadt(codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,login,indicacao_clinica,indicacao_acidente,
observacao,senha,tipo_transacao)

    response = client_app.post(endpoint("execucao_spsadt"), json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json