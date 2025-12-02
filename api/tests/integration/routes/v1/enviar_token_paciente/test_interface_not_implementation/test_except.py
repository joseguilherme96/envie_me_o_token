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

def test_o_rpa_nao_deve_ser_processado_devido_dados_incompletos_para_execucao_sp_sadt(mocker):

    app = create_app()

    with app.app_context():

        api = FactoryAPITokenPaciente.create()

        fake = Mock()
        fake.processar_rpa.side_effect = Exception({
            "message":"Dados incompletos",
            "status_code":400
        })

        mocker.patch(
            "src.factory.factory_execucao_sp_sadt.FactoryExecucaoSPSADT.create",
            return_value=fake
        )

        json_response, status = api.enviar_dados_para_execucao_sp_sadt()

        assert status == 400
        assert json_response.json["message"] == "Dados incompletos"

def test_o_rpa_nao_deve_ser_processado_devido_falha_na_construcao_xml_para_envio(mocker):

    app = create_app()

    with app.app_context():

        api = FactoryAPITokenPaciente.create()

        fake = Mock()
        fake.construir_xml.side_effect = Exception({
            "message":"Falha ao construir XML.",
            "status_code":400
        })

        mocker.patch(
            "src.factory.factory_request_sp_sadt_data_xml.FactoryRequestSPSADTDataXML.create",
            return_value=fake
        )

        json_response, status = api.enviar_dados_para_execucao_sp_sadt()

        assert status == 400
        assert json_response.json["message"] == "Falha ao construir XML."

def test_o_processamento_do_rpa_deve_ser_interrompido_devido_ao_web_service_do_cliente_estar_indisponivel(mocker):

    app = create_app()

    with app.app_context():

        fake = Mock()
        fake.processar_rpa.side_effect = Exception({
            "message":"Web service do cliente indisponível.",
            "status_code":503
        })

        mocker.patch(
            "src.factory.factory_execucao_sp_sadt.FactoryExecucaoSPSADT.create",
            return_value=fake
        )

        api = FactoryAPITokenPaciente.create()
        json_response, status = api.enviar_dados_para_execucao_sp_sadt()

        assert status == 503
        assert json_response.json["message"] == "Web service do cliente indisponível."

