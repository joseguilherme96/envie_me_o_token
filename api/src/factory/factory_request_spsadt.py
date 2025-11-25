from src.fake.fake_execucao_sp_sadat import FakeRequestSPSADT
from src.rpa.request_execucao_sp_sadat import RequestSPSADAT
import os
from dotenv import load_dotenv

class FactoryRequestSPSADT:

     @staticmethod
     def create(uri):

        load_dotenv(dotenv_path="api/.env")

        if os.getenv("ENV_FOR_DYNACONF") == "test":

            return FakeRequestSPSADT(uri)

        return RequestSPSADAT(uri)

        
