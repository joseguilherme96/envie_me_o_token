from pytest import fixture
from config import settings
import logging
from utils.functions import _atendimento_rn,_beneficiario_data,_nome_beneficiario,_numero_carteira

@fixture(scope="session")
def beneficiario_data():

    yield _beneficiario_data

@fixture(scope="session")
def numero_carteira():

    yield _numero_carteira

@fixture(scope="session")
def atendimento_rn():

    yield _atendimento_rn

@fixture(scope="session")
def nome_beneficiario():

    yield _nome_beneficiario
    
@fixture(scope="session")
def beneficiario_no_mark_parametrize_scope_session(app,client_app,beneficiario_data,nome_beneficiario,atendimento_rn,
                                                   numero_carteira):

    endpoint = f"{settings.BASE_URL}/beneficiario"

    data = beneficiario_data(numero_carteira(2345124532), atendimento_rn(False), nome_beneficiario("Maria"))
    response = client_app.post(endpoint, json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json