from src.factory.factory_request_spsadt import FactoryRequestSPSADT
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv


@patch("requests.post")
def test_a_execucao_da_requisicao_sp_sadt_deve_ser_feita_com_sucesso(
    mock_request_post, template_data_xml_request, template_data_xml_response
):

    response = MagicMock()
    response.status_code = 201
    response.text = template_data_xml_response
    mock_request_post.return_value = response

    request_sp_sadt = FactoryRequestSPSADT.create("http://apifake.com")
    ler_todo_conteudo_solicitacao_xml = template_data_xml_request.format(
        tipo_transacao="",
        sequencial_transacao="",
        data_registro_transacao="",
        hora_registro_transacao="",
        codigo_prestador_na_operadora="",
        registro_ANS="",
        numero_guia_operadora="",
        padrao="",
        login_prestador="",
        senha_prestador="",
        numero_guia_prestador="",
        tipo_etapa_autorizacao="",
        numero_carteira="",
        atendimento_rn="",
        nome_beneficiario="",
        identificador_beneficiario="",
        codigo_prestado_na_operadora="",
        nome_contratado="",
        nome_profissional="",
        conselho_profissional="",
        numero_conselho_profissional="",
        uf="",
        cbos="",
        carater_atendimento="",
        data_solicitacao="",
        indicacao_clinica="",
        tipo_atendimento="",
        indicacao_acidente="",
        codigo_procedimento="",
        descricao_procedimento="",
        quantidade_solicitada="",
        codigo_operadora="",
        observacao="",
        hash="",
    )
    status_code, text = request_sp_sadt.executar_request_sp_sadt(
        ler_todo_conteudo_solicitacao_xml
    )
    assert template_data_xml_response == text
