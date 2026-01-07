from flask import Blueprint, jsonify, request
from src.models.Solicitante import Solicitante
import logging
from src.utils.is_numeric_or_error import isNumericOrError
from src.utils.not_empty_or_error import notEmptyOrError
from flask_jwt_extended import jwt_required

solicitante = Blueprint("solicitante", __name__)

@solicitante.route('/solicitante', methods=["POST"])
@jwt_required()
def cadastrar_solicitante():
    try:
        dados = request.get_json()

        logging.debug(dados)
        
        notEmptyOrError(dados, "codigo_solicitante", "O campo codigo_solicitante é obrigatório !")
        notEmptyOrError(dados, "profissional_solicitante", "O campo profissional_solicitante é obrigatório !")
        notEmptyOrError(dados, "conselho_profissional", "O campo conselho_profissional é obrigatório !")
        notEmptyOrError(dados, "numero_conselho_profissional", "O campo numero_conselho_profissional é obrigatório !")
        notEmptyOrError(dados, "uf", "O campo uf é obrigatório !")
        notEmptyOrError(dados, "cbos", "O campo cbos é obrigatório !")

        solicitante = Solicitante.buscar({"codigo_solicitante": dados["codigo_solicitante"]})
        logging.debug(solicitante)
        
        if(solicitante):
            return jsonify({"message": "Já existe um solicitante com o mesmo codigo_solicitante cadastrado !"}), 409
        
        if isinstance(dados.get("profissional_solicitante"), str) == False:
            return jsonify({"message": "O campo profissional_solicitante deve ser um texto !"}), 400
        
        if isinstance(dados.get("numero_conselho_profissional"), str) == False:
            return jsonify({"message": "O campo numero_conselho_profissional deve ser um texto !"}), 400
        
        isNumericOrError(dados, "codigo_solicitante", "O campo codigo_solicitante deve ser um número inteiro !")
        isNumericOrError(dados, "conselho_profissional", "O campo conselho_profissional deve ser um número inteiro !")
        isNumericOrError(dados, "uf", "O campo uf deve ser um número inteiro !")
        isNumericOrError(dados, "cbos", "O campo cbos deve ser um número inteiro !")
        
        dados = Solicitante.inserir(Solicitante(
            codigo_solicitante=dados["codigo_solicitante"],
            profissional_solicitante=dados["profissional_solicitante"],
            conselho_profissional=dados["conselho_profissional"],
            numero_conselho_profissional=dados["numero_conselho_profissional"],
            uf=dados["uf"],
            cbos=dados["cbos"]
        ))
        
        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201
    
    except Exception as e:
        logging.error(e.args)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
