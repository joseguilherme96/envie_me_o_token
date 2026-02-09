from pytest import mark
from config import settings


@mark.parametrize(
    "login,senha,mensagem",
    [
        ("", "24dsdf", "O campo login não deve ser vazio !"),
        ("jdjdjd", "", "O campo senha não deve ser vazia !"),
    ],
)
def test_nao_deve_ser_cadastrado_login_devido_os_campos_estarem_em_brancos(
    user_mark_parametrize_scope_function, mensagem
):

    assert user_mark_parametrize_scope_function["status_code"] == 400
    assert user_mark_parametrize_scope_function["message"] == mensagem


@mark.parametrize(
    "login,senha,mensagem",
    [
        ("tesetes3s3@teste.com", "12", "A senha deve ter no minimo 8 caracteres !"),
        (
            "teste3e44ss3@test.com",
            "12345678",
            "A senha deve conter no minimo duas letras !",
        ),
    ],
)
def test_as_senhas_devem_ser_invalidadas(
    app, user_mark_parametrize_scope_function, mensagem
):

    assert user_mark_parametrize_scope_function["status_code"] == 400
    assert user_mark_parametrize_scope_function["message"] == mensagem


@mark.parametrize(
    "login,senha,mensagem",
    [
        ("testse9@teste.com.br", "123456jf", "O usuário já existe !"),
    ],
)
def test_o_usuario_nao_deve_ser_cadastrado_novamente_devido_ja_existir_na_base_de_dados(
    tipo_user_scope_function,
    user_mark_parametrize_scope_function,
    client_app_scope_function,
    login,
    senha,
    mensagem,
):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/users",
        json={
            "login": login,
            "senha": senha,
            "tipo_usuario_id": tipo_user_scope_function["data"]["cod_tipo_user"],
        },
    )


    assert response.status_code == 409
