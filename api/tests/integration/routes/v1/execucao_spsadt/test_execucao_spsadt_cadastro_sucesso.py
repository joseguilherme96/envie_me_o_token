import logging


def test_deve_ser_cadastrado_execucao_spsadt(execucao_spsadt_no_mark_parametrize):

    logging.debug(execucao_spsadt_no_mark_parametrize)

    assert execucao_spsadt_no_mark_parametrize["message"] == "Cadastrado com sucesso!"
    assert execucao_spsadt_no_mark_parametrize["status_code"] == 201
