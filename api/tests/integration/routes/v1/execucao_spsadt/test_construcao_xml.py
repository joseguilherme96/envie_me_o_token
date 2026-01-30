from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
from src.factory.factory_request_sp_sadt_data_xml import FactoryRequestSPSADTDataXML
import xml.etree.ElementTree as ET
from tests.utils.find_element_xml import find,find_all

def test_deve_contruir_xml_para_execucao_sp_sadt(execucao_spsadt_no_mark_parametrize,beneficiario_no_mark_parametrize_scope_session,contratado_no_mark_parametrize_scope_session,
                                                   solicitante_no_mark_parametrize_scope_session,operadora_no_mark_parametrize_scope_session,execucao_spsadt_procedimento_no_mark_parametrize,caplog):

    api_token_paciente = APITokenPaciente() 
    api_token_paciente.buscar_dados_para_execucao_sp_sadt(execucao_spsadt_no_mark_parametrize['data']['codigo_execucao'])

    factory_request_sp_sadt_data_xml = FactoryRequestSPSADTDataXML.create(api_token_paciente.dados_exec_sp_sadat)
    factory_request_sp_sadt_data_xml.construir_xml()

    xml = ET.fromstring(factory_request_sp_sadt_data_xml.xml)

    prefix = "sch"
    path_prefix = f".//{prefix}:"

    tipo_transacao = find(xml,f"{path_prefix}tipoTransacao")
    assert tipo_transacao is not None
    assert tipo_transacao.text == execucao_spsadt_no_mark_parametrize["data"]["tipo_transacao"]

    sequencial_transacao = find(xml,f"{path_prefix}sequencialTransacao")
    assert sequencial_transacao is not None
    assert sequencial_transacao.text == str(execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"])

    data_registro_transacao = find(xml, f"{path_prefix}dataRegistroTransacao")
    assert data_registro_transacao is not None

    hora_registro_transacao = find(xml, f"{path_prefix}horaRegistroTransacao")
    assert hora_registro_transacao is not None

    codigo_prestador_na_operadora = find_all(xml,f"{path_prefix}codigoPrestadorNaOperadora")[0]
    assert codigo_prestador_na_operadora is not None
    assert codigo_prestador_na_operadora.text == str(execucao_spsadt_no_mark_parametrize["data"]["codigo_contratado"])

    registro_ans = find(xml, f"{path_prefix}registroANS")
    assert registro_ans is not None
    assert registro_ans.text == str(operadora_no_mark_parametrize_scope_session["data"]["registro_ans"])

    padrao = find(xml, f"{path_prefix}Padrao")
    assert padrao is not None

    login_prestador = find(xml, f"{path_prefix}loginPrestador")
    assert login_prestador is not None
    assert login_prestador.text == execucao_spsadt_no_mark_parametrize["data"]["login"]

    senha_prestador = find(xml, f"{path_prefix}senhaPrestador")
    assert senha_prestador is not None
    assert senha_prestador.text == execucao_spsadt_no_mark_parametrize["data"]["senha"]

    cabecalho_solicitacao_registro_ans = find(xml, f"{path_prefix}cabecalhoSolicitacao/{prefix}:registroANS")
    assert cabecalho_solicitacao_registro_ans is not None
    assert cabecalho_solicitacao_registro_ans.text == str(operadora_no_mark_parametrize_scope_session["data"]["registro_ans"])

    numero_guia_prestador = find(xml, f"{path_prefix}numeroGuiaPrestador")
    assert numero_guia_prestador is not None
    assert numero_guia_prestador.text == str(execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"])

    numero_carteira = find(xml, f"{path_prefix}numeroCarteira")
    assert numero_carteira is not None
    assert numero_carteira.text == beneficiario_no_mark_parametrize_scope_session["data"]["numero_carteira"]

    atendimento_rn = find(xml, f"{path_prefix}atendimentoRN")
    assert atendimento_rn is not None
    expected_rn = "S" if beneficiario_no_mark_parametrize_scope_session["data"]["atendimento_rn"] else "N"
    assert atendimento_rn.text == expected_rn

    nome_beneficiario = find(xml, f"{path_prefix}nomeBeneficiario")
    assert nome_beneficiario is not None
    assert nome_beneficiario.text == beneficiario_no_mark_parametrize_scope_session["data"]["nome_beneficiario"]

    identificador_beneficiario = find(xml, f"{path_prefix}identificadorBeneficiario")
    assert identificador_beneficiario is not None
    assert identificador_beneficiario.text == beneficiario_no_mark_parametrize_scope_session["data"]["numero_carteira"]

    codigo_prestado_na_operadora = find_all(xml, f"{path_prefix}codigoPrestadorNaOperadora")[1]
    assert codigo_prestado_na_operadora is not None
    assert codigo_prestado_na_operadora.text == str(solicitante_no_mark_parametrize_scope_session["data"]["codigo_solicitante"])

    nome_contratado = find(xml, f"{path_prefix}nomeContratado")
    assert nome_contratado is not None
    assert nome_contratado.text == contratado_no_mark_parametrize_scope_session["data"]["nome_contratado"]

    nome_profissional = find(xml, f"{path_prefix}nomeProfissional")
    assert nome_profissional is not None
    assert nome_profissional.text == solicitante_no_mark_parametrize_scope_session["data"]["profissional_solicitante"]

    conselho_profissional = find(xml, f"{path_prefix}conselhoProfissional")
    assert conselho_profissional is not None
    assert conselho_profissional.text == str(solicitante_no_mark_parametrize_scope_session["data"]["conselho_profissional"])

    numero_conselho_profissional = find(xml, f"{path_prefix}numeroConselhoProfissional")
    assert numero_conselho_profissional is not None
    assert numero_conselho_profissional.text == solicitante_no_mark_parametrize_scope_session["data"]["numero_conselho_profissional"]

    uf = find(xml, f"{path_prefix}UF")
    assert uf is not None
    assert uf.text == str(solicitante_no_mark_parametrize_scope_session["data"]["uf"])

    cbos = find(xml, f"{path_prefix}CBOS")
    assert cbos is not None
    assert cbos.text == str(solicitante_no_mark_parametrize_scope_session["data"]["cbos"])

    carater_atendimento = find(xml, f"{path_prefix}caraterAtendimento")
    assert carater_atendimento is not None
    assert carater_atendimento.text == contratado_no_mark_parametrize_scope_session["data"]["carater_atendimento"]

    indicacao_clinica = find(xml, f"{path_prefix}indicacaoClinica")
    assert indicacao_clinica is not None
    assert indicacao_clinica.text == str(execucao_spsadt_no_mark_parametrize["data"]["indicacao_clinica"])

    tipo_atendimento = find(xml, f"{path_prefix}tipoAtendimento")
    assert tipo_atendimento is not None
    assert tipo_atendimento.text == contratado_no_mark_parametrize_scope_session["data"]["tipo_atendimento"]

    indicacao_acidente = find(xml, f"{path_prefix}indicacaoAcidente")
    assert indicacao_acidente is not None
    assert indicacao_acidente.text == str(execucao_spsadt_no_mark_parametrize["data"]["indicacao_acidente"])

    codigo_procedimento = find(xml, f"{path_prefix}codigoProcedimento")
    assert codigo_procedimento is not None
    assert codigo_procedimento.text == str(execucao_spsadt_procedimento_no_mark_parametrize["data"]["codigo_procedimento"])

    descricao_procedimento = find(xml, f"{path_prefix}descricaoProcedimento")
    assert descricao_procedimento is not None
    assert descricao_procedimento.text == execucao_spsadt_procedimento_no_mark_parametrize["data"]["descricao_procedimento"]

    quantidade_solicitada = find(xml, f"{path_prefix}quantidadeSolicitada")
    assert quantidade_solicitada is not None
    assert quantidade_solicitada.text == str(execucao_spsadt_procedimento_no_mark_parametrize["data"]["quantidade_solicitada"])

    codigo_na_operadora = find(xml, f"{path_prefix}codigonaOperadora")
    assert codigo_na_operadora is not None
    assert codigo_na_operadora.text == str(operadora_no_mark_parametrize_scope_session["data"]["registro_ans"])

    nome_contratado = find(xml, f"{path_prefix}nomeContratado")
    assert nome_contratado is not None
    assert nome_contratado.text == contratado_no_mark_parametrize_scope_session["data"]["nome_contratado"]
    
    cnes = find(xml, f"{path_prefix}CNES")
    assert cnes is not None

    observacao = find(xml, f"{path_prefix}observacao")
    assert observacao is not None
    assert observacao.text == execucao_spsadt_no_mark_parametrize["data"]["observacao"]
    
