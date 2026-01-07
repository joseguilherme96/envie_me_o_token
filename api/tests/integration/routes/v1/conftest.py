from pytest import fixture,raises,mark
import requests
from config import settings
import logging
from flask_jwt_extended import create_access_token

from fixtures.operadora_no_mark_parametrize import operadora_no_mark_parametrize
from fixtures.execucao_spsadt_no_mark_parametrize import execucao_spsadt_no_mark_parametrize
from fixtures.execucao_spsadt_no_mark_parametrize import execucao_spsadt_no_mark_parametrize_option_2
from fixtures.execucao_spsadt_no_mark_parametrize import execucao_spsadt_no_mark_parametrize_option_3
from fixtures.contratado_no_mark_parametrize import contratado_no_mark_parametrize
from fixtures.solicitante_no_mark_parametrize import solicitante_no_mark_parametrize
from fixtures.get_data_execucao_spsadt import get_data_execucao_spsadt
from fixtures.endpoint import endpoint
from fixtures.execucao_spsadt_mark_parametrize import execucao_spsadt_mark_parametrize
from fixtures.contratado_no_mark_parametrize import contratado_no_mark_parametrize_scope_session
from fixtures.solicitante_no_mark_parametrize import solicitante_no_mark_parametrize_scope_session
from fixtures.operadora_no_mark_parametrize import operadora_no_mark_parametrize_scope_session

from fixtures.beneficiario_no_mark_parametrize_scope_function import beneficiario_no_mark_parametrize
from fixtures.beneficiario_no_mark_parametrize_scope_function import beneficiario_data
from fixtures.beneficiario_no_mark_parametrize_scope_function import nome_beneficiario
from fixtures.beneficiario_no_mark_parametrize_scope_function import atendimento_rn
from fixtures.beneficiario_no_mark_parametrize_scope_function import numero_carteira
from fixtures.beneficiario_no_mark_parametrize_scope_session import beneficiario_no_mark_parametrize_scope_session
from fixtures.beneficiario_no_mark_parametrize_scope_session import beneficiario_data
from fixtures.beneficiario_no_mark_parametrize_scope_session import nome_beneficiario
from fixtures.beneficiario_no_mark_parametrize_scope_session import atendimento_rn
from fixtures.beneficiario_no_mark_parametrize_scope_session import numero_carteira

from fixtures.user import user
from fixtures.user import user_mark_parametrize_scope_function


@fixture
def setup_tables(app,beneficiario,contratado,solicitante,operadora,tipo_user, user):

    logging.info("Iniciando setup das tabelas : beneficiario, contratado, solicitante, operadora, tipo_user e user")

    yield beneficiario, contratado, solicitante, operadora, tipo_user, user

    logging.info("Finalizando setup das tabelas : beneficiario, contratado, solicitante, operadora, tipo_user e user")

@fixture
def beneficiario(app,request_fixture,numero_carteira,atendimento_rn,nome_beneficiario,response_status_code,response_message):

    endpoint = f"{settings.BASE_URL}/beneficiario"
    data = {
        "numero_carteira": numero_carteira,
        "atendimento_rn": atendimento_rn,
        "nome_beneficiario": nome_beneficiario
    }

    logging.debug(data)
    logging.debug(endpoint)

    response = request_fixture.post(endpoint, json=data)

    logging.debug(response)

    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture
def contratado(codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento,request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/contratado", json={
        "codigo_prestador_na_operadora": codigo_prestador_na_operadora,
        "nome_contratado": nome_contratado,
        "carater_atendimento": carater_atendimento,
        "tipo_atendimento": tipo_atendimento,
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture
def solicitante(codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos,request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/solicitante", json={
        "codigo_solicitante":codigo_solicitante,
        "profissional_solicitante": profissional_solicitante,
        "conselho_profissional": conselho_profissional,
        "numero_conselho_profissional": numero_conselho_profissional,
        "uf": uf,
        "cbos": cbos
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture
def operadora(registro_ans,nome_operadora,request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/operadora", json={
        "registro_ans": registro_ans,
        "operadora": nome_operadora
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def tipo_user(request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/tipo_user", json={
        "tipo_user": "XXXXXXXXX"
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def request_fixture():
   
   request = requests.Session()

   access_token = create_access_token(identity="usuario_teste")

   request.headers.update({
       "Authorization" : f"Bearer {access_token}"
   })

   yield request

   request.close()