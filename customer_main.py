from pyspark.sql import SparkSession
from customer_method import customer_method


if __name__== '__main__':
  spark = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

  customer_method(spark)









