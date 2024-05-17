from flask import Blueprint, request, jsonify
from algoritmo_diagnostico import asignarRuta

ruta = Blueprint('ruta', __name__)


@ruta.route("/obtenerRuta", methods=['GET', 'POST'])
def cuestionario():
    respuestas_estudiante = request.get_json()
    factores = respuestas_estudiante['respuestas']
    respuestas = [factores['cumpleaños'], factores['actividades'], factores['time'], factores['gift'], factores['money'],
                factores['party'], factores['angry'], factores['vacations']]   
    response = asignarRuta(respuestas)
    return jsonify(response)

@ruta.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

