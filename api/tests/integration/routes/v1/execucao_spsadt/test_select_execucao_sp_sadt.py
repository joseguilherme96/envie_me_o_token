from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
from pytest import raises

def test_deve_retornar_dados_para_execucao_sp_sadt(execucao_spsadt_no_mark_parametrize,beneficiario_no_mark_parametrize_scope_session,contratado_no_mark_parametrize_scope_session,
                                                   solicitante_no_mark_parametrize_scope_session,operadora_no_mark_parametrize_scope_session,execucao_spsadt_procedimento_no_mark_parametrize):

    api_token_paciente = APITokenPaciente()
    api_token_paciente.buscar_dados_para_execucao_sp_sadt(execucao_spsadt_no_mark_parametrize['data']['codigo_execucao'])


    assert isinstance(api_token_paciente.dados_exec_sp_sadat,dict)
    assert api_token_paciente.dados_exec_sp_sadat == {
        "codigo_execucao":execucao_spsadt_no_mark_parametrize['data']["codigo_execucao"],
        "codigo_beneficiario":beneficiario_no_mark_parametrize_scope_session['data']["numero_carteira"],
        "codigo_contratado": contratado_no_mark_parametrize_scope_session['data']["codigo_prestador_na_operadora"],
        "codigo_solicitante":solicitante_no_mark_parametrize_scope_session['data']["codigo_solicitante"],
        "operadora_registro_ans":operadora_no_mark_parametrize_scope_session['data']["registro_ans"],
        'indicacao_clinica': execucao_spsadt_no_mark_parametrize['data']['indicacao_clinica'], 
        'observacao': execucao_spsadt_no_mark_parametrize['data']['observacao'],
        'tipo_transacao': execucao_spsadt_no_mark_parametrize['data']['tipo_transacao'],
        "login":execucao_spsadt_no_mark_parametrize['data']['login'],
        "indicacao_acidente":execucao_spsadt_no_mark_parametrize['data']['indicacao_acidente'],
        "senha":execucao_spsadt_no_mark_parametrize['data']['senha'],
        "beneficiario": {
            "numero_carteira":beneficiario_no_mark_parametrize_scope_session['data']["numero_carteira"],
            "atendimento_rn":beneficiario_no_mark_parametrize_scope_session["data"]["atendimento_rn"],
            "nome_beneficiario":beneficiario_no_mark_parametrize_scope_session["data"]['nome_beneficiario'],
        },
        "contratado": {
            "codigo_prestador_na_operadora": contratado_no_mark_parametrize_scope_session["data"]["codigo_prestador_na_operadora"],
            "nome_contratado": contratado_no_mark_parametrize_scope_session["data"]["nome_contratado"],
            "carater_atendimento": contratado_no_mark_parametrize_scope_session["data"]["carater_atendimento"],
            "tipo_atendimento": contratado_no_mark_parametrize_scope_session["data"]["tipo_atendimento"]
        },
        "solicitante": {
            "codigo_solicitante": solicitante_no_mark_parametrize_scope_session["data"]["codigo_solicitante"],
            "profissional_solicitante": solicitante_no_mark_parametrize_scope_session["data"]["profissional_solicitante"],
            "conselho_profissional": solicitante_no_mark_parametrize_scope_session["data"]["conselho_profissional"],
            "numero_conselho_profissional": solicitante_no_mark_parametrize_scope_session["data"]["numero_conselho_profissional"],
            "uf": solicitante_no_mark_parametrize_scope_session["data"]["uf"],
            "cbos": solicitante_no_mark_parametrize_scope_session["data"]["cbos"]
        },
        "operadora": {
            "registro_ans": operadora_no_mark_parametrize_scope_session["data"]["registro_ans"],
            "operadora": operadora_no_mark_parametrize_scope_session["data"]["operadora"]
        },
        "execucao_spsadt_procedimento": [
            {
                "codigo_procedimento": execucao_spsadt_procedimento_no_mark_parametrize["data"]["codigo_procedimento"],
                "codigo_execucao": execucao_spsadt_procedimento_no_mark_parametrize["data"]["codigo_execucao"],
                "descricao_procedimento": execucao_spsadt_procedimento_no_mark_parametrize["data"]["descricao_procedimento"],
                "quantidade_solicitada": execucao_spsadt_procedimento_no_mark_parametrize["data"]["quantidade_solicitada"]
            }
        ]
    }

def test_deve_falhar_a_busca_por_nao_ter_passado_nenhum_parametro():

    with raises(TypeError) as type_error:

        api_token_paciente = APITokenPaciente()
        api_token_paciente.buscar_dados_para_execucao_sp_sadt()
