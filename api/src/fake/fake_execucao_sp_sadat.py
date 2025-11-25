from src.abstract.abstract_execucao_sp_sadat import AbstractExecucaoSPSADAT
from src.fake.fake_resquest_execucao_sp_sadat import FakeRequestSPSADT

class FakeExecucaoSPSADAT(AbstractExecucaoSPSADAT):

    def __init__(self,dados_sp_sadat):

        self.dados_sp_sadat = dados_sp_sadat
        pass

    def processar_rpa(self):

        try:

            self.validar_dados_a_enviar()
            self.solicitar_autorizacao()
            self.validar_autorizacao()
            self.salvar_autorizacao()

            return {}
        
        except Exception as e:

            raise e

    def validar_dados_a_enviar(self):

        pass

    def solicitar_autorizacao(self):

        request = FakeRequestSPSADT()
        request.executar_request_sp_sadt()

        pass

    def validar_autorizacao(self):

        pass

    def salvar_autorizacao(self):

        pass

    
    