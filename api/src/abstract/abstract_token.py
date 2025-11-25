from abc import ABC, abstractmethod

class AbstractTokenPaciente(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def validar_dados_enviados():

        pass
    
    @abstractmethod
    def receber_token_consulta_paciente_route():

        pass

