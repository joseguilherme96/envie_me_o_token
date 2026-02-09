from flask import Blueprint, jsonify, request
from src.models.Contratado import Contratado
import logging
from src.utils.is_numeric_or_error import isNumericOrError
from src.utils.not_empty_or_error import notEmptyOrError
from flask_jwt_extended import jwt_required

contratado = Blueprint("contratado", __name__)


@contratado.route("/contratado", methods=["POST"])
@jwt_required()
def cadastrar_contratado():
    try:
        dados = request.get_json()

        logging.debug(dados)

        notEmptyOrError(
            dados,
            "codigo_prestador_na_operadora",
            "O campo codigo_prestador_na_operadora é obrigatório !",
        )
        notEmptyOrError(
            dados, "nome_contratado", "O campo nome_contratado é obrigatório !"
        )
        notEmptyOrError(
            dados, "carater_atendimento", "O campo carater_atendimento é obrigatório !"
        )
        notEmptyOrError(
            dados, "tipo_atendimento", "O campo tipo_atendimento é obrigatório !"
        )

        if Contratado.buscar(
            {"codigo_prestador_na_operadora": dados["codigo_prestador_na_operadora"]}
        ):
            return jsonify(
                {
                    "message": "Já existe um contratado com o mesmo codigo_prestador_na_operadora cadastrado !"
                }
            ), 409

        if not isinstance(dados.get("nome_contratado"), str):
            return jsonify(
                {"message": "O campo nome_contratado deve ser um texto !"}
            ), 400

        isNumericOrError(
            dados,
            "codigo_prestador_na_operadora",
            "O campo codigo_prestador_na_operadora deve ser um número inteiro !",
        )
        isNumericOrError(
            dados,
            "carater_atendimento",
            "O campo carater_atendimento deve ser um número inteiro !",
        )
        isNumericOrError(
            dados,
            "tipo_atendimento",
            "O campo tipo_atendimento deve ser um número inteiro !",
        )

        logging.debug(dados["carater_atendimento"])
        logging.debug(dados["tipo_atendimento"])

        dados = Contratado.inserir(
            Contratado(
                codigo_prestador_na_operadora=dados["codigo_prestador_na_operadora"],
                nome_contratado=dados["nome_contratado"],
                carater_atendimento=str(dados["carater_atendimento"]),
                tipo_atendimento=str(dados["tipo_atendimento"]),
            )
        )

        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201

    except Exception as e:
        logging.error(e.args)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar ! {e}"}), 500
