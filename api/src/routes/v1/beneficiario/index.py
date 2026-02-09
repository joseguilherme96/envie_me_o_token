from flask import Blueprint, jsonify, request
from src.models.Beneficiario import Beneficiario
import logging
from flask_jwt_extended import jwt_required

beneficiario = Blueprint("beneficiario", __name__)


@beneficiario.route("/beneficiario", methods=["POST"])
@jwt_required()
def cadastrar_beneficiario():
    try:
        header = request.headers

        logging.debug(header)

        dados = request.get_json()

        logging.debug(dados)

        try:
            int(dados["numero_carteira"])

        except Exception:
            return jsonify(
                {"message": "O campo numero_carteira deve ser um inteiro !"}
            ), 400

        if (
            len(str(dados["numero_carteira"])) < 8
            or len(str(dados["numero_carteira"])) > 12
        ):
            return jsonify({"message": "O campo numero_carteira é inválido !"}), 400

        if not isinstance(dados["atendimento_rn"], bool):
            return jsonify(
                {"message": "O campo atendimento_rn deve ser um booleano !"}
            ), 400

        if Beneficiario.buscar({"numero_carteira": dados["numero_carteira"]}):
            return jsonify({"message": "Beneficiário já cadastrado !"}), 409

        data = Beneficiario(
            numero_carteira=dados["numero_carteira"],
            atendimento_rn=dados["atendimento_rn"],
            nome_beneficiario=dados["nome_beneficiario"],
        )
        dados = Beneficiario.inserir(data)

        logging.debug(dados)

        return jsonify({"message": "Cadastrado com sucesso !", "data": dados}), 201

    except Exception as e:
        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
