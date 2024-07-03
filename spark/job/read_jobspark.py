import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Carregar configurações do arquivo JSON
with open('config.json') as f:
    config = json.load(f)

# Configuração do SparkSession com recursos otimizados
spark = SparkSession.builder \
    .appName("PySpark S3 Example") \
    .config("spark.hadoop.fs.s3a.endpoint", config['aws_endpoint']) \
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

# Exemplo de leitura de DataFrame a partir de arquivo PARQUET no S3
df = spark.read.parquet("s3a://raw/testev2.parquet")

# Exibir os primeiros registros do DataFrame
df.show()

# Encerrar SparkSession
spark.stop()
