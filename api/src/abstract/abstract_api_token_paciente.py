from abc import ABC, abstractmethod

class AbstractAPITokenPaciente(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def validar_dados_enviados():

        pass

    @abstractmethod
    def buscar_dados_para_execucao_sp_sadt():

        return {}
    
    @abstractmethod
    def receber_token_paciente_route():

        pass

