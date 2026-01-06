import logging

def test_deve_ser_cadastrado_usuario(app,user):

    logging.debug(user)

    assert user["message"] == "Cadastrado com sucesso!"
    assert user["status_code"] == 201
