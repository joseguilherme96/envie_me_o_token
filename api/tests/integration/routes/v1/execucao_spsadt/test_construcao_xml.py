from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
from src.factory.factory_request_sp_sadt_data_xml import FactoryRequestSPSADTDataXML
import xml.etree.ElementTree as ET
from tests.utils.find_element_xml import find, find_all


def test_deve_contruir_xml_para_execucao_sp_sadt(
    execucao_spsadt_no_mark_parametrize,
    beneficiario_no_mark_parametrize_scope_session,
    contratado_no_mark_parametrize_scope_session,
    solicitante_no_mark_parametrize_scope_session,
    operadora_no_mark_parametrize_scope_session,
    execucao_spsadt_procedimento_no_mark_parametrize,
    caplog,
):

    api_token_paciente = APITokenPaciente()
    api_token_paciente.buscar_dados_para_execucao_sp_sadt(
        execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"]
    )

    factory_request_sp_sadt_data_xml = FactoryRequestSPSADTDataXML.create(
        api_token_paciente.dados_exec_sp_sadat
    )
    factory_request_sp_sadt_data_xml.construir_xml()

    assert factory_request_sp_sadt_data_xml.xml is not None, "XML não foi construído"

    xml = ET.fromstring(factory_request_sp_sadt_data_xml.xml)

    tipo_transacao = find(xml, ".//sch:tipoTransacao")
    assert tipo_transacao is not None
    assert (
        tipo_transacao.text
        == execucao_spsadt_no_mark_parametrize["data"]["tipo_transacao"]
    )

    sequencial_transacao = find(xml, ".//sch:sequencialTransacao")
    assert sequencial_transacao is not None
    assert sequencial_transacao.text == str(
        execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"]
    )

    data_registro_transacao = find(xml, ".//sch:dataRegistroTransacao")
    assert data_registro_transacao is not None

    hora_registro_transacao = find(xml, ".//sch:horaRegistroTransacao")
    assert hora_registro_transacao is not None

    codigo_prestador_na_operadora = find_all(
        xml, ".//sch:codigoPrestadorNaOperadora"
    )[0]
    assert codigo_prestador_na_operadora is not None
    assert codigo_prestador_na_operadora.text == str(
        execucao_spsadt_no_mark_parametrize["data"]["codigo_contratado"]
    )

    registro_ans = find(xml, ".//sch:registroANS")
    assert registro_ans is not None
    assert registro_ans.text == str(
        operadora_no_mark_parametrize_scope_session["data"]["registro_ans"]
    )

    padrao = find(xml, ".//sch:Padrao")
    assert padrao is not None

    login_prestador = find(xml, ".//sch:loginPrestador")
    assert login_prestador is not None
    assert login_prestador.text == execucao_spsadt_no_mark_parametrize["data"]["login"]

    senha_prestador = find(xml, ".//sch:senhaPrestador")
    assert senha_prestador is not None
    assert senha_prestador.text == execucao_spsadt_no_mark_parametrize["data"]["senha"]

    cabecalho_solicitacao_registro_ans = find(
        xml, ".//sch:cabecalhoSolicitacao/sch:registroANS"
    )
    assert cabecalho_solicitacao_registro_ans is not None
    assert cabecalho_solicitacao_registro_ans.text == str(
        operadora_no_mark_parametrize_scope_session["data"]["registro_ans"]
    )

    numero_guia_prestador = find(xml, ".//sch:numeroGuiaPrestador")
    assert numero_guia_prestador is not None
    assert numero_guia_prestador.text == str(
        execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"]
    )

    numero_carteira = find(xml, ".//sch:numeroCarteira")
    assert numero_carteira is not None
    assert (
        numero_carteira.text
        == beneficiario_no_mark_parametrize_scope_session["data"]["numero_carteira"]
    )

    atendimento_rn = find(xml, ".//sch:atendimentoRN")
    assert atendimento_rn is not None
    expected_rn = (
        "S"
        if beneficiario_no_mark_parametrize_scope_session["data"]["atendimento_rn"]
        else "N"
    )
    assert atendimento_rn.text == expected_rn

    nome_beneficiario = find(xml, ".//sch:nomeBeneficiario")
    assert nome_beneficiario is not None
    assert (
        nome_beneficiario.text
        == beneficiario_no_mark_parametrize_scope_session["data"]["nome_beneficiario"]
    )

    identificador_beneficiario = find(xml, ".//sch:identificadorBeneficiario")
    assert identificador_beneficiario is not None
    assert (
        identificador_beneficiario.text
        == beneficiario_no_mark_parametrize_scope_session["data"]["numero_carteira"]
    )

    codigo_prestado_na_operadora = find_all(
        xml, ".//sch:codigoPrestadorNaOperadora"
    )[1]
    assert codigo_prestado_na_operadora is not None
    assert codigo_prestado_na_operadora.text == str(
        solicitante_no_mark_parametrize_scope_session["data"]["codigo_solicitante"]
    )

    nome_contratado = find(xml, ".//sch:nomeContratado")
    assert nome_contratado is not None
    assert (
        nome_contratado.text
        == contratado_no_mark_parametrize_scope_session["data"]["nome_contratado"]
    )

    nome_profissional = find(xml, ".//sch:nomeProfissional")
    assert nome_profissional is not None
    assert (
        nome_profissional.text
        == solicitante_no_mark_parametrize_scope_session["data"][
            "profissional_solicitante"
        ]
    )

    conselho_profissional = find(xml, ".//sch:conselhoProfissional")
    assert conselho_profissional is not None
    assert conselho_profissional.text == str(
        solicitante_no_mark_parametrize_scope_session["data"]["conselho_profissional"]
    )

    numero_conselho_profissional = find(xml, ".//sch:numeroConselhoProfissional")
    assert numero_conselho_profissional is not None
    assert (
        numero_conselho_profissional.text
        == solicitante_no_mark_parametrize_scope_session["data"][
            "numero_conselho_profissional"
        ]
    )

    uf = find(xml, ".//sch:UF")
    assert uf is not None
    assert uf.text == str(solicitante_no_mark_parametrize_scope_session["data"]["uf"])

    cbos = find(xml, ".//sch:CBOS")
    assert cbos is not None
    assert cbos.text == str(
        solicitante_no_mark_parametrize_scope_session["data"]["cbos"]
    )

    carater_atendimento = find(xml, ".//sch:caraterAtendimento")
    assert carater_atendimento is not None
    assert (
        carater_atendimento.text
        == contratado_no_mark_parametrize_scope_session["data"]["carater_atendimento"]
    )

    indicacao_clinica = find(xml, ".//sch:indicacaoClinica")
    assert indicacao_clinica is not None
    assert indicacao_clinica.text == str(
        execucao_spsadt_no_mark_parametrize["data"]["indicacao_clinica"]
    )

    tipo_atendimento = find(xml, ".//sch:tipoAtendimento")
    assert tipo_atendimento is not None
    assert (
        tipo_atendimento.text
        == contratado_no_mark_parametrize_scope_session["data"]["tipo_atendimento"]
    )

    indicacao_acidente = find(xml, ".//sch:indicacaoAcidente")
    assert indicacao_acidente is not None
    assert indicacao_acidente.text == str(
        execucao_spsadt_no_mark_parametrize["data"]["indicacao_acidente"]
    )

    codigo_procedimento = find(xml, ".//sch:codigoProcedimento")
    assert codigo_procedimento is not None
    assert codigo_procedimento.text == str(
        execucao_spsadt_procedimento_no_mark_parametrize["data"]["codigo_procedimento"]
    )

    descricao_procedimento = find(xml, ".//sch:descricaoProcedimento")
    assert descricao_procedimento is not None
    assert (
        descricao_procedimento.text
        == execucao_spsadt_procedimento_no_mark_parametrize["data"][
            "descricao_procedimento"
        ]
    )

    quantidade_solicitada = find(xml, ".//sch:quantidadeSolicitada")
    assert quantidade_solicitada is not None
    assert quantidade_solicitada.text == str(
        execucao_spsadt_procedimento_no_mark_parametrize["data"][
            "quantidade_solicitada"
        ]
    )

    codigo_na_operadora = find(xml, ".//sch:codigonaOperadora")
    assert codigo_na_operadora is not None
    assert codigo_na_operadora.text == str(
        operadora_no_mark_parametrize_scope_session["data"]["registro_ans"]
    )

    nome_contratado = find(xml, ".//sch:nomeContratado")
    assert nome_contratado is not None
    assert (
        nome_contratado.text
        == contratado_no_mark_parametrize_scope_session["data"]["nome_contratado"]
    )

    cnes = find(xml, ".//sch:CNES")
    assert cnes is not None

    observacao = find(xml, ".//sch:observacao")
    assert observacao is not None
    assert observacao.text == execucao_spsadt_no_mark_parametrize["data"]["observacao"]
