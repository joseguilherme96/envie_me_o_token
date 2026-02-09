from src.fake.fake_api_token_paciente import FakeAPITokenPaciente
from src.routes.v1.enviar_token_paciente.api_token_paciente import APITokenPaciente
from dotenv import load_dotenv
from config import settings
import logging


class FactoryAPITokenPaciente:
    @staticmethod
    def create():

        load_dotenv(dotenv_path="api/.env")

        if settings.ENV_FOR_DYNACONF == "testing" and settings.USE_CLASS_FAKE:
            return FakeAPITokenPaciente()

        return APITokenPaciente()
