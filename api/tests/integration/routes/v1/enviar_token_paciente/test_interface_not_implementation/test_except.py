from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente
from src import create_app
from unittest.mock import Mock

def test_o_rpa_nao_deve_ser_processado_devido_a_ausencia_do_atributo_token(mocker):

    app = create_app()

    with app.app_context():

        api = FactoryAPITokenPaciente.create()
        mocker.patch.object(api,"validar_dados_enviados",Mock(side_effect=KeyError({
            "message":"O atributo token não foi enviado !","status_code":400
        })))

        json_response, status = api.enviar_dados_para_execucao_sp_sadt()

        assert status == 400
        assert "message" in json_response.json
        assert json_response.json["message"] == "O atributo token não foi enviado !"