from pytest import fixture
from config import settings


@fixture(scope="function")
def operadora_no_mark_parametrize(client_app_scope_function):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/operadora",
        json={"registro_ans": 232132, "operadora": "saude py"},
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture(scope="session")
def operadora_no_mark_parametrize_scope_session(client_app):

    response = client_app.post(
        f"{settings.BASE_URL}/operadora",
        json={"registro_ans": settings.REGISTRO_ANS, "operadora": "saude py"},
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json
