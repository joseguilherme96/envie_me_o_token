from pytest import fixture
import requests
from config import settings
import logging


@fixture(scope="session")
def execucao_spsadt_procedimento_no_mark_parametrize(
    client_app, execucao_spsadt_no_mark_parametrize
):

    response = client_app.post(
        f"{settings.BASE_URL}/execucao_spsadt_procedimento",
        json={
            "codigo_procedimento": 1,
            "codigo_execucao": execucao_spsadt_no_mark_parametrize["data"][
                "codigo_execucao"
            ],
            "descricao_procedimento": "Fisioterapia",
            "quantidade_solicitada": 10,
        },
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json
