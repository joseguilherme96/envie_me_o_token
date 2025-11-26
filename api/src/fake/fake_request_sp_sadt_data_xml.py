from src.abstract.abstract_request_sp_sadt_data_xml import AbstractRequestSPSADTDataXML

class FakeRequestSPSADTDataXML(AbstractRequestSPSADTDataXML):

    def __init__(self,dados_sp_sadt_db):

        self.dados_sp_sadt_db = dados_sp_sadt_db
        self.xml = None
        self.path_template = ""

    def construir_xml(self):

        self.xml = f"<xml><Paciente>Henrique</Paciente><NumeroCarterinha>32424242242424242</NumeroCarterinha></xml>"

