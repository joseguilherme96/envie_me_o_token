from flask import Blueprint, jsonify, request
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.models.Beneficiario import Beneficiario
from src.models.Contratado import Contratado
from src.models.Operadora import Operadora
from src.models.Solicitante import Solicitante
import logging
from src.utils.is_numeric_or_error import isNumericOrError
from src.utils.not_empty_or_error import notEmptyOrError
from flask_jwt_extended import jwt_required

execucao_spsadt = Blueprint("execucao_spsadt", __name__)


@execucao_spsadt.route("/execucao_spsadt", methods=["POST"])
@jwt_required()
def cadastrar_execucao_spsadt():
    try:
        dados = request.get_json()

        logging.debug(dados)

        notEmptyOrError(
            dados, "codigo_beneficiario", "O campo codigo_beneficiario é obrigatório !"
        )
        notEmptyOrError(
            dados, "codigo_contratado", "O campo codigo_contratado é obrigatório !"
        )
        notEmptyOrError(
            dados, "codigo_solicitante", "O campo codigo_solicitante é obrigatório !"
        )
        notEmptyOrError(
            dados,
            "operadora_registro_ans",
            "O campo operadora_registro_ans é obrigatório !",
        )
        notEmptyOrError(dados, "login", "O campo login é obrigatório !")
        notEmptyOrError(
            dados, "indicacao_clinica", "O campo indicacao_clinica é obrigatório !"
        )
        notEmptyOrError(
            dados, "indicacao_acidente", "O campo indicacao_acidente é obrigatório !"
        )
        notEmptyOrError(dados, "observacao", "O campo observacao é obrigatório !")
        notEmptyOrError(dados, "senha", "O campo senha é obrigatório !")
        notEmptyOrError(
            dados, "tipo_transacao", "O campo tipo_transacao é obrigatório !"
        )

        if not isinstance(dados.get("codigo_beneficiario"), str):
            return jsonify(
                {"message": "O campo codigo_beneficiario deve ser um texto !"}
            ), 400

        if not isinstance(dados.get("login"), str):
            return jsonify({"message": "O campo login deve ser um texto !"}), 400

        if not isinstance(dados.get("observacao"), str):
            return jsonify({"message": "O campo observacao deve ser um texto !"}), 400

        if not isinstance(dados.get("senha"), str):
            return jsonify({"message": "O campo senha deve ser um texto !"}), 400

        if not isinstance(dados.get("tipo_transacao"), str):
            return jsonify(
                {"message": "O campo tipo_transacao deve ser um texto !"}
            ), 400

        if not isinstance(dados.get("indicacao_clinica"), bool):
            return jsonify(
                {"message": "O campo indicacao_clinica deve ser um booleano !"}
            ), 400

        isNumericOrError(
            dados,
            "codigo_contratado",
            "O campo codigo_contratado deve ser um número inteiro !",
        )
        isNumericOrError(
            dados,
            "codigo_solicitante",
            "O campo codigo_solicitante deve ser um número inteiro !",
        )
        isNumericOrError(
            dados,
            "operadora_registro_ans",
            "O campo operadora_registro_ans deve ser um número inteiro !",
        )
        isNumericOrError(
            dados,
            "indicacao_acidente",
            "O campo indicacao_acidente deve ser um número inteiro !",
        )

        beneficiario = Beneficiario.buscar(
            where={"numero_carteira": dados["codigo_beneficiario"]}
        )
        logging.debug(beneficiario)

        if not beneficiario:
            return jsonify(
                {"message": "O codigo_beneficiario não está cadastrado !"}
            ), 404

        contratado = Contratado.buscar(
            where={"codigo_prestador_na_operadora": dados["codigo_contratado"]}
        )
        logging.debug(contratado)

        if not contratado:
            return jsonify(
                {"message": "O codigo_contratado não está cadastrado !"}
            ), 404

        solicitante = Solicitante.buscar(
            where={"codigo_solicitante": dados["codigo_solicitante"]}
        )
        logging.debug(solicitante)

        if not solicitante:
            return jsonify(
                {"message": "O codigo_solicitante não está cadastrado !"}
            ), 404

        operadora = Operadora.buscar(
            where={"registro_ans": dados["operadora_registro_ans"]}
        )
        logging.debug(operadora)

        if not operadora:
            return jsonify(
                {"message": "O operadora_registro_ans não está cadastrado !"}
            ), 404

        dados = ExecucaoSPSADT.inserir(
            ExecucaoSPSADT(
                codigo_beneficiario=dados["codigo_beneficiario"],
                codigo_contratado=dados["codigo_contratado"],
                codigo_solicitante=dados["codigo_solicitante"],
                operadora_registro_ans=dados["operadora_registro_ans"],
                login=dados["login"],
                indicacao_clinica=dados["indicacao_clinica"],
                indicacao_acidente=dados["indicacao_acidente"],
                observacao=dados["observacao"],
                senha=dados["senha"],
                tipo_transacao=dados["tipo_transacao"],
            )
        )

        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201

    except Exception as e:
        logging.error(e.args)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
