from src.fake.fake_token import FakeTokenPaciente
from src.routes.v1.enviar_token_paciente.token_paciente import TokenPaciente
import os
from dotenv import load_dotenv

class FactoryToken:

     @staticmethod
     def create():

        load_dotenv(dotenv_path="api/.env")

        if os.getenv("ENV_FOR_DYNACONF") == "test":

            return FakeTokenPaciente()

        return TokenPaciente()