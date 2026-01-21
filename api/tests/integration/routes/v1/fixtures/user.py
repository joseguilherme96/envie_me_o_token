from pytest import fixture
import requests
from config import settings
from flask_jwt_extended import create_access_token

@fixture(scope="session")
def user(tipo_user,client_app):

    login = "usuario_teste"

    response = client_app.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": "senha123",
        "tipo_usuario_id": tipo_user["data"]["cod_tipo_user"]
    })
    
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="function")
def user_scope_function(tipo_user_scope_function,client_app_scope_function):

    login = "usuario_teste"

    response = client_app_scope_function.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": "senha123",
        "tipo_usuario_id": tipo_user_scope_function["data"]["cod_tipo_user"]
    })
    
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="function")
def user_mark_parametrize_scope_function(tipo_user_scope_function,login,senha,client_app_scope_function):

    response = client_app_scope_function.post(f"{settings.BASE_URL}/users", json={
        "login": login,
        "senha": senha,
        "tipo_usuario_id": tipo_user_scope_function["data"]["cod_tipo_user"]
    })

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json