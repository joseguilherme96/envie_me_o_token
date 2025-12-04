from src.abstract.abstract_execucao_sp_sadat import AbstractExecucaoSPSADAT
from src.fake.fake_resquest_execucao_sp_sadat import FakeRequestSPSADT
import logging

class ExecucaoSPSADAT(AbstractExecucaoSPSADAT):

    def __init__(self,uri,dados_sp_sadat):

        self.dados_sp_sadat = dados_sp_sadat
        self.uri = uri
        self.status_code = None
        self.response = None
        self.processado = False

    def processar_rpa(self):

        pass

    def validar_dados_a_enviar(self):

        pass

    def solicitar_autorizacao(self):

        logging.info("Solicitando autorização...")
        request = FakeRequestSPSADT("http://apifake.com")
        self.status_code, self.response = request.executar_request_sp_sadt(self.dados_sp_sadat)

    def validar_autorizacao(self):

        pass

    def salvar_autorizacao(self):

        pass

    
    