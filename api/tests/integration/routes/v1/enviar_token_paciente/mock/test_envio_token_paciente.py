import requests
from unittest.mock import patch
from pytest import mark
from dotenv import load_dotenv
from config import settings


@patch("requests.post")
def test_deve_responder_status_code_201(mock_request_post):

    load_dotenv()

    mock_request_post.return_value.json.return_value = {
        "message": "O paciente foi autorizado com sucesso !",
        "messages": [],
    }

    response = requests.post(
        f"{settings.BASE_URL}/enviar_token_paciente",
        json={"token": "123343222", "codigo_execucao_sp_sadt": 1},
    )
    response_json = response.json()

    assert response_json == {
        "message": "O paciente foi autorizado com sucesso !",
        "messages": [],
    }


@patch("requests.post")
def test_deve_responder_token_invalido(mock_request_post):

    mock_request_post.return_value.json.return_value = {
        "message": "Falha ao processar autorização !",
        "messages": [],
    }

    response = requests.post(
        f"{settings.BASE_URL}/enviar_token_paciente",
        json={"token": "123343222", "codigo_execucao_sp_sadt": 1},
    )
    response_json = response.json()

    assert response_json == {
        "message": "Falha ao processar autorização !",
        "messages": [],
    }
