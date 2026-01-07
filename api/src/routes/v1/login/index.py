from flask import Blueprint,jsonify
from src.models.Users import Users
from flask import request
from flask_jwt_extended import create_access_token
import logging
from src.utils.not_empty_or_error import notEmptyOrError
from werkzeug.security import check_password_hash

login = Blueprint('login', __name__)

@login.route('/login', methods=["POST"])
def login_usuario():

    try:
        dados = request.get_json()

        notEmptyOrError(dados,"login","O login não pode ficar em branco !")
        notEmptyOrError(dados,"senha","A senha não pode ficar em branco !")


        where = {"login": dados["login"]}
        login = Users.buscar(where)

        if len(login) == 0:
            return jsonify({"message": "Login ou senha incorretos !"}), 401
        
        logging.debug(login)

        senha = login[0][0].senha
        check_senha = check_password_hash(senha, dados["senha"])

        logging.debug(check_senha)

        if check_senha:
            access_token = create_access_token(identity=dados["login"])
            response = {"message": "Login efetuado com sucesso !", "data": {"login":login[0][0].login,"tipo_usuario_id":login[0][0].tipo_usuario_id},"access_token":access_token}
            logging.debug(response)

            return jsonify(response), 200

        return jsonify({"message": "Login ou senha incorretos !"}), 401
    
    except Exception as e:

        logging.debug(e)

        if isinstance(e.args[0],dict):

            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]
        
        return jsonify({"message": f"Falha ao efetuar login ! {e}"}), 500