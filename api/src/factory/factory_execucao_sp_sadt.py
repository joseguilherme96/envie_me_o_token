from src.fake.fake_execucao_sp_sadat import FakeExecucaoSPSADAT
from src.rpa.execucao_sp_sadat import ExecucaoSPSADAT
import os
from dotenv import load_dotenv
from config import settings
import logging


class FactoryExecucaoSPSADT:
    @staticmethod
    def create(uri, dados_sp_sadat):

        load_dotenv(dotenv_path="api/.env")

        logging.info("Criando instância de ExecucaoSPSADT...")

        if settings.ENV_FOR_DYNACONF == "testing" and settings.USE_CLASS_FAKE:
            classe = FakeExecucaoSPSADAT(uri, dados_sp_sadat)

        if not settings.USE_CLASS_FAKE:
            classe = ExecucaoSPSADAT(uri, dados_sp_sadat)

        logging.debug(classe)
        return classe
