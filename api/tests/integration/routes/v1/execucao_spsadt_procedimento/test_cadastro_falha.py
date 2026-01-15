from pytest import mark
from config import settings


@mark.parametrize("codigo_procedimento,codigo_execucao,descricao_procedimento,quantidade_solicitada,response_message,response_status_code,index",[
    ("",1,"Fisioterapia",10,"O campo codigo_procedimento deve ser preenchido !",400,0),
    (1,"","Fisioterapia",10,"O campo codigo_execucao deve ser preenchido !",400,1),
    (1,1,"",10,"O campo descricao_procedimento deve ser preenchido !",400,2),
    (1,1,"Fisioterapia","","O campo quantidade_solicitada deve ser preenchido !",400,3),
])
def test_deve_ocorrer_falha_no_cadastro_devido_aos_campos_estarem_em_brancos(execucao_spsadt_no_mark_parametrize_option_2, client_app,codigo_procedimento,codigo_execucao,descricao_procedimento,quantidade_solicitada,response_message,response_status_code,index):

    usar_codigo_cadastrado = [
        [False,False],
        [False,False],
        [False,True],
        [False,True],
    ]


    payload = {
        "codigo_procedimento": codigo_procedimento,
        "codigo_execucao" : execucao_spsadt_no_mark_parametrize_option_2["data"]["codigo_execucao"] if usar_codigo_cadastrado[index][1] else codigo_execucao,
        "descricao_procedimento": descricao_procedimento,
        "quantidade_solicitada": quantidade_solicitada

    }

    response = client_app.post(f"{settings.BASE_URL}/execucao_spsadt_procedimento",json=payload)
    response_json =response.json

    assert response_json["message"] == response_message
    assert response.status_code == response_status_code

@mark.parametrize("codigo_procedimento,codigo_execucao,descricao_procedimento,quantidade_solicitada,response_message,response_status_code,index",[
    ("sdsdsd",1,"Fisioterapia",10,"O campo codigo_procedimento deve ser um numero inteiro !",400,0),
    (12121,"sdsdsd","Fisioterapia",10,"O campo codigo_execucao deve ser um numero inteiro !",400,1),
    (1,1,"Fisioterapia","adad","O campo quantidade_solicitada deve ser um numero inteiro !",400,2),
])
def test_alguns_campos_enviados_devem_ser_numeros_inteiros(execucao_spsadt_no_mark_parametrize_option_2, client_app,codigo_procedimento,codigo_execucao,descricao_procedimento,quantidade_solicitada,response_message,response_status_code,index):
    
    usar_codigo_cadastrado = [
        [False,False],
        [False,False],
        [False,True],
        [False,True],
    ]


    payload = {
        "codigo_procedimento": codigo_procedimento,
        "codigo_execucao" : execucao_spsadt_no_mark_parametrize_option_2["data"]["codigo_execucao"] if usar_codigo_cadastrado[index][1] else codigo_execucao,
        "descricao_procedimento": descricao_procedimento,
        "quantidade_solicitada": quantidade_solicitada

    }

    response = client_app.post(f"{settings.BASE_URL}/execucao_spsadt_procedimento",json=payload)
    response_json =response.json

    assert response_json["message"] == response_message
    assert response.status_code == response_status_code

def test_o_valor_do_campo_descricao_enviado_deve_ser_um_texto(execucao_spsadt_no_mark_parametrize_option_3,client_app):

    payload = {
        "codigo_procedimento": 1,
        "codigo_execucao" : 1,
        "descricao_procedimento": 1,
        "quantidade_solicitada": 1

    }

    response = client_app.post(f"{settings.BASE_URL}/execucao_spsadt_procedimento",json=payload)
    response_json =response.json

    assert response_json["message"] == "O campo descricao_procedimento deve ser um texto !"
    assert response.status_code == 400

def test_o_valor_codigo_execucao_enviado_nao_deve_ser_valido(execucao_spsadt_no_mark_parametrize_option_3,client_app):

    payload = {
        "codigo_procedimento": 1,
        "codigo_execucao" : 122323,
        "descricao_procedimento": "Fisioterapia",
        "quantidade_solicitada": 1

    }

    response = client_app.post(f"{settings.BASE_URL}/execucao_spsadt_procedimento",json=payload)
    response_json =response.json

    assert response_json["message"] == "Não foi encontrado o codigo_execucao informado !"
    assert response.status_code == 404

