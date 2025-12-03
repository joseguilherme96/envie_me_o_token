from src.fake.fake_request_sp_sadt_data_xml import FakeRequestSPSADTDataXML
from src.routes.v1.enviar_token_paciente.request_sp_sadt_data_xml import RequestSPSADTDataXML
from dotenv import load_dotenv
from config import settings

class FactoryRequestSPSADTDataXML:

     @staticmethod
     def create(dados_sp_sadt_db):

        load_dotenv(dotenv_path="api/.env")

        if settings.ENV_FOR_DYNACONF == "testing" and settings.USE_CLASS_FAKE:

            return FakeRequestSPSADTDataXML(dados_sp_sadt_db)

        return RequestSPSADTDataXML(dados_sp_sadt_db)