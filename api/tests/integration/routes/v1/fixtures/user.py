from pytest import fixture
import requests
from config import settings
from flask_jwt_extended import create_access_token

@fixture(scope="session")
def user(tipo_user,request_fixture):

    login = "usuario_teste"

    response = request_fixture.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": "senha123",
        "tipo_usuario_id": tipo_user["data"]["cod_tipo_user"]
    })
    
    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="function")
def user_mark_parametrize_scope_function(tipo_user,login,senha,request_fixture):

    response = request_fixture.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": senha,
        "tipo_usuario_id": tipo_user["data"]["cod_tipo_user"]
    })

    response_json = response.json()
    response_json["status_code"] = response.status_code

    yield response_json