# PROJETO DATALAKEHOUSE

Projeto utilizando soluções open-source.

Ambiente com o intuito de praticar com tecnologias que o mercado utiliza, com a intenção de aumentar os serviços.

## Serviços:

- **DOCKER**: Utilizado para empacotar e distribuir aplicações.
- **MINIO**: Armazenamento de objetos compatível com a API AWS S3.
- **SPARK**: Processamento de dados distribuído.
- **TRINO**: Mecanismo de consulta SQL distribuído.
- **JUPYTER**: Ambiente de notebook interativo para análise de dados.
- **HIVE METASTORE**: Armazenamento de metadados para o Hive.

## Subir o Ambiente

### Passo 01: Instalar Docker e Docker Compose

Para instalar Docker e Docker Compose, siga as instruções em: [Documentação Docker](https://docs.docker.com/engine/install/ubuntu/)

### Passo 02: Buildar a Imagem do Spark

No diretório `spark/imagem` que contém um Dockerfile e um arquivo requirements.txt específico para sua aplicação, execute o seguinte comando:

```bash
sudo docker build . -t sparkhome

### Passo 03: Subir os Serviços no Docker

Para iniciar os serviços no Docker, utilize o seguinte comando:

```bash
sudo docker compose up -d


Após realizar os passos acima, o ambiente estará configurado.

Os serviços que contêm interface gráfica são MinIO, Jupyter e Spark.

A interface gráfica do Spark pode ser acessada ao executar algum job no Spark.
