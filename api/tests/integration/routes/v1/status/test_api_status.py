from config import settings
import requests

def test_api_status_servidor_flask():

    response = requests.get(f"{settings.BASE_URL}/status")
    assert response.status_code == 200

    response_json = response.json()

    assert response_json["enviroment"] == settings.ENV_FOR_DYNACONF
    assert response_json["db"].split("\\").pop() == settings.BD_NAME