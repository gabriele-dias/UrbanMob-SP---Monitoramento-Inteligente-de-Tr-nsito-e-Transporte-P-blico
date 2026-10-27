# 🚦 UrbanMob SP - Monitoramento Inteligente de Trânsito e Transporte Público

## 📖 Sobre o Projeto

O UrbanMob SP é uma API REST desenvolvida em Python utilizando Flask para fornecer informações sobre mobilidade urbana.

O objetivo do projeto é servir como backend para um aplicativo mobile desenvolvido em Flutter, aplicando conceitos de Sistemas Distribuídos por meio da comunicação entre cliente, servidor e serviços externos.

O sistema será responsável por disponibilizar informações relacionadas a:

- Trânsito urbano
- Transporte público
- Velocidade média por região
- Intensidade do tráfego
- Localização de ônibus
- Alertas de mobilidade urbana

---

# 🛠 Tecnologias Utilizadas

## Back-end

- Python
- Flask
- Requests
- Python Dotenv

## Mobile

- Flutter
- Dart

## Infraestrutura

- Docker
- Docker Compose

## Comunicação

- HTTP
- HTTPS
- JSON

## Controle de Versão

- Git
- GitHub

---

# 📁 Estrutura do Projeto

```text
UrbanMob-SP/

backend/
│
├── app.py
├── rotas.py
├── configuracao.py
│
├── servicos/
│   ├── traffic.py
│   └── sptrans.py
│
├── requirements.txt
├── Dockerfile
│
└── .env


mobile/
│
├── lib/
│   ├── screens/
│   ├── widgets/
│   ├── services/
│   └── main.dart
│
└── pubspec.yaml
```

---

# 🏗 Arquitetura

```text
Usuário
    │
    ▼
Aplicativo Flutter
    │
    ▼
API Flask
    │
    ▼
Serviços
    │
    ▼
Dados de Trânsito
    │
    ▼
Resposta JSON
    │
    ▼
Aplicativo Flutter
```

---

# 🎯 Objetivos da Sprint 1

Nesta etapa inicial o objetivo é construir a estrutura base da API.

Funcionalidades desenvolvidas:

- Inicialização do servidor Flask
- Organização em rotas e serviços
- Retorno de dados simulados (Mock)
- Testes locais via navegador e Postman

---

# 🔗 Endpoints Disponíveis

## Home

### Endpoint

```http
GET /
```

### Resposta

```json
{
  "api": "UrbanMob SP",
  "status": "online"
}
```

---

## Status

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

## Trânsito Geral

### Endpoint

```http
GET /traffic
```

### Resposta

```json
{
  "cidade": "São Paulo",
  "congestionamento": "Moderado",
  "velocidade_media": 28,
  "intensidade": "Normal"
}
```

---

## Trânsito por Região

### Endpoint

```http
GET /traffic/<regiao>
```

### Exemplo

```http
GET /traffic/centro
```

### Resposta

```json
{
  "regiao": "Centro",
  "congestionamento": "Alto",
  "velocidade_media": 18,
  "intensidade": "Intensa"
}
```

---

# ⚙ Estrutura de Código

## app.py

Responsável pela inicialização da aplicação Flask.

```python
from flask import Flask
from rotas import api

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
```

### Responsabilidades

- Criar a aplicação Flask
- Registrar as rotas
- Inicializar o servidor

---

## rotas.py

Responsável pelo recebimento das requisições HTTP e retorno das respostas.

```python
from flask import Blueprint, jsonify
from servicos.traffic import obter_dados_trafego

api = Blueprint("api", __name__)
```

### Exemplo

```python
@api.route("/traffic")
def traffic():

    dados = obter_dados_trafego()

    return jsonify(dados)
```

---

## traffic.py

Responsável pelas regras de negócio relacionadas ao trânsito.

```python
def obter_dados_trafego():

    return {
        "cidade": "São Paulo",
        "congestionamento": "Moderado",
        "velocidade_media": 28,
        "intensidade": "Normal"
    }
```

---

## configuracao.py

Responsável pelo carregamento das variáveis de ambiente.

```python
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME")
```

---

# 🚀 Execução do Projeto

## Criar Ambiente Virtual

```bash
python -m venv .venv
```

---

## Ativar Ambiente

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Instalar Dependências

```bash
pip install flask requests python-dotenv
```

---

## Gerar requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Executar Aplicação

```bash
python app.py
```

Servidor disponível em:

```text
http://127.0.0.1:5000
```

---

# 🧪 Testes

## Home

```text
http://127.0.0.1:5000/
```

---

## Status

```text
http://127.0.0.1:5000/status
```

---

## Trânsito

```text
http://127.0.0.1:5000/traffic
```

---

## Trânsito por Região

```text
http://127.0.0.1:5000/traffic/centro
```

---

# 🗺 Integrações Futuras

O projeto foi estruturado para permitir integração futura com serviços externos de mobilidade urbana.

Possíveis integrações:

- OpenStreetMap
- SPTrans
- APIs de geolocalização
- APIs de monitoramento urbano
- Dados de transporte público em tempo real

---

# 📦 Sprint 2

## Objetivos

- Integração OpenStreetMap
- Estudo da API SPTrans
- Mapeamento das regiões monitoradas
- Criação dos serviços de geolocalização

---

# 🐳 Sprint 3

## Objetivos

- Dockerfile
- Docker Compose
- Execução isolada da API
- Padronização do ambiente

---

# 📱 Sprint 4

## Objetivos

- Estrutura Flutter
- Tela Home
- Tela Trânsito
- Tela Mapa

---

# 🔄 Sprint 5

## Objetivos

- Integração Flutter + Flask
- Consumo dos endpoints
- Atualização automática dos dados
- Tratamento de erros

---

# 🚌 Sprint 6

## Objetivos

- Integração SPTrans
- Consulta de linhas
- Localização de ônibus
- Atualização em tempo real

---

# 📊 Sprint 7

## Objetivos

- Dashboard Inteligente
- Estatísticas de trânsito
- Indicadores de mobilidade urbana
- Relatórios e métricas

---

# 📚 Conceitos de Sistemas Distribuídos Aplicados

O projeto utiliza conceitos fundamentais da disciplina de Sistemas Distribuídos:

- Comunicação Cliente-Servidor
- APIs REST
- Protocolo HTTP/HTTPS
- Transferência de dados em JSON
- Integração entre sistemas heterogêneos
- Arquitetura distribuída

---

# 👩‍💻 Autor

**Gabriele Dias**

Projeto desenvolvido para a disciplina de **Sistemas Distribuídos (APS)**.