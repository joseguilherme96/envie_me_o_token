import logging
from config import settings
from pytest import mark
from hypothesis import given, strategies as st
from hypothesis.strategies import characters


@mark.parametrize(
    "numero_carteira, atendimento_rn, nome_beneficiario,executar_spsadt,response_status_code,response_message",
    [
        ("1351236743", False, "José", False, 201, "Cadastrado com sucesso !"),
        ("1236783423", True, "João", False, 201, "Cadastrado com sucesso !"),
    ],
)
def test_deve_cadastrar_beneficiario(
    beneficiario, executar_spsadt, response_status_code, response_message
):

    assert beneficiario["message"] == response_message
    assert beneficiario["status_code"] == response_status_code


test_com_numeros_nao_repetidos = []


@given(
    numero_carteira=st.integers(min_value=11111111, max_value=999999999999),
    atendimento_rn=st.booleans(),
    nome_beneficiario=st.text(
        alphabet=characters(min_codepoint=97, max_codepoint=122),
        min_size=3,
        max_size=70,
    ),
)
def test_deve_cadastrar_beneficiario_com_dados_gerados_em_massa(
    app, numero_carteira, atendimento_rn, nome_beneficiario, client_app
):

    if numero_carteira not in test_com_numeros_nao_repetidos:
        test_com_numeros_nao_repetidos.append(numero_carteira)

        response = client_app.post(
            f"{settings.BASE_URL}/beneficiario",
            json={
                "numero_carteira": numero_carteira,
                "atendimento_rn": atendimento_rn,
                "nome_beneficiario": nome_beneficiario,
            },
        )

        logging.debug(response)
        logging.debug(response.json)

        assert response.status_code == 201
        assert response.json["message"] == "Cadastrado com sucesso !"
