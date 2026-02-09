import logging
from pytest import mark


@mark.parametrize("registro_ans,nome_operadora", [(323232, "Operadora Saúde")])
def test_deve_ser_cadastrado_operadora(operadora, registro_ans, nome_operadora):

    logging.debug(operadora)

    assert operadora["message"] == "Cadastrado com sucesso!"
    assert operadora["status_code"] == 201
