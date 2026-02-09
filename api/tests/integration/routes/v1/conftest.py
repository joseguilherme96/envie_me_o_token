from pytest import fixture
from config import settings
import logging

# Fixtures são auto-descobertas pelo pytest via conftest.py
# ruff: noqa: F401
from fixtures.beneficiario_no_mark_parametrize_scope_session import (
    beneficiario_data as beneficiario_data_session,
    nome_beneficiario as nome_beneficiario_session,
    atendimento_rn as atendimento_rn_session,
    numero_carteira as numero_carteira_session,
)
from fixtures.beneficiario_no_mark_parametrize_scope_function import (
    beneficiario_data,
    nome_beneficiario,
    atendimento_rn,
    numero_carteira,
)
from fixtures.user import (
    user_mark_parametrize_scope_function,
    user_scope_function,
)
from fixtures.execucao_spsadt_mark_parametrize import execucao_spsadt_mark_parametrize
from fixtures.beneficiario_no_mark_parametrize_scope_session import (
    beneficiario_no_mark_parametrize_scope_session,
)
from fixtures.contratado_no_mark_parametrize import (
    contratado_no_mark_parametrize_scope_session,
)
from fixtures.solicitante_no_mark_parametrize import (
    solicitante_no_mark_parametrize_scope_session,
)
from fixtures.operadora_no_mark_parametrize import (
    operadora_no_mark_parametrize_scope_session,
)
from fixtures.endpoint import endpoint
from fixtures.get_data_execucao_spsadt import get_data_execucao_spsadt
from fixtures.execucao_spsadt_no_mark_parametrize import (
    execucao_spsadt_no_mark_parametrize,
    execucao_spsadt_no_mark_parametrize_option_2,
    execucao_spsadt_no_mark_parametrize_option_3,
)
from fixtures.execucao_spsadt_procedimento_no_mark_parametrize import (
    execucao_spsadt_procedimento_no_mark_parametrize,
)





@fixture
def setup_tables(
    app, beneficiario, contratado, solicitante, operadora, tipo_user, user
):

    logging.info(
        "Iniciando setup das tabelas : beneficiario, contratado, solicitante, operadora, tipo_user e user"
    )

    yield beneficiario, contratado, solicitante, operadora, tipo_user, user

    logging.info(
        "Finalizando setup das tabelas : beneficiario, contratado, solicitante, operadora, tipo_user e user"
    )


@fixture
def beneficiario(
    app,
    client_app,
    numero_carteira,  # noqa: F811
    atendimento_rn,  # noqa: F811
    nome_beneficiario,  # noqa: F811
    response_status_code,
    response_message,
):

    endpoint = f"{settings.BASE_URL}/beneficiario"  # noqa: F811
    data = {
        "numero_carteira": numero_carteira,
        "atendimento_rn": atendimento_rn,
        "nome_beneficiario": nome_beneficiario,
    }

    logging.debug(data)
    logging.debug(endpoint)

    response = client_app.post(endpoint, json=data)

    logging.debug(response)

    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture
def contratado(
    codigo_prestador_na_operadora,
    nome_contratado,
    carater_atendimento,
    tipo_atendimento,
    client_app,
):

    response = client_app.post(
        f"{settings.BASE_URL}/contratado",
        json={
            "codigo_prestador_na_operadora": codigo_prestador_na_operadora,
            "nome_contratado": nome_contratado,
            "carater_atendimento": carater_atendimento,
            "tipo_atendimento": tipo_atendimento,
        },
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture
def solicitante(
    codigo_solicitante,
    profissional_solicitante,
    conselho_profissional,
    numero_conselho_profissional,
    uf,
    cbos,
    client_app_scope_function,
):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/solicitante",
        json={
            "codigo_solicitante": codigo_solicitante,
            "profissional_solicitante": profissional_solicitante,
            "conselho_profissional": conselho_profissional,
            "numero_conselho_profissional": numero_conselho_profissional,
            "uf": uf,
            "cbos": cbos,
        },
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture
def operadora(registro_ans, nome_operadora, client_app_scope_function):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/operadora",
        json={"registro_ans": registro_ans, "operadora": nome_operadora},
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture(scope="session")
def tipo_user(client_app):

    response = client_app.post(
        f"{settings.BASE_URL}/tipo_user", json={"tipo_user": "Prestador"}
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json


@fixture(scope="function")
def tipo_user_scope_function(client_app_scope_function):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/tipo_user", json={"tipo_user": "Prestador"}
    )
    response_json = response.json
    response_json["status_code"] = response.status_code

    yield response_json
