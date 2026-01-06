from pytest import fixture
import requests
from config import settings

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

@fixture(scope="function")
def user_mark_parametrize_scope_function(tipo_user,login,senha):

    response = requests.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": senha,
        "tipo_usuario_id": tipo_user["data"]["cod_tipo_user"]
    })

    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json