from flask import Blueprint, jsonify
from servicos.google_maps import obter_dados_trafego

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({
        "api": "Transporte Urbano",
        "status": "online"
    })

@api.route("/status")
def status():
    return jsonify({
        "status": "online"
    })

@api.route("/traffic")
def traffic():
    dados = obter_dados_trafego()
    return jsonify(dados)

@api.route("/traffic/<regiao>")
def traffic_regiao(regiao):

    return jsonify({
        "regiao": regiao,
        "congestionamento": "Alto",
        "velocidade_media": 22,
        "intensidade": "Intensa"
    })