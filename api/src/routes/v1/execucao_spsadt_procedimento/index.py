from flask import Blueprint, jsonify, request
from src.models.ExecucaoSPSADTProcedimento import ExecucaoSPSADTProcedimento
from src.models.ExecucaoSPSADT import ExecucaoSPSADT
from src.utils.is_numeric_or_error  import isNumericOrError
from src.utils.not_empty_or_error import notEmptyOrError
import logging
from flask_jwt_extended import jwt_required

execucao_spsadt_procedimento = Blueprint("execucao_spsadt_procedimento", __name__)

@execucao_spsadt_procedimento.route('/execucao_spsadt_procedimento', methods=["POST"])
@jwt_required()
def cadastrar_execucao_spsadt_procedimento():
    try:
        dados = request.get_json()

        logging.debug(dados)

        notEmptyOrError(dados,"codigo_procedimento","O campo codigo_procedimento deve ser preenchido !")
        notEmptyOrError(dados,"codigo_execucao","O campo codigo_execucao deve ser preenchido !")
        notEmptyOrError(dados,"descricao_procedimento","O campo descricao_procedimento deve ser preenchido !")
        notEmptyOrError(dados,"quantidade_solicitada","O campo quantidade_solicitada deve ser preenchido !")

        if not isinstance(dados["descricao_procedimento"],str):

            return jsonify({"message":"O campo descricao_procedimento deve ser um texto !"}),400
        
        isNumericOrError(dados,"codigo_procedimento","O campo codigo_procedimento deve ser um numero inteiro !")
        isNumericOrError(dados,"codigo_execucao","O campo codigo_execucao deve ser um numero inteiro !")
        isNumericOrError(dados,"quantidade_solicitada","O campo quantidade_solicitada deve ser um numero inteiro !")

        execucao_sp_sadt = ExecucaoSPSADT.buscar({"codigo_execucao":dados["codigo_execucao"]})

        logging.debug(execucao_sp_sadt)

        if not execucao_sp_sadt:

            return jsonify({"message": "Não foi encontrado o codigo_execucao informado !"}),404
        
        dados = ExecucaoSPSADTProcedimento.inserir(ExecucaoSPSADTProcedimento(
            codigo_procedimento=dados["codigo_procedimento"],
            codigo_execucao=dados["codigo_execucao"],
            descricao_procedimento=dados["descricao_procedimento"],
            quantidade_solicitada=dados["quantidade_solicitada"]
        ))

        logging.debug(dados)
        
        return jsonify({"message": "Cadastrado com sucesso!", "data": dados}), 201
    
    except Exception as e:

        logging.error(e.args)

        if isinstance(e.args[0], dict):
            return jsonify({"message": e.args[0]["message"]}), e.args[0]["status_code"]

        return jsonify({"message": f"Falha ao cadastrar! {e}"}), 500
