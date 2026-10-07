from pyspark.sql import SparkSession
from transaction import ecommerce_transaction

if __name__=='__main__':
    spark= SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    ecommerce_transaction(spark)