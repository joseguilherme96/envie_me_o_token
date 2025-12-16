from pytest import fixture
import requests
from config import settings
import logging

@fixture
def solicitante_no_mark_parametrize():

    response = requests.post(f"{settings.BASE_URL}/solicitante", json={
        "codigo_solicitante": 23323,
        "profissional_solicitante": "Sonia",
        "conselho_profissional": "1",
        "numero_conselho_profissional": "12121",
        "uf": 1,
        "cbos": 1
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def solicitante_no_mark_parametrize_scope_session():

    response = requests.post(f"{settings.BASE_URL}/solicitante", json={
        "codigo_solicitante": 2323,
        "profissional_solicitante": "Sonia",
        "conselho_profissional": "1",
        "numero_conselho_profissional": "12121",
        "uf": 1,
        "cbos": 1
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json