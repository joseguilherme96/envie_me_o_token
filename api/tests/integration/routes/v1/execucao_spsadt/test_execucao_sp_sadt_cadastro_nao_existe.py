from pytest import mark
import logging

@mark.parametrize("""codigo_beneficiario,codigo_contratado,codigo_solicitante,operadora_registro_ans,login,
indicacao_clinica,indicacao_acidente,observacao,senha,tipo_transacao,response""",[
    ("1234567834343",12345,1001,123456,"usuario_teste",True,0,"Observação teste","SENHA123","SOLICITACAO_AUTORIZACAO","O codigo_beneficiario não está cadastrado !")
])
def test_nao_deve_ser_possivel_realizar_o_cadastro_da_execucao_sp_sadt_devido_colunas_que_fazem_vinculos_com_registros_de_outras_tabelas_nao_existirem(execucao_spsadt_mark_parametrize,response):

    logging.debug(execucao_spsadt_mark_parametrize)

    assert execucao_spsadt_mark_parametrize["message"] == response
    assert execucao_spsadt_mark_parametrize["status_code"] == 404

