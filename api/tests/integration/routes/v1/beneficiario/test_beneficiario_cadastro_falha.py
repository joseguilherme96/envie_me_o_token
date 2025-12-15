from hypothesis import strategies as st, given
from hypothesis.strategies import characters
from config import settings
from pytest import mark
import logging

@mark.parametrize("numero_carteira, atendimento_rn, nome_beneficiario, executar_spsadt, response_status_code, response_message",
                  [
                      ("123453423417","False","Layan",False,400,"O campo atendimento_rn deve ser um booleano !")
                  ])
def test_nao_deve_cadastrar_beneficiario_com_parametro_atendimento_rn_invalido(beneficiario,executar_spsadt,response_status_code,response_message):

    assert beneficiario["message"] == response_message
    assert beneficiario["status_code"] == response_status_code

@given(
    numero_carteira=st.text(min_size=8,max_size=12,alphabet=characters(min_codepoint=97, max_codepoint=122)),
    atendimento_rn=st.booleans(),
    nome_beneficiario=st.text(alphabet=characters(min_codepoint=97, max_codepoint=122), min_size=3, max_size=70)
)
def test_nao_deve_cadastrar_beneficiario_pois_o_valor_enviado_nao_e_um_numero_de_carteirinha(app, numero_carteira, atendimento_rn, nome_beneficiario,request_fixture):

    endpoint = f"{settings.BASE_URL}/beneficiario"
    data = {
    "numero_carteira": numero_carteira,
    "atendimento_rn": atendimento_rn,
    "nome_beneficiario": nome_beneficiario
    }
    response = request_fixture.post(endpoint, json=data)

    logging.debug(response)

    assert response.status_code == 400
    assert response.json()["message"] == "O campo numero_carteira deve ser um inteiro !"