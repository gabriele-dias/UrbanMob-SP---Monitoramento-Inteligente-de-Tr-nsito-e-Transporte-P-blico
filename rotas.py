from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/traffic", methods=["GET"])
def obter_trafego():

    dados = {
        "congestionamento": "Alto",
        "velocidade_media": 22,
        "intensidade": "Intensa"
    }

    return jsonify(dados)