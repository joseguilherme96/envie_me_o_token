from src.abstract.abstract_execucao_sp_sadat import AbstractExecucaoSPSADAT
from src.fake.fake_resquest_execucao_sp_sadat import FakeRequestSPSADT
import logging
from utils.DataXMLExecucaoSPSADT import DataXMLExecucaoSPSADT
from lxml import etree
from pathlib import Path
from config import settings


class ExecucaoSPSADAT(AbstractExecucaoSPSADAT):
    def __init__(self, uri, dados_sp_sadat):

        self.dados_sp_sadat = dados_sp_sadat
        self.uri = uri
        self.status_code = None
        self.response = None
        self.processado = False

    def processar_rpa(self):

        try:
            self.validar_xml_contra_xsd()
            self.solicitar_autorizacao()
            self.validar_autorizacao()
            self.salvar_autorizacao()

            self.processado = True

        except Exception as e:
            self.processado = False
            raise e

    def validar_xml_contra_xsd(self):

        xml = etree.fromstring(self.dados_sp_sadat.encode("utf-8"))
        namespaces = {
            "soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
            "sch": "http://www.ans.gov.br/padroes/tiss/schemas",
        }
        data_xml = DataXMLExecucaoSPSADT(xml, namespaces)

        try:
            solicitacao_procedimento_ws = data_xml.find_or_error(
                ".//sch:solicitacaoProcedimentoWS"
            )

            BASE_DIR = Path(settings.BASE_PATH_MODELO_TEMPLATE)
            xsd_path = BASE_DIR / "xsd/tissWebServicesV3_05_00_xsd.xml"
            xmlschema_doc = etree.parse(xsd_path)
            schema = etree.XMLSchema(xmlschema_doc)
            schema.assertValid(solicitacao_procedimento_ws)

            logging.debug("XML é válido!")

            return True

        except etree.DocumentInvalid:
            logging.debug("XML é inválido")
            raise {
                "message": "XML inválido para autorizar SPSADT !",
                "status_code": 500,
            }

        except Exception:
            logging.debug("Erro:")
            raise {
                "message": "Erro desconhecido ao validar xml contra xsd !",
                "status_code": 500,
            }

    def solicitar_autorizacao(self):

        logging.info("Solicitando autorização no Web Service SOAP...")
        request = FakeRequestSPSADT("http://apifake.com")
        self.status_code, self.response = request.executar_request_sp_sadt(
            self.dados_sp_sadat
        )

    def validar_autorizacao(self):

        pass

    def salvar_autorizacao(self):

        pass
