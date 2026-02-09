from unittest.mock import patch, MagicMock
from src.factory.factory_execucao_sp_sadt import FactoryExecucaoSPSADT
from pytest import raises


@patch("requests.post")
def test_deve_autorizar_paciente(
    mock_response, template_data_xml_request, template_data_xml_response
):

    response = MagicMock()
    response.status_code = 201
    response.text = template_data_xml_response.format(
        tipo_transacao="RESPOSTA_SOLICITACAO",
        sequencial_transacao="1111",
        data_registro="2016-12-01",
        hora_registro="12:00:00",
        registro_ans="111111",
        cnpj="00111222000100",
        padrao="3.03.01",
        login="TESTE001",
        senha="9c4c9c4c9c4c9c4c9c4c9c4c9c4c9c4c",
        guia_prestador="1111",
        guia_operadora="2222",
        data_autorizacao="2016-12-01",
        senha_autorizacao="000000001",
        numero_carteira="1111111111111",
        atendimento_rn="N",
        nome_beneficiario="BENEFICIARIO",
        codigo_prestador="1111",
        nome_contratado="CONTRATADO",
        cnes="9999999",
        status_solicitacao="1",
        codigo_tabela="22",
        codigo_procedimento="40101010",
        descricao_procedimento="ECG CONVENCIONAL DE AT",
        quantidade_solicitada="1",
        quantidade_autorizada="1",
        hash="A551AF234DF921F8AA6CEAC4E2FE579D",
    )

    mock_response.return_value = response

    dados_sp_sadat = template_data_xml_request.format(
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
    execucao_sp_sadt = FactoryExecucaoSPSADT.create(
        "http://apifake.com", dados_sp_sadat
    )
    execucao_sp_sadt.solicitar_autorizacao()

    assert response.text == execucao_sp_sadt.response


@patch("requests.post")
def test_deve_levantar_uma_excecao_ao_nao_passar_todos_os_dados_para_execucao_sp_sadt(
    mock_response, template_data_xml_request, template_data_xml_response
):

    with raises(TypeError):
        response = MagicMock()
        response.status_code = 201
        response.text = template_data_xml_response.format(
            tipo_transacao="RESPOSTA_SOLICITACAO",
            sequencial_transacao="1111",
            data_registro="2016-12-01",
            hora_registro="12:00:00",
            registro_ans="111111",
            cnpj="00111222000100",
            padrao="3.03.01",
            login="TESTE001",
            senha="9c4c9c4c9c4c9c4c9c4c9c4c9c4c9c4c",
            guia_prestador="1111",
            guia_operadora="2222",
            data_autorizacao="2016-12-01",
            senha_autorizacao="000000001",
            numero_carteira="1111111111111",
            atendimento_rn="N",
            nome_beneficiario="BENEFICIARIO",
            codigo_prestador="1111",
            nome_contratado="CONTRATADO",
            cnes="9999999",
            status_solicitacao="1",
            codigo_tabela="22",
            codigo_procedimento="40101010",
            descricao_procedimento="ECG CONVENCIONAL DE AT",
            quantidade_solicitada="1",
            quantidade_autorizada="1",
            hash="A551AF234DF921F8AA6CEAC4E2FE579D",
        )
        mock_response.return_value = template_data_xml_response

        template_data_xml_request.format(
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
        execucao_sp_sadt = FactoryExecucaoSPSADT.create("http://apifake.com")
        execucao_sp_sadt.solicitar_autorizacao()

        assert template_data_xml_response == execucao_sp_sadt.response
