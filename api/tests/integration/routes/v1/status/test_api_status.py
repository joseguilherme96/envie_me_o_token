from config import settings
import requests


def test_api_status_servidor_flask(client_app):

    response = client_app.get(f"{settings.BASE_URL}/status")
    assert response.status_code == 200

    response_json = response.json

    assert response_json["environment"] == settings.ENV_FOR_DYNACONF
    assert response_json["db"].split("\\").pop() == settings.BD_NAME
    assert response_json["max_connections"]
    assert response_json["opened_connetions"] or response_json["opened_connetions"] == 0
