# UrbanMob SP - Monitoramento Inteligente de Trânsito e Transporte Público

## Sobre o Projeto

O UrbanMob SP é uma API REST desenvolvida em Python utilizando Flask para fornecer informações sobre trânsito urbano.

O objetivo do projeto é servir como backend para um aplicativo Android, utilizando conceitos de Sistemas Distribuídos por meio da comunicação entre cliente, servidor e serviços externos.

---

# Tecnologias Utilizadas

- Python
- Flask
- JSON
- HTTP/HTTPS
- Requests
- Python Dotenv
- Git/GitHub

---

# Estrutura do Projeto

```text
UrbanMob-SP/
│
├── app.py
├── rotas.py
├── configuracao.py
├── .env
│
├── servicos/
│   └── google_maps.py
│
├── requirements.txt
│
└── .venv/
```

---

# Arquitetura

```text
Cliente
(Navegador/Android)
          ↓
      Flask API
          ↓
       Rotas
          ↓
      Serviços
          ↓
 Google Maps API
```

---

# Execução do Projeto

## Criar ambiente virtual

```bash
python -m venv .venv
```

## Ativar ambiente

Git Bash

```bash
source .venv/Scripts/activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Instalar dependências

```bash
pip install flask requests python-dotenv
```

## Gerar requirements

```bash
pip freeze > requirements.txt
```

---

# app.py

Responsável por iniciar a aplicação Flask.

```python
from flask import Flask
from rotas import api

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
```

## O que faz

- Cria o servidor Flask.
- Importa as rotas.
- Registra as rotas na aplicação.
- Inicia o servidor local.

---

# rotas.py

Responsável por receber requisições HTTP e devolver respostas.

```python
from flask import Blueprint, jsonify
from servicos.google_maps import obter_dados_trafego

api = Blueprint("api", __name__)
```

---

## Rota Principal

```python
@api.route("/")
def home():
    return jsonify({
        "api": "Transporte Urbano",
        "status": "online"
    })
```

### Endpoint

```http
GET /
```

### Resposta

```json
{
  "api": "Transporte Urbano",
  "status": "online"
}
```

---

## Verificação de Status

```python
@api.route("/status")
def status():
    return jsonify({
        "status": "online"
    })
```

### Endpoint

```http
GET /status
```

### Resposta

```json
{
  "status": "online"
}
```

---

## Dados de Trânsito

```python
@api.route("/traffic")
def traffic():

    dados = obter_dados_trafego()

    return jsonify(dados)
```

### Endpoint

```http
GET /traffic
```

### Fluxo

```text
Usuário
    ↓
/traffic
    ↓
rotas.py
    ↓
google_maps.py
    ↓
JSON
    ↓
Usuário
```

---

# google_maps.py

Responsável por buscar informações de trânsito.

Atualmente o serviço já está preparado para consumir a API do Google Maps.

```python
import requests
from configuracao import Config
```

---

## Funcionamento

1. Define origem e destino.
2. Faz requisição para a API do Google.
3. Recebe resposta JSON.
4. Processa os dados.
5. Retorna informações para a rota.

---

# Configuração da API Key

Criar arquivo:

```text
.env
```

Conteúdo:

```env
GOOGLE_API_KEY=SUA_CHAVE_AQUI
```

---

# configuracao.py

```python
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

## O que faz

- Carrega variáveis do arquivo `.env`.
- Disponibiliza a chave para toda a aplicação.

---

# Testes

Iniciar servidor:

```bash
python app.py
```

Servidor:

```text
http://127.0.0.1:5000
```

---

## Teste da Home

```text
http://127.0.0.1:5000/
```

---

## Teste do Status

```text
http://127.0.0.1:5000/status
```

---

## Teste do Trânsito

```text
http://127.0.0.1:5000/traffic
```

---

# Problema Encontrado

Durante a integração com a Google Maps API foi identificado o seguinte erro:

```json
{
  "status": "REQUEST_DENIED"
}
```

Causa:

```text
API Key não configurada
```

Solução:

```text
Criar uma chave no Google Cloud Platform
e configurar o arquivo .env.
```

---

# Próximas Etapas

## Sprint 2

- Configurar API Key do Google Maps.
- Habilitar Routes API.
- Consumir dados reais de trânsito.

## Sprint 3

- Docker.

## Sprint 4

- Desenvolvimento Android.

## Sprint 5

- Integração Android + API Flask.

## Sprint 6

- Integração SPTrans.
- Localização de ônibus em tempo real.

---

# Autor

Gabriel Dias

Projeto desenvolvido para a disciplina de Sistemas Distribuídos (APS).