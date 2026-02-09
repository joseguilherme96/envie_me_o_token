import logging
from config import settings


def test_cadastro_execucao_spsadt_procedimento(
    execucao_spsadt_no_mark_parametrize_option_2, client_app
):

    response = client_app.post(
        f"{settings.BASE_URL}/execucao_spsadt_procedimento",
        json={
            "codigo_procedimento": 1,
            "codigo_execucao": execucao_spsadt_no_mark_parametrize_option_2["data"][
                "codigo_execucao"
            ],
            "descricao_procedimento": "Fisioterapia",
            "quantidade_solicitada": 10,
        },
    )
    response_json = response.json

    logging.debug(response_json)

    assert response_json["message"] == "Cadastrado com sucesso!"
    assert response.status_code == 201
