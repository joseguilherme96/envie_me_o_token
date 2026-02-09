from pytest import mark
from config import settings


@mark.parametrize("login,senha", [("hdhfssh@gmail.com.br", "23242dddd221")])
def test_login_sucesso(
    user_mark_parametrize_scope_function, login, senha, client_app_scope_function
):

    response = client_app_scope_function.post(
        f"{settings.BASE_URL}/login", json={"login": login, "senha": senha}
    )

    response_json = response.json

    assert response.status_code == 200
    assert response_json["message"] == "Login efetuado com sucesso !"
