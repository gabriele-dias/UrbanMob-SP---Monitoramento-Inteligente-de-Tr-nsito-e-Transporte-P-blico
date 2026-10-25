Tecnologias Utilizadas
Front-end Mobile

O aplicativo será desenvolvido para dispositivos Android utilizando o Android Studio, ambiente oficial de desenvolvimento para a plataforma Android. O Android Studio permitirá a criação das telas, navegação entre funcionalidades e integração com serviços externos.

Back-end

O servidor da aplicação será desenvolvido em Python, utilizando o framework Flask para disponibilizar os serviços REST responsáveis pelo fornecimento das informações de trânsito e transporte urbano.

APIs Externas
Google Maps API

A Google Maps API será utilizada para obtenção de informações relacionadas ao trânsito urbano, permitindo visualizar:

Nível de congestionamento;
Velocidade média das vias;
Intensidade do tráfego;
Mapas interativos;
Geolocalização.
Infraestrutura
Docker

O Docker será utilizado para padronizar o ambiente de execução da API, garantindo que o sistema funcione da mesma forma em qualquer computador, independentemente do sistema operacional utilizado.

Comunicação
HTTP/HTTPS

A comunicação entre o aplicativo Android e a API será realizada através dos protocolos HTTP e HTTPS, utilizando requisições REST e respostas em formato JSON.

Requisito Funcional RF01 - Consultar Trânsito

Descrição:
 O sistema deverá permitir que o usuário consulte informações sobre o trânsito urbano em tempo real.

Funcionalidades:

Visualizar o nível de congestionamento das principais vias;
Consultar a velocidade média dos veículos nas regiões monitoradas;
Visualizar a intensidade do tráfego em tempo real;
Exibir as informações em mapa interativo;
Atualizar os dados automaticamente em intervalos pré-definidos.

Entrada:

Solicitação do usuário através do aplicativo.

Processamento:

O aplicativo envia uma requisição para a API.
A API consulta os dados do Google Maps.
Os dados são processados e retornados ao aplicativo.

Saída:

Informações atualizadas sobre o trânsito exibidas na tela do dispositivo móvel.
Fluxo do RF01
Plain Text
Usuário
↓
Aplicativo Android
↓
API Transporte Urbano (Python/Flask)
↓
Google Maps API
↓
Retorno dos dados
↓
Exibição das informações de trânsito
