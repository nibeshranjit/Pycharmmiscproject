pyspark --packagesorg.apache.hadoop: hadoop-aws:3.3.4
hadoop_conf = spark._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.access.key", "YOUR_ACCESS_KEY")
hadoop_conf.set("fs.s3a.secret.key", "YOUR_SECRET_KEY")
hadoop_conf.set("fs.s3a.endpoint", "s3.amazonaws.com")

df = spark.read.csv("s3a://your-bucket-name/path/to/file.csv", header=True, inferSchema=True)
df.show()