from flask import Blueprint
from flask import jsonify

from traffic import obter_dados_trafego
from geolocalizacao import listar_regioes
from geolocalizacao import obter_regiao

api = Blueprint("api", __name__)


@api.route("/")
def home():

    return jsonify({
        "api": "UrbanMob SP",
        "status": "online"
    })


@api.route("/status")
def status():

    return jsonify({
        "status": "online"
    })


@api.route("/traffic")
def traffic():

    return jsonify(
        obter_dados_trafego()
    )


@api.route("/regioes")
def regioes():

    return jsonify(
        listar_regioes()
    )


@api.route("/regioes/<nome>")
def regiao(nome):

    dados = obter_regiao(nome)

    if not dados:

        return jsonify({
            "erro": "Região não encontrada"
        }), 404

    return jsonify(dados)