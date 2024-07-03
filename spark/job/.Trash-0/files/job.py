import json
from pyspark.sql import SparkSession, F
from pyspark.sql.functions import col

# Carregar configurações do arquivo JSON
with open('config.json') as f:
    config = json.load(f)

# Configuração do SparkSession com recursos otimizados
spark = SparkSession.builder \
    .appName("PySpark MinIO Example") \
    .config("spark.hadoop.fs.s3a.endpoint", config['aws_endpoint']) \
    .config("spark.hadoop.fs.s3a.access.key", config['aws_access_key_id']) \
    .config("spark.hadoop.fs.s3a.secret.key", config['aws_secret_access_key']) \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", 2) \
    .config("spark.logConf", "true") \
    .config("spark.logLevel", "DEBUG") \
    .getOrCreate()

# Exemplo de criação de DataFrame
data = [("Alice", 28), ("Bob", 25), ("Charlie", 30)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# **Monitor job using Spark Web UI:**
print("Spark Web UI address:", spark.sparkContext.uiWebUrl)

# **Monitor job stages using getExecutorInfos():**
executors = spark.sparkContext.statusTracker.getExecutorInfos()
for executor in executors:
    print(f"Executor ID: {executor.id}, Host: {executor.host}, Tasks: {executor.activeTasks}")
    # You can further iterate through executor.rddTasks() for detailed task information.

# Salvar DataFrame no MinIO com compressão Snappy
df.write.mode("overwrite").option("header", "true").option("compression", "snappy").csv("s3a://raw/teste_sp_v1.csv")

# Encerrar SparkSession
spark.stop()