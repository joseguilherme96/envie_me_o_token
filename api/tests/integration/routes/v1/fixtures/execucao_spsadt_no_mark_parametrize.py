from pytest import fixture
import requests
from config import settings
import logging

@fixture(scope="function")
def execucao_spsadt_no_mark_parametrize(app,endpoint,get_data_execucao_spsadt,beneficiario_no_mark_parametrize,contratado_no_mark_parametrize,
                                        solicitante_no_mark_parametrize,operadora_no_mark_parametrize,client_app):
    
    data = get_data_execucao_spsadt(beneficiario_no_mark_parametrize['data']["numero_carteira"],contratado_no_mark_parametrize['data']["codigo_prestador_na_operadora"],
                                    solicitante_no_mark_parametrize['data']["codigo_solicitante"],operadora_no_mark_parametrize['data']["registro_ans"],
                                    "paciente@gmail.com",True,True,"observacao","dmdm3","SOLICITACAO_AUTORIZACAO")

    response = client_app.post(endpoint("execucao_spsadt"), json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="function")
def execucao_spsadt_no_mark_parametrize_option_2(app,endpoint,get_data_execucao_spsadt,beneficiario_no_mark_parametrize_scope_session,contratado_no_mark_parametrize_scope_session,
                                        solicitante_no_mark_parametrize_scope_session,operadora_no_mark_parametrize_scope_session,client_app):
    
    data = get_data_execucao_spsadt(beneficiario_no_mark_parametrize_scope_session['data']["numero_carteira"],contratado_no_mark_parametrize_scope_session['data']["codigo_prestador_na_operadora"],
                                    solicitante_no_mark_parametrize_scope_session['data']["codigo_solicitante"],operadora_no_mark_parametrize_scope_session['data']["registro_ans"],
                                    "paciente@gmail.com",True,True,"observacao","dmdm3","SOLICITACAO_AUTORIZACAO")

    response = client_app.post(endpoint("execucao_spsadt"), json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json

@fixture(scope="session")
def execucao_spsadt_no_mark_parametrize_option_3(app,endpoint,get_data_execucao_spsadt,beneficiario_no_mark_parametrize_scope_session,contratado_no_mark_parametrize_scope_session,
                                        solicitante_no_mark_parametrize_scope_session,operadora_no_mark_parametrize_scope_session,client_app):
    
    data = get_data_execucao_spsadt(beneficiario_no_mark_parametrize_scope_session['data']["numero_carteira"],contratado_no_mark_parametrize_scope_session['data']["codigo_prestador_na_operadora"],
                                    solicitante_no_mark_parametrize_scope_session['data']["codigo_solicitante"],operadora_no_mark_parametrize_scope_session['data']["registro_ans"],
                                    "paciente@gmail.com",True,True,"observacao","dmdm3","SOLICITACAO_AUTORIZACAO")

    response = client_app.post(endpoint("execucao_spsadt"), json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json