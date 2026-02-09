from pytest import mark
import logging
from config import settings


@mark.parametrize(
    "codigo_prestador_na_operadora,nome_contratado,carater_atendimento,tipo_atendimento",
    [(122232, "Maria", 1, 1)],
)
def test_cadastro_deve_falhar_pois_ja_foi_cadastrado_um_contratado_com_mesmo_codigo_prestador_na_operadora(
    app,
    contratado,
    codigo_prestador_na_operadora,
    nome_contratado,
    carater_atendimento,
    tipo_atendimento,
    client_app,
):

    logging.debug(contratado)

    data = {
        "codigo_prestador_na_operadora": codigo_prestador_na_operadora,
        "nome_contratado": nome_contratado,
        "carater_atendimento": carater_atendimento,
        "tipo_atendimento": tipo_atendimento,
    }
    endpoint = f"{settings.BASE_URL}/contratado"

    response = client_app.post(endpoint, json=data)
    response_json = response.json

    assert response.status_code == 409
    assert (
        response_json["message"]
        == "Já existe um contratado com o mesmo codigo_prestador_na_operadora cadastrado !"
    )
