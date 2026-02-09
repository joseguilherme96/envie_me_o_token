from flask import Blueprint, jsonify, request
from src.models.Operadora import Operadora
import logging
from src.utils.is_numeric_or_error import isNumericOrError
from src.utils.not_empty_or_error import notEmptyOrError
from flask_jwt_extended import jwt_required

operadora = Blueprint("operadora", __name__)


@operadora.route("/operadora", methods=["POST"])
@jwt_required()
def cadastrar_operadora():
    try:
        dados = request.get_json()

        logging.debug(dados)

        notEmptyOrError(dados, "registro_ans", "O campo registro_ans é obrigatório !")
        notEmptyOrError(dados, "operadora", "O campo operadora é obrigatório !")

        operadora = Operadora.buscar({"registro_ans": dados["registro_ans"]})
        logging.debug(operadora)

        if operadora:
            return jsonify(
                {
                    "message": "Já existe uma operadora com o mesmo registro_ans cadastrado !"
                }
            ), 409

        if not isinstance(dados.get("operadora"), str):
            return jsonify({"message": "O campo operadora deve ser um texto !"}), 400

        isNumericOrError(
            dados, "registro_ans", "O campo registro_ans deve ser um número inteiro !"
        )

        dados = Operadora.inserir(
            Operadora(registro_ans=dados["registro_ans"], operadora=dados["operadora"])
        )

        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201

    except Exception as e:
        logging.error(e.args)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
