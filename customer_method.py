from pyspark.sql.types import  StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql import SparkSession
def customer_method(spark):
    customer_data = [("Smith", 23, 5.3),
                     ("Rashmi", 27, 5.8),
                     ("Smith", 23, 5.3),
                     ("Payal", 27, 5.8),
                     ("Megha", 27, 5.4)]

    customer_datatype = StructType([StructField("Name", StringType(), True),
                                    StructField("Age", IntegerType(), True),
                                    StructField("Height", DoubleType(), True)])
    df = spark.createDataFrame(customer_data, customer_datatype)
    df.show()
    df.printSchema()

    distinctDF = df.distinct()
    print("Distinct count: " + str(distinctDF.count()))
    distinctDF.show(truncate=False)

    df2 = df.dropDuplicates()
    print("Distinct count: " + str(df2.count()))
    df2.show(truncate=False)

    dropDisDF = df.dropDuplicates(["Age", "Height"])
    print("Distinct count of Age and Height: " + str(dropDisDF.count()))
    dropDisDF.show(truncate=False)


