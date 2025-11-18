
from flask import Blueprint

main = Blueprint("main",__name__)

@main.route('/')
def index():

    return "Pagina que o paciente vai inserir o token..."


