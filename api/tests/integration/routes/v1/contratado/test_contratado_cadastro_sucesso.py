import logging
from pytest import mark

@mark.parametrize("codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento",[
            (323232,"Maria",1,22)
])
def test_deve_ser_cadastrado_contratado(app, contratado):

    logging.debug(contratado)

    assert contratado["message"] == "Cadastrado com sucesso!"
    assert contratado["status_code"] == 201

@mark.parametrize("codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento",[
            (12232+x,"Maria",1,x) for x in range(1,23)
])
def test_cadastrado_contratado_deve_ser_cadastrado_com_sucesso_devido_o_tipo_atendimento_ser_valido_do_1_ao_23(app, contratado):

    logging.debug(contratado)

    assert contratado["message"] == "Cadastrado com sucesso!"
    assert contratado["status_code"] == 201
