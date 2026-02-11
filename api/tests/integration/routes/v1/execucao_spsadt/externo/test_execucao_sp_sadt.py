from pathlib import Path
from config import settings
import xml.etree.ElementTree as ET
from utils.find_element_xml import find
from random import randint
import logging
from src.rpa.request_execucao_sp_sadat import RequestSPSADAT
from pytest import mark


@mark.test_workflow_dispatch
def test_deve_autorizar_paciente():

    template = Path(f"{settings.BASE_PATH_MODELO_TEMPLATE}/data_request_sp_sadt_v1.xml")

    with open(template, "r"):
        xml = template.read_text()

    xml_format = xml.format(
        tipo_transacao=settings.TIPO_TRANSACAO,
        sequencial_transacao=settings.SEQUENCIAL_TRANSACAO,
        data_registro_transacao=settings.DATA,
        hora_registro_transacao=settings.HORA,
        codigo_prestador_na_operadora=settings.CODIGO_PRESTADOR_NA_OPERADORA,
        registro_ANS=settings.REGISTRO_ANS,
        padrao=settings.PADRAO,
        numero_guia_prestador=randint(1, 9999999999),
        tipo_etapa_autorizacao=settings.TIPO_ETAPA_AUTORIZACAO,
        numero_carteira=settings.NUMERO_CARTEIRA,
        atendimento_rn=settings.ATENDIMENTO_RN,
        nome_beneficiario=settings.NOME_BENEFICIARIO,
        nome_contratado=settings.NOME_CONTRATADO,
        nome_profissional=settings.NOME_PROFISSIONAL,
        conselho_profissional=settings.CONSELHO_PROFISSIONAL,
        numero_conselho_profissional=settings.NUMERO_CONSELHO_PROFISSIONAL,
        uf=settings.UF,
        cbos=settings.CBOS,
        carater_atendimento=settings.CARATER_ATENDIMENTO,
        data_solicitacao=settings.DATA_SOLICITACAO,
        indicacao_clinica=settings.INDICACAO_CLINICA,
        codigo_tabela=settings.CODIGO_TABELA,
        codigo_procedimento=settings.CODIGO_PROCEDIMENTO,
        descricao_procedimento=settings.DESCRICAO_PROCEDIMENTO,
        quantidade_solicitada=settings.QUANTIDADE_SOLICITADA,
        cnes=settings.CNES,
        observacao=settings.OBSERVACAO,
        hash=settings.HASH,
    )

    api_terceiro = RequestSPSADAT(settings.DYNACONF_URL_EXECUCAO_SP_SADT_HOMOLOGACAO)
    status_code, text = api_terceiro.executar_request_sp_sadt(data=xml_format)

    logging.debug(f"Response: {text}")

    assert status_code == 200

    xml = ET.fromstring(text)
    quantidade_autorizada = find(xml, ".//sch:quantidadeAutorizada")
    descricao_glosa = find(xml, ".//sch:descricaoGlosa")

    assert quantidade_autorizada.text == "1"
    assert descricao_glosa is None
