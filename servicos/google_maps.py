from datetime import datetime

def obter_dados_trafego():

    return {
        "congestionamento": "Alto",
        "velocidade_media": 22,
        "intensidade": "Intensa",
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }