import logging
from pytest import mark
import requests
from config import settings

@mark.parametrize("codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,login,indicacao_clinica,indicacao_acidente,observacao,senha,tipo_transacao,response",[
            ("",12345,"1001",123456,"usuario","","","","","","O campo codigo_beneficiario é obrigatório !"),
            ("123456789012342","","","","","","","","","","O campo codigo_contratado é obrigatório !"),
            ("123456789012313",12345,"","","","","","","","","O campo codigo_solicitante é obrigatório !"),
            ("123456789012322",12345,"1001","","","","","","","","O campo operadora_registro_ans é obrigatório !"),
            ("123456789012399",12345,"1001",123456,"","","","","","","O campo login é obrigatório !"),
            ("123456789012192",12345,"1001",123456,"usuario","","","","","","O campo indicacao_clinica é obrigatório !"),
            ("123456789012249",12345,"1001",123456,"usuario","True","","","","","O campo indicacao_acidente é obrigatório !"),
            ("123456789012233",12345,"1001",123456,"usuario","True","0","","","","O campo observacao é obrigatório !"),
            ("123456789012222",12345,"1001",123456,"usuario","True","0","obs","","","O campo senha é obrigatório !"),
            ("123456789012323",12345,"1001",123456,"usuario","True","0","obs","senha","","O campo tipo_transacao é obrigatório !")
])
def test_deve_ocorrer_falha_devido_os_campos_serem_enviados_vazios(app, execucao_spsadt_mark_parametrize,response):

    logging.debug(execucao_spsadt_mark_parametrize)

    assert execucao_spsadt_mark_parametrize["message"] == response
    assert execucao_spsadt_mark_parametrize["status_code"] == 400

@mark.parametrize("codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,login,indicacao_clinica,indicacao_acidente,observacao,senha,tipo_transacao,response",[
            (1234567890123222,12345,1001,123456,"usuario",True,0,"obs","senha","tipo","O campo codigo_beneficiario deve ser um texto !"),
            ("123456789012344","abc",1001,123456,"usuario",True,0,"obs","senha","tipo","O campo codigo_contratado deve ser um número inteiro !"),
            ("123456789023232",12345,"abc",123456,"usuario",True,0,"obs","senha","tipo","O campo codigo_solicitante deve ser um número inteiro !"),
            ("123456789015422",12345,1001,"abc","usuario",True,0,"obs","senha","tipo","O campo operadora_registro_ans deve ser um número inteiro !"),
            ("123456789015222",12345,1001,123456,123456,True,0,"obs","senha","tipo","O campo login deve ser um texto !"),
            ("123456789014949",12345,1001,123456,"usuario","abc",0,"obs","senha","tipo","O campo indicacao_clinica deve ser um booleano !"),
            ("123456789012333",12345,1001,123456,"usuario",True,"abc","obs","senha","tipo","O campo indicacao_acidente deve ser um número inteiro !"),
            ("123456789012211",12345,1001,123456,"usuario",True,0,123456,"senha","tipo","O campo observacao deve ser um texto !"),
            ("123456789012111",12345,1001,123456,"usuario",True,0,"obs",123456,"tipo","O campo senha deve ser um texto !"),
            ("123456789012321",12345,1001,123456,"usuario",True,0,"obs","senha",123456,"O campo tipo_transacao deve ser um texto !")
])
def test_deve_ocorrer_falha_no_cadastro_na_execucao_sp_sadt_pois_alguns_dados_enviados_nao_tem_o_tipo_correto(execucao_spsadt_mark_parametrize,response):
    
    logging.debug(execucao_spsadt_mark_parametrize)

    assert execucao_spsadt_mark_parametrize["message"] == response
    assert execucao_spsadt_mark_parametrize["status_code"] == 400

@mark.parametrize("codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,response_expected,interacao",
        [
                    ("123452289012344", 23232, 1001, 2323,"O codigo_beneficiario não está cadastrado !",0),
                    ("", 23232, 1001, 2313,"O codigo_contratado não está cadastrado !",1),
                    ("", "", 1001, 4332,"O codigo_solicitante não está cadastrado !",2),
                    ("", "", "", 2211,"O operadora_registro_ans não está cadastrado !",3),
        ])
def test_nao_deve_ser_cadastrado_a_execucao_sp_sadt_pois_a_codigos_com_vinculos_externos_enviados_que_nao_existem(app,codigo_beneficiario,codigo_contratado,codigo_solicitante,
operadora_registro_ans,response_expected,interacao,request_fixture,beneficiario_no_mark_parametrize_scope_session,contratado_no_mark_parametrize_scope_session,
solicitante_no_mark_parametrize_scope_session,operadora_no_mark_parametrize_scope_session):
    
    use_codigo_criado_nas_fixtures_conforme_interacao = [
        ["fixture_beneficiario","fixture_contratado","fixture_solicitante","fixture_operadora"],
        [False,False,False,False],
        [True,False,False,False],
        [True,True,False,False],
        [True,True,True,False]
    ]

    start = interacao + 1

    response = request_fixture.post(f"{settings.BASE_URL}/execucao_spsadt", json={
            "codigo_beneficiario": beneficiario_no_mark_parametrize_scope_session['data']['numero_carteira'] if use_codigo_criado_nas_fixtures_conforme_interacao[start][0] else codigo_beneficiario,
            "codigo_contratado": contratado_no_mark_parametrize_scope_session['data']['codigo_prestador_na_operadora'] if use_codigo_criado_nas_fixtures_conforme_interacao[start][1] else codigo_contratado,
            "codigo_solicitante": solicitante_no_mark_parametrize_scope_session['data']['codigo_solicitante'] if use_codigo_criado_nas_fixtures_conforme_interacao[start][2] else codigo_solicitante,
            "operadora_registro_ans": operadora_no_mark_parametrize_scope_session['data']['registro_ans'] if use_codigo_criado_nas_fixtures_conforme_interacao[start][3] else operadora_registro_ans,
            "login": "paciente@gmail.com",
            "indicacao_clinica": True,
            "indicacao_acidente": 1,
            "observacao": "ss",
            "senha": "sdsd",
            "tipo_transacao": "SOLICITACAO_AUTORIZACAO"
        })

    response_json = response.json()

    assert response_json["message"] == response_expected
    assert response.status_code == 404
    
   