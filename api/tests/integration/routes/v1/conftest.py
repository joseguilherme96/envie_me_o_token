from pytest import fixture,raises,mark
import requests
from config import settings
import logging

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
def contratado(codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento):

    response = requests.post(f"{settings.BASE_URL}/contratado", json={
        "codigo_prestador_na_operadora": codigo_prestador_na_operadora,
        "nome_contratado": nome_contratado,
        "carater_atendimento": carater_atendimento,
        "tipo_atendimento": tipo_atendimento,
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture
def solicitante(codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos,):

    response = requests.post(f"{settings.BASE_URL}/solicitante", json={
        "codigo_solicitante": codigo_solicitante,
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
def operadora(registro_ans,nome_operadora):

    response = requests.post(f"{settings.BASE_URL}/operadora", json={
        "registro_ans": registro_ans,
        "operadora": nome_operadora
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def tipo_user():

    response = requests.post(f"{settings.BASE_URL}/tipo_user", json={
        "tipo_user": "XXXXXXXXX"
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def user(tipo_user):

    response = requests.post(f"{settings.BASE_URL}/users", json={
        "login": "usuario_teste",
        "senha": "senha123",
        "tipo_usuario_id": tipo_user["data"]["cod_tipo_user"]
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def request_fixture():
   
   request = requests.Session()

   request.headers.update({
       "Authorization" : f"Bearer {settings.TOKEN}"
   })

   yield request

   request.close()