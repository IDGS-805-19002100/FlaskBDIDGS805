from flask import Blueprint

# Aquí definimos el objeto que app.py busca importar
inscripciones = Blueprint('inscripciones', __name__)

from . import routes