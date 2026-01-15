import logging
from pytest import mark
from config import settings


@mark.parametrize("numero_carteira, atendimento_rn, nome_beneficiario,executar_spsadt,response_status_code,response_message",
                  [
                      ("123456789012",False,"José",False,201,"Cadastrado com sucesso !"),
                  ])
def test_nao_deve_cadastrar_o_mesmo_beneficiario_duas_vezes(app,beneficiario,numero_carteira, atendimento_rn, nome_beneficiario,executar_spsadt,response_status_code,response_message,client_app):


    logging.debug(beneficiario)

    data = {
    "numero_carteira": numero_carteira,
    "atendimento_rn": atendimento_rn,
    "nome_beneficiario": nome_beneficiario
    }
    endpoint = f"{settings.BASE_URL}/beneficiario"  

    logging.debug(data)
    logging.debug(endpoint)

    response = client_app.post(endpoint, json=data)

    logging.debug(response)

    assert response.status_code == 409
    assert response.json["message"] == "Beneficiário já cadastrado !"