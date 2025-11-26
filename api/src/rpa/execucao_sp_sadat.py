from abstract.abstract_execucao_sp_sadat import AbstractExecucaoSPSADAT

class ExecucaoSPSADAT(AbstractExecucaoSPSADAT):

    def __init__(self,uri,dados_sp_sadat):

        self.dados_sp_sadat = dados_sp_sadat
        self.uri = uri
        pass

    def processar_rpa(self):

        pass

    def validar_dados_a_enviar(self):

        pass

    def solicitar_autorizacao(self):

        pass

    def validar_autorizacao(self):

        pass

    def salvar_autorizacao(self):

        pass

    
    