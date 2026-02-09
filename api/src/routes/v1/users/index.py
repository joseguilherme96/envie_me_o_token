from flask import Blueprint, jsonify, request
from src.models.Users import Users
from werkzeug.security import generate_password_hash
import logging
from src.utils.not_empty_or_error import notEmptyOrError
from flask_jwt_extended import jwt_required

users = Blueprint("users", __name__)


@users.route("/users", methods=["POST"])
@jwt_required()
def cadastrar_users():
    try:
        dados = request.get_json()

        logging.debug(request.headers)
        logging.debug(dados)

        notEmptyOrError(dados, "login", "O campo login não deve ser vazio !")
        notEmptyOrError(dados, "senha", "O campo senha não deve ser vazia !")

        query = Users.buscar({"login": dados["login"]})

        if len(query) > 0:
            return jsonify({"message": "O usuário já existe !"}), 409

        if len(dados["senha"]) < 8:
            return jsonify(
                {"message": "A senha deve ter no minimo 8 caracteres !"}
            ), 400

        quantidade_letras = 0
        for caractere in dados["senha"]:
            if caractere not in (str(x) for x in range(0, 10)):
                quantidade_letras += 1

        logging.debug(quantidade_letras)

        if quantidade_letras < 2:
            return jsonify(
                {"message": "A senha deve conter no minimo duas letras !"}
            ), 400

        hash_senha = generate_password_hash(dados["senha"])

        payload = Users(
            login=dados["login"],
            senha=hash_senha,
            tipo_usuario_id=dados["tipo_usuario_id"],
        )

        logging.debug(payload.__dict__)

        dados = Users.inserir(payload)

        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201

    except Exception as e:
        logging.debug(e)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
