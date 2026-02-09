from pytest import fixture
from config import settings
import logging


@fixture
def endpoint():

    def _endpoint(route):

        endpoint = f"{settings.BASE_URL}/{route}"
        logging.debug(endpoint)

        return endpoint

    yield _endpoint


@fixture(scope="session")
def endpoint():

    def _endpoint(route):

        endpoint = f"{settings.BASE_URL}/{route}"
        logging.debug(endpoint)

        return endpoint

    yield _endpoint
