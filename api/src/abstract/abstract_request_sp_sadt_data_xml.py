from abc import ABC, abstractmethod


class AbstractRequestSPSADTDataXML(ABC):
    @abstractmethod
    def __init__(self, dados_sp_sadt_db):

        self.dados_sp_sadt_db = dados_sp_sadt_db
        self.xml = None
        self.path_template = ""

    @abstractmethod
    def construir_xml(self):

        self.xml = ""
