from src.fake.fake_api_token_paciente import FakeAPITokenPaciente
from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
import os
from dotenv import load_dotenv

class FactoryAPITokenPaciente:

     @staticmethod
     def create():

        load_dotenv(dotenv_path="api/.env")

        if os.getenv("ENV_FOR_DYNACONF") == "test":

            return FakeAPITokenPaciente()

        return APITokenPaciente()