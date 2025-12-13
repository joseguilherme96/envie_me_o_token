import logging
from pytest import mark

@mark.parametrize("codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento,response",[
            ("","","","","O campo codigo_prestador_na_operadora é obrigatório !"),
            ("32323","","","","O campo nome_contratado é obrigatório !"),
            ("32323", "32323", "", "", "O campo carater_atendimento é obrigatório !"),
            ("32323", "32323", "32323", "", "O campo tipo_atendimento é obrigatório !")
])
def test_deve_ocorrer_falha_no_cadastro_devido_ao_valor_que_nao_foi_enviado_no_campo_que_e_obrigatorio(app, contratado,response):

    logging.debug(contratado)

    assert contratado["message"] == response
    assert contratado["status_code"] == 400

@mark.parametrize("codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento,response",[
            ("fdfdfdfdf", "2323232", "sdsdsd", "sdsdsdsdds", "O campo codigo_prestador_na_operadora deve ser um número inteiro !"),
            (1222, 2323232, "sdsdsd", "sdsdsdsdds", "O campo nome_contratado deve ser um texto !"),
            (32323, "Maria", "sdsds", 11, "O campo carater_atendimento deve ser um número inteiro !"),
            (32323, "32323", 1, "sdsdsd", "O campo tipo_atendimento deve ser um número inteiro !")
])
def test_deve_ocorrer_falha_no_cadastro_dos_dados_do_contratado_pois_alguns_dados_enviados_devem_ser_numeros_inteiros(contratado,response):
    
    logging.debug(contratado)

    assert contratado["message"] == response
    assert contratado["status_code"] == 400

@mark.parametrize("codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento",[
            (122232+x,"Maria",1,x) for x in range(23,50)
])
def test_cadastro_contratado_deve_falhar_devido_ao_tipo_atendimento_nao_ser_valido(app, contratado):

    logging.debug(contratado)

    assert contratado["status_code"] == 500
