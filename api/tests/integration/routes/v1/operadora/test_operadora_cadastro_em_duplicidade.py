from pytest import mark
import logging
from config import settings
import requests

@mark.parametrize("registro_ans,nome_operadora",[
            (1222122,"Operadora Saúde")
])
def test_cadastro_deve_falhar_pois_ja_foi_cadastrado_uma_operadora_com_mesmo_registro_ans(operadora,registro_ans,nome_operadora, client_app_scope_function):

    logging.debug(operadora)

    data = {
        "registro_ans": registro_ans,
        "operadora": nome_operadora
    }
    endpoint = f"{settings.BASE_URL}/operadora"

    response = client_app_scope_function.post(endpoint, json=data)
    response_json = response.json

    assert response.status_code == 409
    assert response_json["message"] == "Já existe uma operadora com o mesmo registro_ans cadastrado !"