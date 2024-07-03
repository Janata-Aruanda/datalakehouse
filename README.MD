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
```
### Passo 03: Subir os Serviços no Docker

Para iniciar os serviços no Docker, utilize o seguinte comando:

```bash
sudo docker compose up -d
```

Após realizar os passos acima, o ambiente estará configurado.

Os serviços que contêm interface gráfica são MinIO, Jupyter e Spark.

A interface gráfica do Spark pode ser acessada ao executar algum job no Spark.


### VERSÃO DO SPARK 

3.2.1


### Jars 

Jars necessario para spark escrever e ler dados no MINIO

```bash
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar 
```
```bash
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.2.1/hadoop-common-3.2.1.jar
```
```bash
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.2/hadoop-aws-3.2.2.jar
```


### Conf Spark 


```bash
config("spark.hadoop.fs.s3a.endpoint", config['aws_endpoint']) \
    .config("spark.hadoop.fs.s3a.access.key", config['aws_access_key_id']) \
    .config("spark.hadoop.fs.s3a.secret.key", config['aws_secret_access_key']) \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", 2) \
    .config("spark.logConf", "true") \
    .config("spark.logLevel", "INFO") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
    .config("spark.hadoop.fs.s3a.connection.maximum", 1000) \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.fast.upload", "true") \
    .config("spark.hadoop.fs.s3a.buffer.dir", "/tmp") \
    .config("spark.hadoop.fs.s3a.fast.upload.buffer", "disk") \
    .config("spark.hadoop.fs.s3a.attempts.maximum", 3) \
    .config("spark.hadoop.fs.s3a.multipart.size", 104857600) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl.disable.cache", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.readahead.range", 1048576) \
    .config("spark.hadoop.fs.s3a.connection.timeout", 100000) \
    .getOrCreate()
```

### Spark-Submit

```bash
spark-submit --master local[*] --jars /opt/spark/jars/hadoop-aws-3.2.2.jar,/opt/spark/jars/aws-java-sdk-bundle-1.11.901.jar job_spark.py
```
