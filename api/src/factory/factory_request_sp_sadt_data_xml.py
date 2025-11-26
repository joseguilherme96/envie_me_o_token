from src.fake.fake_request_sp_sadt_data_xml import FakeRequestSPSADTDataXML
from src.routes.v1.enviar_token_paciente.request_sp_sadt_data_xml import RequestSPSADTDataXML
import os
from dotenv import load_dotenv

class FactoryRequestSPSADTDataXML:

     @staticmethod
     def create(dados_sp_sadt_db):

        load_dotenv(dotenv_path="api/.env")

        if os.getenv("ENV_FOR_DYNACONF") == "test":

            return FakeRequestSPSADTDataXML(dados_sp_sadt_db)

        return RequestSPSADTDataXML(dados_sp_sadt_db)