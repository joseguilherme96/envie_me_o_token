from src.fake.fake_execucao_sp_sadat import FakeExecucaoSPSADAT
from src.rpa.execucao_sp_sadat import ExecucaoSPSADAT
import os
from dotenv import load_dotenv

class FactoryExecucaoSPSADT:

     @staticmethod
     def create(uri,dados_sp_sadat):

        load_dotenv(dotenv_path="api/.env")

        if os.getenv("ENV_FOR_DYNACONF") == "test":

            return FakeExecucaoSPSADAT(uri,dados_sp_sadat)

        return ExecucaoSPSADAT(uri,dados_sp_sadat)

        
