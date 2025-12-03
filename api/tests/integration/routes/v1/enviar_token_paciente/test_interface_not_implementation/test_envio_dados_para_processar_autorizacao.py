from src.factory.factory_api_token_paciente import FactoryAPITokenPaciente
from src import create_app
import logging
from unittest.mock import patch,Mock
import xml.etree.ElementTree as ET


@patch("requests.post")
def test_o_rpa_deve_ser_processado_com_o_envio_dos_dados_para_autorizacao(mock_request_post,caplog):

    response = Mock()
    response.status_code = 201
    response.text = "<xml>API SOAP Autorizado</xml>"

    logging.info("Mockando retorno de qualquer requisicao externa !")
    mock_request_post.return_value = response

    caplog.set_level(level="INFO")

    api = FactoryAPITokenPaciente.create()

    app = create_app()

    with app.app_context():

        logging.info("Enviando dados paciente para API RESTful.....")
        response = api.enviar_dados_para_execucao_sp_sadt()

    assert response[1] == 201
    assert response[0].json == {"message": "O paciente foi autorizado com sucesso !"}
    logging.info(f"Resposta de autorização para tratamento do paciente : {response[0].json}")

    assert isinstance(api.dados_env_e_valido,object) is True
    logging.info(f"Validacao dos dados enviados : {api.dados_env_e_valido}")

    assert  isinstance(api.dados_exec_sp_sadat,object) is True
    logging.info(f"Dados encontrados para execução sp sadt : {api.dados_exec_sp_sadat}")

    try:

        xml = api.factory_request_sp_sadt_data_xml.xml
        ET.fromstring(xml)

    except ET.ParseError:

        assert False, "XML inválido"

    logging.info(f"XML construído para envio na API SOAP : {api.factory_request_sp_sadt_data_xml.xml}")

    assert api.execucao_sp_sadt.response == "<xml>API SOAP Autorizado</xml>"
    logging.info(f"Resposta da solicitação de autorização no Web Service SOAP : {api.execucao_sp_sadt.response}")

    assert api.execucao_sp_sadt.processado is True
    logging.info(f"O RPA foi exeutado com sucesso na API SOAP : {api.execucao_sp_sadt.processado}")

        