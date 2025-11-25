from src.rpa.abstract.abstract_request_sp_sadat import AbstractRequestSPSADAT
import requests


class FakeRequestSPSADT(AbstractRequestSPSADAT):

    def __init__(self,uri):

        self.uri = uri

    def executar_request_sp_sadt(self,data):

        try:

            response = requests.post(self.uri,data=data)
            return [response.status_code, response.text]
        
        except Exception as e:

            raise e

        