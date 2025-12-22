import logging
from pytest import mark

@mark.parametrize("codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos,response",[
            ("","","","","","","O campo codigo_solicitante é obrigatório !"),
            ("1001","","","","","","O campo profissional_solicitante é obrigatório !"),
            ("1001","Dr. Maria","","","","","O campo conselho_profissional é obrigatório !"),
            ("1001","Dr. Maria","1","","","","O campo numero_conselho_profissional é obrigatório !"),
            ("1001","Dr. Maria","1","123456","","","O campo uf é obrigatório !"),
            ("1001","Dr. Maria","1","123456","35","","O campo cbos é obrigatório !")
])
def test_deve_ocorrer_falha_no_cadastro_devido_ao_valor_que_nao_foi_enviado_no_campo_que_e_obrigatorio(app, solicitante,response,codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos):

    logging.debug(solicitante)

    assert solicitante["message"] == response
    assert solicitante["status_code"] == 400

@mark.parametrize("codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos,response",[
            ("abc","Dr. Maria",1,"123456",35,225125,"O campo codigo_solicitante deve ser um número inteiro !"),
            (1001,123,1,"123456",35,225125,"O campo profissional_solicitante deve ser um texto !"),
            (1001,"Dr. Maria","abc","123456",35,225125,"O campo conselho_profissional deve ser um número inteiro !"),
            (1001,"Dr. Maria",1,123456,35,225125,"O campo numero_conselho_profissional deve ser um texto !"),
            (1001,"Dr. Maria",1,"123456","abc",225125,"O campo uf deve ser um número inteiro !"),
            (1001,"Dr. Maria",1,"123456",35,"abc","O campo cbos deve ser um número inteiro !")
])
def test_deve_ocorrer_falha_no_cadastro_dos_dados_do_solicitante_pois_alguns_dados_enviados_devem_ser_numeros_inteiros(solicitante,response):
    
    logging.debug(solicitante)

    assert solicitante["message"] == response
    assert solicitante["status_code"] == 400