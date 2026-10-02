from pyspark.sql import SparkSession

from car_method import car_method

if __name__== '__main__':
  spark = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()
  car_method(spark)