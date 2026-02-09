import logging
from pytest import mark


@mark.parametrize(
    "codigo_solicitante,profissional_solicitante,conselho_profissional,numero_conselho_profissional,uf,cbos",
    [(1008, "Dr. Maria Santos", 1, "123456", 35, 225125)],
)
def test_deve_ser_cadastrado_solicitante(app, solicitante):

    logging.debug(solicitante)

    assert solicitante["message"] == "Cadastrado com sucesso!"
    assert solicitante["status_code"] == 201
