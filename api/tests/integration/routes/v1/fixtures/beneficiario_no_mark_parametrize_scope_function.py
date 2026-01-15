from pytest import fixture
import logging
from utils.functions import _atendimento_rn,_beneficiario_data,_nome_beneficiario,_numero_carteira

@fixture(scope="function")
def beneficiario_data():
    
    yield _beneficiario_data

@fixture(scope="function")
def numero_carteira():
    
    yield _numero_carteira

@fixture(scope="function")
def atendimento_rn():
    
    yield _atendimento_rn
    
@fixture(scope="function")
def nome_beneficiario():

    yield _nome_beneficiario

@fixture(scope="function")
def beneficiario_no_mark_parametrize(app,client_app,endpoint,beneficiario_data,numero_carteira,atendimento_rn,nome_beneficiario):

    data = beneficiario_data(numero_carteira(2341534532), atendimento_rn(False), nome_beneficiario("Maria"))
    response = client_app.post(endpoint("beneficiario"), json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json
