import logging
from pytest import mark


@mark.parametrize(
    "registro_ans,nome_operadora,response",
    [
        ("", "", "O campo registro_ans é obrigatório !"),
        ("32323", "", "O campo operadora é obrigatório !"),
    ],
)
def test_deve_ocorrer_falha_no_cadastro_devido_ao_valor_que_nao_foi_enviado_no_campo_que_e_obrigatorio(
    operadora, registro_ans, nome_operadora, response
):

    logging.debug(operadora)

    assert operadora["message"] == response
    assert operadora["status_code"] == 400


@mark.parametrize(
    "registro_ans,nome_operadora,response",
    [
        (
            "fdfdfdfdf",
            "Operadora Saúde",
            "O campo registro_ans deve ser um número inteiro !",
        ),
        (1222, 2323232, "O campo operadora deve ser um texto !"),
    ],
)
def test_deve_ocorrer_falha_no_cadastro_dos_dados_da_operadora_pois_alguns_dados_enviados_devem_ser_numeros_inteiros(
    operadora, registro_ans, nome_operadora, response
):

    logging.debug(operadora)

    assert operadora["message"] == response
    assert operadora["status_code"] == 400
