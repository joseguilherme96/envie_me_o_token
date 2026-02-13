from pytest import fixture
from config import settings


@fixture(scope="function")
def solicitante_no_mark_parametrize(client_app_scope_function):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/solicitante",
        json={
            "codigo_solicitante": 23323,
            "profissional_solicitante": "Sonia",
            "conselho_profissional": "1",
            "numero_conselho_profissional": "12121",
            "uf": 1,
            "cbos": 1,
        },
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture(scope="session")
def solicitante_no_mark_parametrize_scope_session(client_app):

    response = client_app.post(
        f"{settings.BASE_URL}/solicitante",
        json={
            "codigo_solicitante": settings.CODIGO_PRESTADOR_NA_OPERADORA,
            "profissional_solicitante": "Sonia",
            "conselho_profissional": settings.CONSELHO_PROFISSIONAL,
            "numero_conselho_profissional": "12121",
            "uf": settings.UF,
            "cbos": settings.CBOS,
        },
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json
