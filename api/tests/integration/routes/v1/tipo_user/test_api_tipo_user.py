import requests
import logging
from config import settings

def test_cadastro_tipo_user(app,caplog):

    caplog.set_level(level="DEBUG")

    response = requests.post(f"{settings.BASE_URL}/tipo_user",json={"tipo_user":"Beneficiario"})
    response_json =  response.json()

    logging.debug(response_json)

    assert response_json["message"] == "Cadastrado com sucesso !"
    assert response.status_code == 201

