import logging


def test_deve_ser_cadastrado_usuario(user_scope_function):

    logging.debug(user_scope_function)

    assert user_scope_function["message"] == "Cadastrado com sucesso!"
    assert user_scope_function["status_code"] == 201
