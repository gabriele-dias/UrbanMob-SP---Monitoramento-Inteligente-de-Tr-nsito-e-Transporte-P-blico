REGIOES = [
    {
        "nome": "Centro",
        "latitude": -23.550520,
        "longitude": -46.633308
    }
]


def listar_regioes():
    return REGIOES


def obter_regiao(nome):

    for regiao in REGIOES:

        if regiao["nome"].lower() == nome.lower():
            return regiao

    return None