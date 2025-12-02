from src.fake.fake_resquest_execucao_sp_sadat import FakeRequestSPSADT
from src.rpa.request_execucao_sp_sadat import RequestSPSADAT
from dotenv import load_dotenv
from config import settings

class FactoryRequestSPSADT:

     @staticmethod
     def create(uri):

        load_dotenv(dotenv_path="api/.env")

        if settings.ENV_FOR_DYNACONF == "testing":

            return FakeRequestSPSADT(uri)

        return RequestSPSADAT(uri)

        
