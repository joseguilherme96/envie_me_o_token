from pytest import fixture
import requests
from config import settings
import logging

@fixture
def contratado_no_mark_parametrize(request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/contratado", json={
        "codigo_prestador_na_operadora": "2122323",
        "nome_contratado": "Sonia",
        "carater_atendimento": 1,
        "tipo_atendimento": 1,
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def contratado_no_mark_parametrize_scope_session(request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/contratado", json={
        "codigo_prestador_na_operadora": "2323123",
        "nome_contratado": "Sonia",
        "carater_atendimento": 1,
        "tipo_atendimento": 1,
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json