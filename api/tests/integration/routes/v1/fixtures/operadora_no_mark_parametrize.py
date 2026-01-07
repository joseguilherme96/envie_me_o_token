from pytest import fixture
import requests
from config import settings

@fixture
def operadora_no_mark_parametrize(request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/operadora", json={
        "registro_ans": 232132,
        "operadora": "saude py"
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def operadora_no_mark_parametrize_scope_session(request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/operadora", json={
        "registro_ans": 23232,
        "operadora": "saude py"
    })
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json