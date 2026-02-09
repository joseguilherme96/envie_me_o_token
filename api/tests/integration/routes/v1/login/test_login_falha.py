from pytest import mark
from config import settings


@mark.parametrize(
    "login,senha",
    [
        ("hdhfsh@gmail.com.br", "dkdjjd948848443"),
        ("hdhfsh@gmail.com.br", "dkdjjd94884ww8443"),
        ("hdhfsh@gmail.com.br", "dkdjjd94884wwss8443"),
    ],
)
def test_login_falha_devido_senha_estar_errada(
    client_app_scope_function, user_mark_parametrize_scope_function, login, senha
):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/login", json={"login": login, "senha": "sdsdsdsdsd"}
    )

    assert response.status_code == 401


@mark.parametrize(
    "login,senha",
    [
        ("hdhfsh@gmail.com.br", "dkdjjd948848443"),
        ("hdhfsh@gmail.com.br", "dkdjjd94884ww8443"),
        ("hdhfsh@gmail.com.br", "dkdjjd94884wwss8443"),
    ],
)
def test_login_falha_devido_usuario_estar_errado(
    client_app_scope_function, user_mark_parametrize_scope_function, login, senha
):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/login", json={"login": "sssdsf", "senha": senha}
    )

    assert response.status_code == 401
