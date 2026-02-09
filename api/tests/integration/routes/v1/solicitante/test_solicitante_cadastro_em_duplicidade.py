from pytest import mark
import logging
from config import settings


@mark.parametrize(
    "codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos",
    [(1006, "Dr. Maria Santos", 1, "123456", 35, 225125)],
)
def test_cadastro_deve_falhar_pois_ja_foi_cadastrado_um_solicitante_com_mesmo_codigo_solicitante(
    app_scope_function,
    solicitante,
    codigo_solicitante,
    profissional_solicitante,
    conselho_profissional,
    numero_conselho_profissional,
    uf,
    cbos,
    client_app_scope_function,
):

    logging.debug(solicitante)

    data = {
        "codigo_solicitante": codigo_solicitante,
        "profissional_solicitante": profissional_solicitante,
        "conselho_profissional": conselho_profissional,
        "numero_conselho_profissional": numero_conselho_profissional,
        "uf": uf,
        "cbos": cbos,
    }
    endpoint = f"{settings.BASE_URL}/solicitante"

    response = client_app_scope_function.post(endpoint, json=data)
    response_json = response.json

    assert response.status_code == 409
    assert (
        response_json["message"]
        == "Já existe um solicitante com o mesmo codigo_solicitante cadastrado !"
    )
