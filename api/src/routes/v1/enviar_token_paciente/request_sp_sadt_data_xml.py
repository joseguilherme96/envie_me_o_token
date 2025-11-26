from src.abstract.abstract_request_sp_sadt_data_xml import AbstractRequestSPSADTDataXML

class RequestSPSADTDataXML(AbstractRequestSPSADTDataXML):

    def __init__(self,dados_sp_sadt_db):

        self.dados_sp_sadt_db = dados_sp_sadt_db
        self.xml = None
        self.path_template = ""

    def construir_xml(self):

        self.xml =""

