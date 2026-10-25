# API Transporte Urbano

Projeto desenvolvido para a disciplina de Sistemas Distribuídos com o objetivo de disponibilizar informações de trânsito através de uma API REST desenvolvida em Python/Flask.

## Objetivo

Criar uma API capaz de fornecer informações sobre trânsito urbano para um aplicativo Android.

Na primeira etapa foi implementado um endpoint simples utilizando dados simulados para validar a arquitetura da aplicação.

---

# Estrutura do Projeto

```text
api-transporte-urbano/
│
├── app.py
├── rotas.py
├── configuracao.py
├── .env
│
├── servicos/
│   └── google_maps.py
│
└── requirements.txt
```

---

# Instalação

## 1. Criar ambiente virtual

```bash
python -m venv venv
```

## 2. Ativar ambiente virtual

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

## 3. Instalar dependências

```bash
pip install flask python-dotenv requests
```

## 4. Gerar requirements

```bash
pip freeze > requirements.txt
```

---

# Funcionamento da Aplicação

A aplicação segue uma arquitetura Cliente-Servidor.

```text
Navegador
    ↓
Flask
    ↓
Rotas
    ↓
JSON
```

O navegador faz uma requisição HTTP para a API.

O Flask recebe essa requisição, localiza a rota correspondente e retorna os dados em formato JSON.

---

# Arquivo app.py

```python
from flask import Flask
from rotas import api

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
```

## Explicação

### Importação do Flask

```python
from flask import Flask
```

Importa a classe Flask responsável por criar o servidor web.

---

### Importação das rotas

```python
from rotas import api
```

Importa as rotas definidas no arquivo `rotas.py`.

---

### Criação da aplicação

```python
app = Flask(__name__)
```

Cria uma instância da aplicação Flask.

---

### Registro das rotas

```python
app.register_blueprint(api)
```

Conecta as rotas criadas em `rotas.py` à aplicação principal.

---

### Inicialização do servidor

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Inicia o servidor local na porta 5000.

O parâmetro `debug=True` permite visualizar erros detalhados durante o desenvolvimento.

---

# Arquivo rotas.py

```python
from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/traffic")
def traffic():
    return jsonify({
        "congestionamento": "Alto",
        "velocidade_media": 22,
        "intensidade": "Intensa"
    })
```

---

## Explicação

### Importação

```python
from flask import Blueprint, jsonify
```

- Blueprint organiza as rotas da aplicação.
- jsonify converte objetos Python para JSON.

---

### Criação do Blueprint

```python
api = Blueprint("api", __name__)
```

Cria um agrupamento de rotas chamado "api".

---

### Definição da rota

```python
@api.route("/traffic")
```

Determina que a função abaixo será executada quando o usuário acessar:

```text
/traffic
```

---

### Função traffic

```python
def traffic():
```

Responsável por processar a requisição.

---

### Retorno da resposta

```python
return jsonify({
    "congestionamento": "Alto",
    "velocidade_media": 22,
    "intensidade": "Intensa"
})
```

Retorna os dados em formato JSON.

---

# Fluxo da Requisição

Quando o usuário acessa:

```text
http://127.0.0.1:5000/traffic
```

O seguinte processo acontece:

```text
Usuário
    ↓
GET /traffic
    ↓
Flask
    ↓
Rotas
    ↓
Função traffic()
    ↓
jsonify()
    ↓
JSON
    ↓
Usuário
```

---

# Resposta Atual

```json
{
  "congestionamento": "Alto",
  "velocidade_media": 22,
  "intensidade": "Intensa"
}
```

---

# Tecnologias Utilizadas

- Python
- Flask
- JSON
- HTTP/HTTPS
- Git
- GitHub

---

# Próximos Passos

## Sprint 2

Implementar integração com a Google Maps API para substituir os dados simulados por informações reais de trânsito.

## Sprint 3

Containerização utilizando Docker.

## Sprint 4

Desenvolvimento do aplicativo Android.

## Sprint 5

Integração entre Android e API Flask.

---



Projeto acadêmico desenvolvido para a disciplina de Sistemas Distribuídos.