from abc import ABC, abstractmethod


class AbstractExecucaoSPSADAT(ABC):
    @abstractmethod
    def __init__(self):

        pass

    @abstractmethod
    def processar_rpa():

        pass

    @abstractmethod
    def validar_xml_contra_xsd():

        pass

    @abstractmethod
    def solicitar_autorizacao():

        pass

    @abstractmethod
    def validar_autorizacao():

        pass

    @abstractmethod
    def salvar_autorizacao(self):

        pass
