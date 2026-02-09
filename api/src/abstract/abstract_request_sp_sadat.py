from abc import ABC, abstractmethod


class AbstractRequestSPSADAT(ABC):
    @abstractmethod
    def __init__(self, uri):

        self.uri = uri

    @abstractmethod
    def executar_request_sp_sadt(self):

        pass
