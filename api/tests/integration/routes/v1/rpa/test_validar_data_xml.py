import logging
from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
from src.factory.factory_request_sp_sadt_data_xml import FactoryRequestSPSADTDataXML
from src.rpa.execucao_sp_sadat import ExecucaoSPSADAT
from config import settings
from pytest import mark


@mark.homologacao
def test_ao_construir_xml_para_execucao_sp_sadt_os_dados_devem_ser_validos_para_serem_enviados(
    execucao_spsadt_no_mark_parametrize,
    beneficiario_no_mark_parametrize_scope_session,
    contratado_no_mark_parametrize_scope_session,
    solicitante_no_mark_parametrize_scope_session,
    operadora_no_mark_parametrize_scope_session,
    execucao_spsadt_procedimento_no_mark_parametrize,
):

    codigo_execucao = execucao_spsadt_no_mark_parametrize["data"]["codigo_execucao"]
    logging.debug(codigo_execucao)

    api_token_paciente = APITokenPaciente()
    api_token_paciente.buscar_dados_para_execucao_sp_sadt(codigo_execucao)

    xml_data = FactoryRequestSPSADTDataXML.create(
        api_token_paciente.dados_exec_sp_sadat
    )
    xml_data.construir_xml()

    logging.debug(xml_data.xml)

    execucao_sp_sadt = ExecucaoSPSADAT(
        settings.URL_EXECUCAO_SP_SADT_HOMOLOGACAO, xml_data.xml
    )

    try:
        execucao_sp_sadt.validar_xml_contra_xsd()

        assert True

    except Exception as error:
        logging.error(error)
        assert False
